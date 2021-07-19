## :bulb: Introduction
- API 구현 : 게시물 및 리뷰 열람 (GET), 게시물 수정 (POST), 새 리뷰 작성 (POST)
- 구조 
  - Sqlite3 격리수준 DEFERRED, 트랜잭션 Commit 전까지 Locking 상태
  - 리뷰 작성
    - <b>`POST request` :arrow_right: `Redis lpush` :arrow_right: `rpop` :arrow_right: `Sqlite3 Insert`</b>
    - 비동기 작업의 중복 및 누락 방지
  - 그 외
    - <b>`POST/GET request` :arrow_right: `Sqlite3 Select / Update`</b>
<br><br>
## :bulb: Tasks in progress
- sqlite3 timeout(언락 대기시간) 수정
- GET/POST 파라미터 구조 일치시키기
- 테스트 코드 구현
<br><br>
## :bulb: How to run 
```bash
$ /bin/bash start.sh
```
<br>

## :bulb: Python Modules used
  - flask
  - redis
<br><br> 
## :bulb: Unit test
<br><br> 
## :bulb: API Response

#### 0. Default URI
  - `http://127.0.0.1:5000/`
```
{
  "data": "hello", 
  "error": null
}
```
#### 1. 모든 게시글 조회
  - `http://127.0.0.1:5000/board`
```
{
  "data": [
    {
      "average_review_point": 3, 
      "category": "LIVING", 
      "id": 1, 
      "last_modify_at": null, 
      "post_time": "2021-07-04 07:04:10", 
      "title": "게시글1", 
      "writer": "test1"
    }, 
    {
      "average_review_point": 0, 
      "category": "PET", 
      "id": 2, 
      "last_modify_at": null, 
      "post_time": "2021-07-10 20:35:08", 
      "title": "게시글2", 
      "writer": "test1"
    }
  ], 
  "error": null
}
```
#### 2. 카테고리에 따른 게시글 조회
##### 2-1. 존재하는 카테고리
  - `http://127.0.0.1:5000/board?category=PET`
```
{
  "data": [
    {
      "average_review_point": 0, 
      "category": "PET", 
      "id": 2, 
      "last_modify_at": null, 
      "post_time": "2021-07-10 20:35:08", 
      "title": "게시글2", 
      "writer": "test1"
    }
  ], 
  "error": null
}
```
##### 2-2. 존재하지 않는 카테고리
  - `http://127.0.0.1:5000/board?category=INFO`
```
{
  "data": "카테고리 INFO의 게시물이 없습니다.",
  "error": null
}
```
#### 3. 특정 게시물의 모든 리뷰 조회
  - `http://localhost:5000/board/1/reviews`
```
{
  "data": [
    {
      "board_id": 1, 
      "id": 1, 
      "point": 3, 
      "user_id": "test1"
    }, 
    {
      "board_id": 1, 
      "id": 2, 
      "point": 4, 
      "user_id": "test1"
    }
  ], 
  "error": null
}
```

#### 4. 게시물 수정(수정일자 업데이트)
  - `curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' "http://localhost:5000/board/modify" -d '{ "boardId": 1 }'`
```
{
  "data": [
    {
      "last_modify_at": "2021-07-19 12:32:18"
    }
  ], 
  "error": null
}
```
#### 5. 새 리뷰 추가 
  - `curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' "http://localhost:5000/board/1/review/add" -d '{ "userId": "test1", "point": 2 }'`
##### - 실제 RDB 에 삽입되기 전 데이터 반환
```
{
  "data": {
    "boardId": "1", 
    "point": 2, 
    "userId": "test1"
  }, 
  "error": null
}
```
##### - 실제 삽입, 멀티 프로세스 구동 (print)
```
{'error': None, 'data': 'PID [9508] 리뷰 등록 완료'}
{'error': None, 'data': 'PID [9510] 리뷰 등록 완료'}
{'error': None, 'data': 'PID [9508] 리뷰 등록 완료'}
{'error': None, 'data': 'PID [9510] 리뷰 등록 완료'}
```
