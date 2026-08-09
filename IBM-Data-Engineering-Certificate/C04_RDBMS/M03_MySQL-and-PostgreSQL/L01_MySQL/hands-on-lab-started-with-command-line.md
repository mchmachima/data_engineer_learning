::page{title="Hands-on Lab: Getting Started with MySQL Command Line"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/images/IDSN-logo.png" width="300"><br>

##

**Estimated time needed:** 20 minutes

In this lab, you will use the MySQL command line interface (CLI) to create a database, restore the structure and contents of tables, explore and query tables, and finally, learn how to dump/backup tables from the database.

## Objectives

After completing this lab, you will be able to use the MySQL command line to:

- Create a database.
- Restore the structure and data of a table.
- Explore and query tables.
- Dump/backup tables from a database.

::page{title="Software Used in this Lab"}

In this lab, you will use <a href="https://www.mysql.com/">MySQL</a>. MySQL is a Relational Database Management System (RDBMS) designed to efficiently store, manipulate, and retrieve data.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20MySQL%20command%20line/images/mysql.png" width="100" height="100">
<p>

To complete this lab you will utilize the MySQL relational database service available as part of the IBM Skills Network Labs (SN Labs) Cloud IDE. SN Labs is a virtual lab environment used in this course.

::page{title="Database Used in this Lab"}

The Sakila database used in this lab comes from the following source: https://dev.mysql.com/doc/sakila/en/ under [New BSD license](https://opensource.org/licenses/bsd-license.php) [Copyright 2021 - Oracle Corporation].

You will use a modified version of the database for the lab, so to follow the lab instructions successfully please use the database provided with the lab, rather than the database from the original source.

The following entity relationship diagram (ERD) shows the schema of the Sakila database:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_ERD.jpg" width="500" height="592">

::page{title="Task A: Create a database"}

1. Go to **Terminal > New Terminal** to open a terminal from the side by side launched Cloud IDE.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20MySQL%20command%20line/images/A.1.png)

2. Copy the command below by clicking on the little copy button on the bottom right of the codeblock and then paste it into the terminal using **Ctrl + V** (Mac: ⌘ + V) to fetch the [sakila_mysql_dump.sql](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_mysql_dump.sql) file to the Cloud IDE.

    ```
    wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_mysql_dump.sql
    ```

    

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20MySQL%20command%20line/images/A.2.png)

3. Start the MySQL service session  using the `Start MySQL in IDE  button` directive.
	

(::openDatabase{db="MySQL" start="false"})

> If the icon doesn\'t start the MySQL database, follow the steps below.
	
- Click the Skills Network extension button on the left side of the window.
- Open the DATABASES menu and click MySQL.
-  Click Create. MySQL may take a few moments to start.

	![mysql create.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/gyIwHX5xAx6ZFXw2ZINfkg/mysql%20create.png)


5. Initiate the mysql command prompt session using the command below in the terminal:

    ```
    mysql --host=mysql --port=3306 --user=root --password
    ```
When prompted, enter the password that was displayed under the **Connection Information** section when MySQL started up.
	![connection pwd-mysql.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Tp4gGmE7jW37rrlgblZidQ/connection%20pwd-mysql.png)

> Please note, you won\'t be able to see your password when typing it in. Not to worry, this is expected!!

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/BrNUnjaHjLBjGNKBow6mlA/sql%20start%20cli.png)

	
	



6. Note down your MySQL service session password because you may need to use it later in the lab.

7. Create a new database **sakila** using the command below in the terminal and proceed to Task B:

    ```
    create database sakila;
    ```

    
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/JTZin5ivCySAIbQFI7QfGw/create%20sakila.png)


::page{title="Task B: Restore the structure and data of a table"}

1. To use the newly created empty sakila database, use the command below in the terminal:

    ```
    use sakila;
    ```

    

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20MySQL%20command%20line/images/B.1.png)

