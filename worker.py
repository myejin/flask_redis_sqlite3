import os 
import time
import json
import redis
import sqlite3 
import config 

def insert_review(rdb, msg):
    # 새 리뷰 삽입
    msg = json.loads(msg)
    boardId, userId, point = msg["boardId"], msg["userId"], msg["point"]
    
    before = rdb.execute('SELECT count(*) FROM reviews').fetchone()[0]
    rdb.execute('INSERT INTO reviews(id, board_id, user_id, point) VALUES (null, ?, ?, ?)', (boardId, userId, point))
    after = rdb.execute('SELECT count(*) FROM reviews').fetchone()[0]
    
    if after == before:
        return f'리뷰 등록을 실패했습니다.'
    return None


rq = redis.from_url(config.CONFIG['REDIS_URL'])
while True:
    if not rq.llen('review'):
        continue

    rdb = sqlite3.connect(
        config.CONFIG['DATABASE'],
        isolation_level=None    
    )
    count = min(10, rq.llen('review'))
    print('쌓인 데이터 수: ', count)
    i = 0
    while i < count:
        msg = rq.rpop('review')
        ret = insert_review(rdb, msg)
        if ret is None:
            print('리뷰 등록 완료') 
        #else: # 에러가 있다면..
        time.sleep(2)  # 연산속도 느리게 하기        
        i += 1
    rdb.close()
