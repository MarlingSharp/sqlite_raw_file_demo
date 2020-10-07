CREATE TABLE student (
  id integer PRIMARY KEY,
  name text NOT NULL,
  age integer NOT NULL
);

INSERT INTO student (name, age) VALUES ("Harry Potter", 15);
INSERT INTO student (name, age) VALUES ("Ronald Weasley", 16);
INSERT INTO student (name, age) VALUES ("Hermione Granger", 15);

SELECT id, name FROM student;

DELETE FROM student WHERE name='Harry Potter';

SELECT name FROM student;
