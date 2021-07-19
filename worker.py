import os 
import time
import json
import redis
import sqlite3 
import config 

def insert_review(rdb, msg):
    '''
    새 리뷰 삽입,
    리뷰 누적평점 및 누적개수 업데이트
    '''
    try:
        msg = json.loads(msg)
        boardId, userId, point = msg["boardId"], msg["userId"], msg["point"]
    
        rdb.execute('INSERT INTO reviews(id, board_id, user_id, point) VALUES (null, ?, ?, ?)', (boardId, userId, point,)) 
        total_point, total_rev_cnt = rdb.execute('SELECT total_point, total_rev_cnt FROM board WHERE id = ?', (boardId,)).fetchone()
        rdb.execute('UPDATE board SET total_point = ? WHERE id = ?', (total_point + point, boardId,))
        rdb.execute('UPDATE board SET total_rev_cnt = ? WHERE id = ?', (total_rev_cnt + 1, boardId,))
        rdb.commit()
        
        time.sleep(2)  # 연산속도 느리게 하기        
        return None, f'PID [{os.getpid()}] 리뷰 등록 완료' 
    except sqlite3.DatabaseError as e:
        return e, None 


rq = redis.from_url(config.CONFIG['REDIS_URL'])
rdb = sqlite3.connect(
        config.CONFIG['DATABASE']
)
while True:
    msg = rq.brpop('review', 0)[1]
    error, data = insert_review(rdb, msg)
    print({'error': error, 'data': data})
rdb.close()
