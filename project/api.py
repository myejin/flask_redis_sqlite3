import json
from flask import jsonify, Blueprint, request 
from .models import get_posts, datetime_modify, get_specific_reviews
from . import rq 
bp = Blueprint("board", __name__)

def get_response(error, data):
    return {"error": error, "data": data}


@bp.route("/")
def index():
    response = {"error": None, "data": "hello"}
    return jsonify(response)


@bp.route("/board")
def board_category():
    req = request.args 

    cat = None
    if 'category' in req:
        cat = req['category']

    error, data = get_posts(cat)

    resp = get_response(error, data)    
    return jsonify(resp)


@bp.route("/board/modify", methods = ['POST'])
def posts_modify(): 
    req = request.get_json()

    error, data = datetime_modify(req["boardId"])

    resp = get_response(error, data)    
    return jsonify(resp)
# curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' "http://localhost:5000/board/modify" -d '{ "boardId": 1 }'


@bp.route("/board/<boardId>/reviews")
def reviews_specific_board(boardId): 
    req = request.args 

    error, data = get_specific_reviews(int(boardId))
    resp = get_response(error, data)     
    return jsonify(resp)


@bp.route("/board/<boardId>/review/add", methods = ['POST'])
def reviews_add(boardId): 
    req = request.get_json()
    req['boardId'] = boardId 
    rq.lpush('review', json.dumps(req))
    resp = get_response(None, '리뷰 입력 중입니다.')    
    return jsonify(resp)
# curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' "http://localhost:5000/board/1/review/add" -d '{ "userId": "test1", "point": 2 }'

