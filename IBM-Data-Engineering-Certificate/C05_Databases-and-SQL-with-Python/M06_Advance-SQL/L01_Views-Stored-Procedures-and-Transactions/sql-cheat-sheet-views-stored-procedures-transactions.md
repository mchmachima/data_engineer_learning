# SQL Cheat Sheet: Views, Stored Procedures and Transactions

Reference cheat sheet for various SQL commands related to views, stored procedures, and transactions — their syntax, descriptions, and examples.

> Note: some examples below were truncated in the original source material (numbered code blocks whose later lines were not captured when copied). They are reproduced as-is rather than filled in, to avoid inventing SQL that wasn't actually provided.

---

## Views

### Create View

**Syntax:**
```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Description:** A CREATE VIEW is an alternative way of representing data that exists in one or more tables.

**Example:**
```sql
CREATE VIEW EMPSALARY AS
SELECT EMP_ID, F_NAME, L_NAME, B_DATE, SEX, SALARY
FROM EMPLOYEES;
```

### Update a View

**Syntax:**
```sql
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Description:** The CREATE OR REPLACE VIEW command updates a view.

**Example:**
```sql
CREATE OR REPLACE VIEW EMPSALARY AS
SELECT EMP_ID, F_NAME, L_NAME, B_DATE, SEX, JOB_TITLE, MIN_SALARY, MAX_SALARY
FROM EMPLOYEES, JOBS
WHERE EMPLOYEES.JOB_ID = JOBS.JOB_IDENT;
```

### Drop a View

**Syntax:**
```sql
DROP VIEW view_name;
```

**Description:** Use the DROP VIEW statement to remove a view from the database.

**Example:**
```sql
DROP VIEW EMPSALARY;
```

---

## Stored Procedures in IBM DB2 Using SQL

### Stored Procedures

**Syntax:**
```sql
--#SET TERMINATOR @
CREATE PROCEDURE PROCEDURE_NAME
LANGUAGE ...
BEGIN
    ...
END
@
```

**Description:** A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again. The default terminator for a stored procedure is semicolon (`;`). To set a different terminator, use the `SET TERMINATOR` clause followed by the terminator, such as `@`.

**Example:** *(truncated in source)*
```sql
--#SET TERMINATOR @
CREATE PROCEDURE RETRIEVE_ALL
LANGUAGE SQL
READS SQL DATA
DYNAMIC RESULT SETS 1
BEGIN
    DECLARE C1 CURSOR
        WITH RETURN FOR
        SELECT * FROM PETSALE;
    -- (remainder of example not captured in source)
```

---

## Stored Procedures in MySQL Using phpMyAdmin

### Stored Procedures

**Syntax:**
```sql
DELIMITER //

CREATE PROCEDURE PROCEDURE_NAME
BEGIN
    ...
END //

DELIMITER ;
```

**Description:** A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again. The default terminator for a stored procedure is semicolon (`;`). To set a different terminator, use the `DELIMITER` clause followed by the terminator, such as `$$` or `//`.

**Example:**
```sql
DELIMITER //

CREATE PROCEDURE RETRIEVE_ALL()
BEGIN
    SELECT * FROM PETSALE;
END //

DELIMITER ;
```

---

## Transactions with DB2

### Commit Command

**Syntax:**
```sql
COMMIT;
```

**Description:** A COMMIT command is used to persist the changes in the database. The default terminator for a COMMIT command is semicolon (`;`).

**Example:** *(truncated in source)*
```sql
CREATE TABLE employee (
    ID INT,
    Name VARCHAR(20),
    City VARCHAR(20),
    Salary INT,
    Age INT
);

INSERT INTO employee (ID, Name, City, Salary, Age)
VALUES
    -- (remainder of example not captured in source)
```

### Rollback Command

**Syntax:**
```sql
ROLLBACK;
```

**Description:** A ROLLBACK command is used to roll back the transactions which are not saved in the database. The default terminator for a ROLLBACK command is semicolon (`;`).