2. Restore the sakila mysql dump file (containing the sakila database table definitions and data) to the newly created empty sakila database. A dump file is a text file that contains the data from a database in the form of SQL statements. This file can be imported using the command line with the following command:

    ```
    source sakila_mysql_dump.sql;
    ```

    

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20MySQL%20command%20line/images/B.2.png)

    > **Note:** You can use the **source** command to restore the database dump file within the mysql command prompt. To restore the database dump file outside of the mysql command prompt, you can use the `mysql --host=mysql --port=3306 --user=root --password sakila < sakila_mysql_dump.sql` command after quitting the mysql command prompt session with command `\q`. <!---->

::page{title="Task C: Explore and query tables"}

1. To list all the tables names from the sakila database, use the command below in the terminal:

    ```
    SHOW FULL TABLES WHERE table_type = 'BASE TABLE';
    ```

    

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20MySQL%20command%20line/images/C.1.png)

    The **Table_type** for these tables is **BASE TABLE**. **BASE TABLE** means that it is a table as opposed to a view (**VIEW**) or an `INFORMATION_SCHEMA` view (**SYSTEM VIEW**).

2. Explore the structure of the **staff** table using the command below in the terminal:

    ```
    DESCRIBE staff;
    ```

    

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20MySQL%20command%20line/images/C.2.png)

    To understand the output, see the following table:

    | Column Name  | Definition  |
    |--------------|---|
    | Field        | Name of the column.  |
    | Type         | Data type of the column.  |
    | Null         | Displays **YES** if column can contain NULL values and **NO** if not. Notice how the primary key displays **NO**.|
    | Key          | Displays the value **PRI** if the column is a primary key, **UNI** if the column is a unique key, and **MUL** if the column is a non-unique index in which one value can appear multiple times. If there is no value displayed, then the column isn&apos;t indexed or it&apos;s indexed as a secondary column. Please note, that if more than one of these values applies to the column, the value that appears will be displayed based on the following order: **PRI**, **UNI**, and **MUL**. |
    | Default      | The default value of the column. If the column&apos;s value has specifically been set as NULL, then the value that appears will be NULL.  |
    | Extra        | Any additional information about a column. |

3. Now retrieve all the records from the **staff** table using the command below in the terminal:

    ```
    SELECT * FROM staff;
    ```

    

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20MySQL%20command%20line/images/C.3.png)

4. Quit the MySQL command prompt session using the command below in the terminal and proceed to Task D:

    ```
    \q
    ```

    

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20MySQL%20command%20line/images/C.4.png)

::page{title="Task D: Dump/backup tables from a database"}

1. Finally, dump/backup the **staff** table from the database using the command below in the terminal:

    ```
    mysqldump --host=mysql --port=3306 --user=root --password sakila staff > sakila_staff_mysql_dump.sql
    ```

    

    This command will backup the **staff** table from the **sakila** database into a file called **sakila_staff_mysql_dump.sql**.

2. Enter your MySQL service session password.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ZjRiGqB6_KOwTLtmEWZSjg/D-2.png)
	
3. To view the contents of the dump file within the terminal, use the command below:

    ```
    cat sakila_staff_mysql_dump.sql
    ```

    

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Getting%20started%20with%20MySQL%20command%20line/images/D.3.png)


## <h3>Congratulations! You have completed this lab, and you are ready for the next topic.<h3/>

**Author**: [Sandip Saha Joy](https://www.linkedin.com/in/sandipsahajoy/)

<img src="
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/6JWO8f_MMOGozgMVR3_sNw/SNIBMfooter.png"
alt="cognitiveclass.ai logo"><br/>

## Other Contributor(s)

- Kathy An
	
	
## <h3 align="center"> © IBM Corporation 2021. All rights reserved. <h3/>

<!--


## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2021-03-15 | 1.0 | Sandip Saha Joy | Created initial version |
| 2021-10-18 | 1.1 | Kathy An | Updated lab instructions |

-->
