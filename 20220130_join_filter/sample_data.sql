CREATE TABLE DEPARTMENTS(
	ID INTEGER,
	NAME CHAR(20),
	LOCATION CHAR(20)
);

CREATE TABLE EMPLOYEES(
	ID INTEGER,
	NAME CHAR(20),
	LAST_NAME CHAR(20),
	DEPT_ID INTEGER,
	MGR_ID INTEGER
);

INSERT INTO DEPARTMENTS (ID, NAME, LOCATION) VALUES(1, 'SALES', 'BERLIN');
INSERT INTO DEPARTMENTS (ID, NAME, LOCATION) VALUES(2, 'IT', 'BERLIN');
INSERT INTO DEPARTMENTS (ID, NAME, LOCATION) VALUES(3, 'HR', 'BERLIN');
INSERT INTO DEPARTMENTS (ID, NAME, LOCATION) VALUES(4, 'WAREHOUSE', 'HAMBURG');
INSERT INTO DEPARTMENTS (ID, NAME, LOCATION) VALUES(5, 'PROCUREMENT', 'HAMBURG');

INSERT INTO EMPLOYEES (ID, NAME, LAST_NAME, DEPT_ID, MGR_ID) VALUES (1, 'JOHN', 'GREEN', 1, 3);
INSERT INTO EMPLOYEES (ID, NAME, LAST_NAME, DEPT_ID, MGR_ID) VALUES (2, 'JANE', 'BRAUN', 1, 3);
INSERT INTO EMPLOYEES (ID, NAME, LAST_NAME, DEPT_ID, MGR_ID) VALUES (3, 'AHMAD', 'DOE', 3, NULL);
INSERT INTO EMPLOYEES (ID, NAME, LAST_NAME, DEPT_ID, MGR_ID) VALUES (4, 'LISA', 'MUSTERMANN', 5, 3);
INSERT INTO EMPLOYEES (ID, NAME, LAST_NAME, DEPT_ID, MGR_ID) VALUES (5, 'DMITRY', 'BLACK', 4, 3);
INSERT INTO EMPLOYEES (ID, NAME, LAST_NAME, DEPT_ID, MGR_ID) VALUES (6, 'CANBURAK', 'TUMER', 4, 3);

COMMIT;