As auto-commit is enabled by default, all transactions will be committed. We need to disable this option to see how rollback works. For DB2, auto-commit has to be disabled manually: click the gear icon on the right side of the SQL Assistant window, select the "On Success" drop-down, and choose "commit after the last statement in the script." Remember to save the changes.

**Example:**
```sql
INSERT INTO employee
VALUES (3, 'Swetha Tiwari', 'Kanpur', 38000, 38);

SELECT * FROM employee;

ROLLBACK;

SELECT * FROM employee;
```

---

## Transactions with MySQL

### Commit Command

**Syntax:**
```sql
COMMIT;
```

**Description:** A COMMIT command is used to persist the changes in the database. The default terminator for a COMMIT command is semicolon (`;`).

**Example:** *(truncated in source)*
```sql
CREATE TABLE employee (
    ID INT,
    Name VARCHAR(20),
    City VARCHAR(20),
    Salary INT,
    Age INT
);

START TRANSACTION;
    -- (remainder of example not captured in source)
```

### Rollback Command

**Syntax:**
```sql
ROLLBACK;
```

**Description:** A ROLLBACK command is used to roll back the transactions which are not saved in the database. The default terminator for a ROLLBACK command is semicolon (`;`).

As auto-commit is enabled by default, all transactions will be committed. We need to disable this option to see how rollback works. For MySQL, use the command `SET autocommit = 0;`.

**Example:**
```sql
INSERT INTO employee
VALUES (3, 'Swetha Tiwari', 'Kanpur', 38000, 38);

SELECT * FROM employee;

ROLLBACK;

SELECT * FROM employee;
```

---

## DB2 Transactions Using Stored Procedure

### Commit Command

**Syntax:**
```sql
DELIMITER //

CREATE PROCEDURE PROCEDURE_NAME
BEGIN
    COMMIT;
END //

DELIMITER ;
```

**Description:** A COMMIT command is used to persist the changes in the database. The default terminator for a COMMIT command is semicolon (`;`).

**Example:** *(truncated in source)*
```sql
--#SET TERMINATOR @

CREATE PROCEDURE TRANSACTION_ROSE
LANGUAGE SQL
MODIFIES SQL DATA
BEGIN
    DECLARE SQLCODE INTEGER DEFAULT 0;
    DECLARE retcode INTEGER DEFAULT 0;

    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    -- (remainder of example not captured in source)
```

### Rollback Command

**Syntax:**
```sql
--#SET TERMINATOR @
CREATE PROCEDURE PROCEDURE_NAME
BEGIN
    ROLLBACK;
    COMMIT;
END
@
```

**Description:** A ROLLBACK command is used to roll back the transactions which are not saved in the database. The default terminator for a ROLLBACK command is semicolon (`;`).

**Example:** *(truncated in source)*
```sql
--#SET TERMINATOR @

CREATE PROCEDURE TRANSACTION_ROSE
LANGUAGE SQL
MODIFIES SQL DATA
BEGIN
    DECLARE SQLCODE INTEGER DEFAULT 0;
    DECLARE retcode INTEGER DEFAULT 0;

    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    -- (remainder of example not captured in source)
```

---

## MySQL Transactions Using Stored Procedure

### Commit Command

**Syntax:**
```sql
DELIMITER //

CREATE PROCEDURE PROCEDURE_NAME
BEGIN
    COMMIT;
END //

DELIMITER ;
```

**Description:** A COMMIT command is used to persist the changes in the database. The default terminator for a COMMIT command is semicolon (`;`).

**Example:** *(truncated in source)*
```sql
DELIMITER //

CREATE PROCEDURE TRANSACTION_ROSE()
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    -- (remainder of example not captured in source)
```

### Rollback Command

**Syntax:**
```sql
DELIMITER //

CREATE PROCEDURE PROCEDURE_NAME
BEGIN
    ROLLBACK;
    COMMIT;
END //

DELIMITER ;
```

**Description:** A ROLLBACK command is used to roll back the transactions which are not saved in the database. The default terminator for a ROLLBACK command is semicolon (`;`).

**Example:** *(not captured in source — original was cut off entirely)*
