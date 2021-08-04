BEGIN TRANSACTION;

/* Create a table called NAMES */
CREATE TABLE NAMES(Id integer , Name text);

/* Create few records in this table */
INSERT INTO NAMES VALUES(1,'Tom');
INSERT INTO NAMES VALUES(2,'Lucy');
INSERT INTO NAMES VALUES(3,'Frank');
INSERT INTO NAMES VALUES(4,'Jane');
INSERT INTO NAMES VALUES(5,'Robert');
INSERT INTO NAMES VALUES(5,'Robert');
COMMIT;

/* Display all the records from the table */
SELECT DISTINCT Name FROM NAMES where Name LIKE '%a%';
SELECT * FROM NAMES where Name LIKE '%a%';
SELECT * FROM NAMES where Name IN ('Robert','Lucy','Tom');

SELECT * FROM NAMES where NOT Name == 'Tom';


SELECT * FROM NAMES where NOT Name == 'Tom' order by Name;



