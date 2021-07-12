DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS board;
DROP TABLE IF EXISTS reviews;

CREATE TABLE users (id varchar(20) PRIMARY key, --사용자 아이디 PK
 name varchar(10) NOT NULL, --사용자명
 passwd varchar(90) NOT NULL --로그인 비밀번호
);

CREATE TABLE board (id integer PRIMARY key autoincrement, --게시판 PK
 title varchar(20) NOT NULL, --게시판 제목
 writer varchar(20) NOT NULL, --게시판 작성자 아이디
 category text check (category in ('COOK', 'LIVING', 'INTERIOR', 'PET')) NOT NULL , --카테고리
 post_time datetime NOT NULL, --게시글 업로드 시각
 last_modify_at datetime DEFAULT NULL, --마지막 수정 시각
 total_point int NOT NULL DEFAULT 0, --누적평점
 total_rev_cnt int NOT NULL DEFAULT 0, --누적리뷰개수
 FOREIGN KEY(writer) REFERENCES users(id)
);

CREATE TABLE reviews(id integer PRIMARY key autoincrement, --리뷰 PK
 board_id integer NOT NULL, --게시글 아이디 
 user_id varchar(20) NOT NULL, --리뷰어 아이디, not UNIQUE
 point int check (point in (1, 2, 3, 4, 5)) NOT NULL, --평점
 FOREIGN KEY(board_id) REFERENCES board(id),
 FOREIGN KEY(user_id) REFERENCES users(id)
);

