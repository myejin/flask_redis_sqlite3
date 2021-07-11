from datetime import datetime, timedelta
from . import db

def get_posts(cat):
    # 카테고리에 따른 게시글 조회
    if cat is None:
        rows = db.get_db().execute('SELECT *, total_point/total_rev_cnt as aver FROM board ORDER BY aver DESC, id DESC')
    else:
        rows = db.get_db().execute('SELECT *, total_point/total_rev_cnt as aver FROM board WHERE category = ? ORDER BY aver DESC, id DESC', (cat,))

    data = []
    for row in rows:
        aver = 0
        if row[8]:
            aver = row[8]
        data.append({'id': row[0], 'title': row[1], 'writer': row[2], 'category': row[3], 'post_time': row[4], 'last_modify_at': row[5], 'average_review_point': aver})
    
    if not data:
        if cat is None:
            cat = '전체'
        return f'카테고리 {cat}의 게시물이 없습니다.', None
    return None, data 


def datetime_modify(id):
    # 게시글 수정으로 last_modify_at 업데이트 
    before = db.get_db().execute('SELECT last_modify_at as aver FROM board WHERE id = ?', (id,)).fetchone()[0]
    db.get_db().execute('UPDATE board SET last_modify_at = CURRENT_TIMESTAMP WHERE id = ?', (id, ))
    after = db.get_db().execute('SELECT last_modify_at FROM board WHERE id = ?', (id,)).fetchone()[0]

    if after == before:
        return f'게시글 수정을 실패했습니다.', None

    data = [{'before': before, 'after': after}]
    return None, data
