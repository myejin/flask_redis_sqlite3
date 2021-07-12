## 프로젝트 개요
게시물 추가, 수정, 삭제와 리뷰 관리 API 구현
<br><br>

## 실행방법

<br><br>

## 파이썬 모듈
  - flask
<br><br>

## API 테스트 (임시 기록용)

#### 1. UI 테스트 
  - `http://127.0.0.1:5000/`
```
{
  "data": "hello", 
  "error": null
}
```
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
  - `http://127.0.0.1:5000/board?category=INFO`
```
{
  "data": null, 
  "error": "카테고리 INFO의 게시물이 없습니다."
}
```
#### 2. Curl 테스트
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



## 유닛 테스트
