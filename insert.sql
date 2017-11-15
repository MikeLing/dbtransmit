DROP TABLE IF EXISTS tbl_test;

CREATE TABLE tbl_test(id INT NOT NULL DEFAULT 1, name text, PRIMARY KEY(id));
INSERT INTO tbl_test VALUES (2, "hello");
UPDATE tbl_test SET name = "abc" where id = 2;
