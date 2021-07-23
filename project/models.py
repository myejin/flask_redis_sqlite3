from datetime import datetime, timedelta
import sqlite3
from . import db

def get_posts(cat):
    """카테고리에 따른 게시글 조회"""

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
        data = f'카테고리 {cat}의 게시물이 없습니다.'
    return None, data 


def datetime_modify(id):
    """게시글 수정으로 last_modify_at 업데이트"""

    db.get_db().execute('UPDATE board SET last_modify_at = CURRENT_TIMESTAMP WHERE id = ?', (id, ))
    db.get_db().commit()
    row = db.get_db().execute('SELECT last_modify_at FROM board WHERE id = ?', (id,)).fetchone()[0]
    data = [{ 'last_modify_at' : row }]
    return None, data


def get_specific_reviews(boardId):
    """특정 게시글의 리뷰 조회"""
    
    rows = db.get_db().execute('SELECT * FROM reviews WHERE board_id = ?', (boardId,))
    data = []
    for row in rows:
        data.append({'id': row[0], 'board_id': row[1], 'user_id': row[2], 'point': row[3]})

    if not data:
        data = f'게시글 {boardId}의 리뷰가 없습니다.'
    return None, data
