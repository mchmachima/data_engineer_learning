::page{title=""}

# Hands-on Lab: Getting Started with the PostgreSQL Command Line

<img src="
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/images/IBM_logo.png"
width="300">

**Estimated time needed:** 20 minutes

##

In this lab, you will use the PostgreSQL command line interface (CLI) to create a database and restore the structure and contents of its tables. Then, you will learn how to explore and query tables. Finally, you will learn how to dump/backup tables from a database.

## Software used in this lab

In this lab, you will use a [PostgreSQL Database](https://www.postgresql.org/ "PostgreSQL Database"). PostgreSQL is a relational database management system (RDBMS) designed to store, manipulate, and retrieve data efficiently.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20PostgreSQL%20command%20line/images/postgresql.png" width="130" height="100">
<p>

To complete this lab, you will utilize the PostgreSQL relational database service available as part of IBM Skills Network Labs (SN Labs) Cloud IDE. SN Labs is a virtual lab environment used in this course.

## Database used in this lab

The Sakila database used in this lab comes from the following source: https://dev.mysql.com/doc/sakila/en/ under [New BSD license](https://opensource.org/licenses/bsd-license.php) [Copyright 2021 - Oracle Corporation].

You will use a modified version of the database for the lab. To follow the lab instructions successfully, please use the database provided by the lab rather than the database from the source.

The following entity relation diagram (ERD) shows the structure of the schema of the Sakila database:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_ERD.jpg" width="500" height="592">

## Objectives

After completing this lab, you will be able to use the PostgreSQL command line to:

- Create a database
- Restore the structure and data of a table
- Explore and query tables
- Dump/backup tables from a database

## Lab structure

In this exercise, you will go through several subtasks where you will use the PostgreSQL command line interface (CLI) to create a database and restore the structure and contents of tables. Then, you will learn how to explore and query tables. Finally, you will learn how to dump/backup tables from a database.

## Task A: Create a database

To get started with this lab, launch PostgreSQL using the Cloud IDE. You can do this by following these steps:

1. Click the Skills Network extension button on the left side of the window.

2. Open the **DATABASES**  menu and click **PostgreSQL**.

3. Click **Create**. PostgreSQL may take a few moments to start.

    ![postgres start pic.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/4zLhpz5CI5tmSl-DH7NRXQ/postgres%20start%20pic.png)

5. Open a new command terminal by clicking **New Terminal**.

    ![new_terminal.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/11lV-AftgBDWDL5bDvv8fQ/new-terminal.png)

6. Copy the command below by clicking the little copy button on the right of the code block and then paste it into the terminal using **Ctrl + V** (Mac: ⌘ + V) to fetch the [sakila_pgsql_dump.sql](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_pgsql_dump.sql) file to the Cloud IDE.

    ```
    wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_pgsql_dump.sql
    ```


    ![wget command1.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/P8B84giC7C0w2FL_A5Tv5g/wget%20command1.png)

9. Now, open the PostgreSQL Command Line Interface (CLI) by clicking **PostgreSQL CLI**.

    ![create_database.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/xym6v5sbYzGIfh2E_C1VQQ/create-database.png)

10. Create a new database named **sakila** using the following command in the terminal:

    ```
    create database sakila;
    ```
	![create_database.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/xym6v5sbYzGIfh2E_C1VQQ/create-database.png)

    > **Note:** You are using the **create database** command to create a new database within the PostgreSQL CLI. To create a new database named sakila outside the command line interface, you can use the following command directly in a terminal window: `createdb --username=postgres --host=postgres --password sakila` after quitting the psql command prompt session with the command `\q.`

## Task B: Restore the structure and data of a table

1. To connect to the newly created empty sakila database, use the following command in the terminal and enter your PostgreSQL service session password:

    ```
    \connect sakila;
    ```

    ![connect sakila.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/xt_LySyANqW2PMSKz7qtAA/connect%20sakila.png)

2. Restore the sakila PostgreSQL dump file (containing the sakila database table definitions and data) to the newly created empty sakila database by using the following command in the terminal:

    ```
    \include sakila_pgsql_dump.sql;
    ```



    ![include sakila.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/L-rn7MbcufaA9jKnu9H_tQ/include%20sakila.png)

    > **Note:** You are using the **\include** command to restore the database dump file within the PostgreSQL CLI. To restore the database dump file outside of the Command Line Interface, you can use the command `pg_restore --username=postgres --host=postgres --password --dbname=sakila < sakila_pgsql_dump.tar` after quitting the CLI prompt session with the command `\q.` Non-text format **.tar** dumps are restored using the **pg_restore** command. So, before using the **pg_restore** command, first, fetch the .tar version of this dump file using the command `wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_pgsql_dump.tar`

3. Repeat Step 1 to reconnect to the sakila database after restoring the dump file.

## Task C: Explore and query tables

1. To list all the table names from the sakila database, use the following command in the terminal:

    ```
    \dt
    ```



    ![reconnect and dt.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/gPzIJQKvOYGTzMsr177QQQ/reconnect%20and%20dt.png)

2. Explore the structure of the **store** table using the following command in the terminal:

    ```
    \d store;
    ```



    ![d store.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/18SDpibLyNuZxMx_0BZDsw/d%20store.png)

3. Retrieve all the records from the **store** table using the following command in the terminal:

    ```
    SELECT * FROM store;
    ```



    ![select stmt.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/QdQfSs7JpRV9XJ6uVF42aQ/select%20stmt.png)

4. Quit the PostgreSQL command prompt session using the following command in the terminal.

    ```
    \q
    ```



    ![quit sakila.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/mJx4e0SEZLbz-roB9tRSXg/quit%20sakila.png)

## Task D: Dump/backup tables from a database

1. Finally, to dump/backup the **store** table from the database, use the following command in the terminal and enter your PostgreSQL service session password:

    ```
    pg_dump --username=postgres --host=postgres --password --dbname=sakila --table=store --format=plain > sakila_store_pgsql_dump.sql
    ```



    > **Note:** To only dump/backup the table **store** from the database in non-text format **.tar**, you can use the command `pg_dump --username=postgres --host=postgres --password --dbname=sakila --table=store --format=tar > sakila_store_pgsql_dump.tar`

2. To view the dump file within the terminal, use the following command:

    ```
    cat sakila_store_pgsql_dump.sql
    ```



    ![dumpfile](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20PostgreSQL%20command%20line/images/1.15.png)

## Conclusion

Congratulations! You have completed this lab, and now you have learned how to create a database, restore the structure and data of a table, explore and query tables, and dump/backup tables from a database.

<br>

#### Author: [Sandip Saha Joy](https://www.linkedin.com/in/sandipsahajoy/)

#### Other Contributors: [David Pasternak](https://www.linkedin.com/in/david-pasternak-6b84a2208/)

<footer>
<img align="left" src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PDM101EN-Coursera/SNIBMfooter.png" alt="">
</footer>

	
## <h3> © IBM Corporation. All rights reserved. <h3/>
	
	
<!---
## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2021-03-15 | 1.0 | Sandip Saha Joy | Created initial version |
| 2021-10-18 | 1.1 | David Pasternak | Updated lab instructions |
| 2024-01-29 | 1.2 | Anita Narain | ID reviewed lab |
| 2024-01-30 | 1.3 | Mary Stenberg | QA pass with edits |



-->