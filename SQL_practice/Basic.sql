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

/* distinct like in not */
SELECT DISTINCT Name FROM NAMES where Name LIKE '%a%';
SELECT * FROM NAMES where Name LIKE '%a%'; -- % means any number of characters
SELECT * FROM NAMES where Name LIKE '_a%'; -- _ means one character only  ------- Here a in second place
SELECT * FROM NAMES where Name IN ('Robert','Lucy','Tom');
SELECT * FROM NAMES where NOT Name == 'Tom';

-- orderby 
SELECT * FROM NAMES where NOT Name == 'Tom' order by Name;

-- null not null

SELECT * FROM NAMES where Name IS NULL;
SELECT * FROM NAMES where Name IS NOT NULL;

-- Update statements

UPDATE NAMES SET NAME = 'VIRAG' WHERE NAME = 'Tom';
SELECT * FROM NAMES;

-- delete

DELETE FROM NAMES WHERE ID == 2;
SELECT * FROM NAMES;

--LIMIT 

SELECT * FROM NAMES LIMIT 3;

--min MAX
SELECT MIN(ID) FROM NAMES;
SELECT MAX(ID) FROM NAMES;

-- COUNT SUM AVG
SELECT COUNT(ID) FROM NAMES WHERE ID <= 5;
SELECT AVG(ID) FROM NAMES WHERE ID <= 5;
SELECT SUM(ID) FROM NAMES WHERE ID <= 5;

-- between 1 and 4 included
SELECT * FROM NAMES WHERE ID between 1 and 4;


-- INNER JOIN

/* Create a table called NAMES */
CREATE TABLE NAMES(Id integer , Name text);

/* Create few records in this table */
INSERT INTO NAMES VALUES(1,'Tom');
INSERT INTO NAMES VALUES(1,'Lucy');
INSERT INTO NAMES VALUES(3,NULL);
INSERT INTO NAMES VALUES(4,'Jane');
INSERT INTO NAMES VALUES(5,'Robert');
INSERT INTO NAMES VALUES(6,'Vista');

/* Create a table called NAMES */
CREATE TABLE MARKS(GRADES integer , Name text);

/* Create few records in this table */
INSERT INTO marks VALUES(7,'Tom');
INSERT INTO marks VALUES(6,'Lucy');
INSERT INTO marks VALUES(8,'Prince');
INSERT INTO marks VALUES(9,'Jane');
INSERT INTO marks VALUES(2,'Robert');

SELECT names.name, marks.grades , names.id 
FROM names
inner join marks
on names.name == marks.name;



-- OUTPUT
/*
Tom|7|1
Lucy|6|1
Jane|9|4
Robert|2|5
*/

-- LEFT JOIN (OUTER)
SELECT names.name, marks.grades , names.id 
FROM names
left join marks
on names.name == marks.name;

--ouput
/*
Tom|7|1
Lucy|6|1
||3
Jane|9|4
Robert|2|5
Vista||6
*/

-- similarly right and full outer join

-- self join
SELECT A.name , B.name 
FROM names A , names B
where A.name <> B.name;
 
-- ouput
/*
Tom|Lucy
Tom|Jane
Tom|Robert
Tom|Vista
Lucy|Tom
Lucy|Jane
Lucy|Robert
Lucy|Vista
Jane|Tom
Jane|Lucy
Jane|Robert
Jane|Vista
Robert|Tom
Robert|Lucy
Robert|Jane
Robert|Vista
Vista|Tom
Vista|Lucy
Vista|Jane
Vista|Robert
*/

--  union and union all (Columns should be same)

select names.name from names
union 
select marks.name from marks;

-- output

-- Jane
-- Lucy
-- Prince
-- Robert
-- Tom
-- Vista


--  group by (generally used with sum,max,avg)
select count(name) from names group by id;

-- having statement (having is used after grouping and where is used before grouping statements....Having is used on aggregate functions)
--You can use both HAVING and WHERE. The WHERE clause filters on individual rows (before they are passed to the aggregate) 
-- and the HAVING clause filters on the aggregated values.

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;

        
--  more example on having

select * from names group by name having count(name) <= 2;

-- 3|
-- 4|Jane
-- 7|Lucy
-- 5|Robert
-- 6|Tom
-- 5|Vista

-- EXISTS operator is used to test for the existence of any record in a subquery.
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20);

