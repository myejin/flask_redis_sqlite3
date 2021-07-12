INSERT INTO users(id, name, passwd)
VALUES ('test1', 'hyejin', '1234');

INSERT INTO board(id, title, writer, category, post_time, total_point, total_rev_cnt)
VALUES (null, '게시글1', 'test1', 'LIVING', '2021-07-04 07:04:10', 7, 2);

INSERT INTO board(id, title, writer, category, post_time)
VALUES (null, '게시글2', 'test1', 'PET', '2021-07-10 20:35:08');

INSERT INTO reviews(id, board_id, user_id, point)
VALUES (null, 1, 'test1', 3);

INSERT INTO reviews(id, board_id, user_id, point)
VALUES (null, 1, 'test1', 4);
