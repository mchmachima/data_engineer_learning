# SQL Cheat Sheet: Join Statements

Reference cheat sheet for various SQL JOIN commands, their syntax, descriptions, and examples.

---

## Joins

| Topic | Syntax | Description | Example |
| --- | --- | --- | --- |
| Cross Join | `SELECT column_name(s) FROM table1 CROSS JOIN table2;` | The CROSS JOIN is used to generate a paired combination of each row of the first table with each row of the second table. | `SELECT DEPT_ID_DEP, LOCT_ID FROM DEPARTMENTS CROSS JOIN LOCATIONS;` |
| Inner Join | `SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name WHERE condition;` | You can use an inner join in a SELECT statement to retrieve only the rows that satisfy the join conditions on every specified table. | `select E.F_NAME,E.L_NAME, JH.START_DATE from EMPLOYEES as E INNER JOIN JOB_HISTORY as JH on E.EMP_ID=JH.EMPL_ID where E.DEP_ID ='5';` |
| Left Outer Join | `SELECT column_name(s) FROM table1 LEFT OUTER JOIN table2 ON table1.column_name = table2.column_name WHERE condition;` | The LEFT OUTER JOIN will return all records from the left side table and the matching records from the right table. | `select E.EMP_ID,E.L_NAME,E.DEP_ID,D.DEP_NAME from EMPLOYEES AS E LEFT OUTER JOIN DEPARTMENTS AS D ON E.DEP_ID=D.DEPT_ID_DEP;` |
| Right Outer Join | `SELECT column_name(s) FROM table1 RIGHT OUTER JOIN table2 ON table1.column_name = table2.column_name WHERE condition;` | The RIGHT OUTER JOIN returns all records from the right table, and the matching records from the left table. | `select E.EMP_ID,E.L_NAME,E.DEP_ID,D.DEP_NAME from EMPLOYEES AS E RIGHT OUTER JOIN DEPARTMENTS AS D ON E.DEP_ID=D.DEPT_ID_DEP;` |
| Full Outer Join | `SELECT column_name(s) FROM table1 FULL OUTER JOIN table2 ON table1.column_name = table2.column_name WHERE condition;` | The FULL OUTER JOIN clause results in the inclusion of rows from two tables. If a value is missing when rows are joined, that value is null in the result table. | `select E.F_NAME,E.L_NAME,D.DEP_NAME from EMPLOYEES AS E FULL OUTER JOIN DEPARTMENTS AS D ON E.DEP_ID=D.DEPT_ID_DEP;` |
| Self Join | `SELECT column_name(s) FROM table1 T1, table1 T2 WHERE condition;` | A self join is a regular join, but it can be used to join a table with itself. | `SELECT B.* FROM EMPLOYEES A JOIN EMPLOYEES B ON A.MANAGER_ID = B.MANAGER_ID WHERE A.EMP_ID = 'E1001';` |

---

## Joins in MySQL Using phpMyAdmin

| Topic | Syntax | Description | Example |
| --- | --- | --- | --- |
| Full Outer Join | `SELECT column_name(s) FROM table1 LEFT OUTER JOIN table2 ON table1.column_name = table2.column_name WHERE condition UNION SELECT column_name(s) FROM table1 RIGHT OUTER JOIN table2 ON table1.column_name = table2.column_name WHERE condition;` | MySQL has no native FULL OUTER JOIN. The UNION operator is used to combine the result-set of a LEFT OUTER JOIN and a RIGHT OUTER JOIN to simulate one. | `select E.F_NAME,E.L_NAME,D.DEP_NAME from EMPLOYEES AS E LEFT OUTER JOIN DEPARTMENTS AS D ON E.DEP_ID=D.DEPT_ID_DEP UNION select E.F_NAME,E.L_NAME,D.DEP_NAME from EMPLOYEES AS E RIGHT OUTER JOIN DEPARTMENTS AS D ON E.DEP_ID=D.DEPT_ID_DEP;` |
