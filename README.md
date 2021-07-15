## :bulb: Introduction
- 게시물 추가, 수정, 삭제와 리뷰 관리 API 구현
<br><br>
## :bulb: Tasks in progress
- Redis 연동
- GET/POST 파라미터 구조 일치시키기
- 테스트 코드 구현
<br><br>
## :bulb: How to run 

<br><br>

## :bulb: Modules used
  - flask
  - 
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
  "data": null, 
  "error": "카테고리 INFO의 게시물이 없습니다."
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
      "after": "2021-07-11 16:00:45", 
      "before": null
    }
  ], 
  "error": null
}
```
#### 5. 게시물에 대한 리뷰 
  - `curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' "http://localhost:5000/board/1/review/add" -d '{ "userId": "test1", "point": 2 }'`
```
{
  "data": [
    {
      "new_review_id": 3
    }
  ], 
  "error": null
}
```
