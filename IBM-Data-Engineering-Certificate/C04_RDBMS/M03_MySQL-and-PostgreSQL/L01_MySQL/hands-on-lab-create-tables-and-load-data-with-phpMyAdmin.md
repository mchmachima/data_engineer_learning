::page{title="Hands-on Lab: Create Tables and Load Data in MySQL using phpMyAdmin"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/images/IBM_logo.png" width="300">

##

**Estimated time needed:** 20 minutes

In this lab, you will learn how to create tables and load data in the MySQL database service using the phpMyAdmin graphical user interface (GUI) tool.

## Objectives

After completing this lab, you will be able to use phpMyAdmin with MySQL to:

- Create a database.
- Create tables.
- Load data into tables manually using the phpMyAdmin GUI.
- Load data into tables using a text/script file.

## Software Used in this Lab

In this lab, you will use <a target="_blank" href="https://www.mysql.com/">MySQL</a>. MySQL is a Relational Database Management System (RDBMS) designed to efficiently store, manipulate, and retrieve data.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/mysql.png" width="100" height="100">
<p>

To complete this lab you will utilize MySQL relational database service available as part of IBM Skills Network Labs (SN Labs) Cloud IDE. SN Labs is a virtual lab environment used in this course.

## Database Used in this Lab

**Books** database has been used in this lab.

The following diagram shows the structure of the **myauthors** table from the Books database:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/Books/Books_schema.png" width="245" height="100"><br>

In the table, **author_id** is an integer, **first_name** is a string that stores a maximum of 100 characters, **middle_name** is a string that stores a maximum of 50 characters, and **last_name** is a string that stores a maximum of 100 characters.

::page{title="Task A: Create a database"}

Start the MySQL service session  using the `Start MySQL in IDE  button` directive.
	

(::openDatabase{db="MySQL" start="false"}) 
	
> If the icon doesn\'t start the MySQL database, follow the steps below.


	

1. Click the Skills Network extension button on the left side of the window.
2. Open the DATABASES menu and click MySQL.
3. Click Create. MySQL may take a few moments to start.

	![mysql create.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/gyIwHX5xAx6ZFXw2ZINfkg/mysql%20create.png)

4. Open the phpMyAdmin tool in a new tab in your browser.

	![open new tab mysql.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/XqcHq_3iddJrLTJG67RRSQ/open%20new%20tab%20mysql.png)


4. You will see the phpMyAdmin GUI tool.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.4.png)

5. In the tree-view, click **New** to create a new empty database. Then enter **Books** as the name of the database and click **Create**.

    The encoding will be left as **utf8mb4_0900_ai_ci**. UTF-8 is the most commonly used character encoding for content or data.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.5.png)

::page{title="Task B: Create tables"}

1. In the Create table interface for the empty database **Books**, enter **myauthors** as the table name and **4** for the Number of columns. This is the first step to creating the table **myauthors** that was shown earlier in this lab.

    Then click **Go**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.6.png)

2. Enter the table definition for the **myauthors** table as shown in the image below with highlighted boxes. Then click **Save**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.7.png)

3. The Table structure for the **myauthors** table will appear.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.8.png)

::page{title="Task C: Load data into tables manually using the phpMyAdmin GUI"}

1. Sometimes, you may want to load a few data rows of data, but you may not have a SQL script on hand to do that. In this case, you can manually load the data into phpMyAdmin. Since this is a manual process, it is better for inserting a small amount of data rather than a large amount.

    To load data manually, go to the **Insert** tab for the **myauthors** table. Enter data for 2 rows of the **myauthors** table as shown in the image below with highlighted boxes. Then click **Go** at the bottom.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.9.png)

2. Notification of the successful insertion of 2 rows to the **myauthors** table will appear.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.10.png)

3. Go to the **Browse** tab for the **myauthors** table to check the newly inserted rows.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.11.png)

::page{title="Task D: Load data into tables using a text/script file"}

1. Now you will use a SQL script to import the remainder of the **myauthors** table data. A SQL script file contains commands and statements that perform operations on your database, and can be useful when importing a large amount of data.

    Download the SQL script below to your local computer:

    - [mysql_table-myauthors_insert-data.sql](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/Books/mysql_table-myauthors_insert-data.sql)

2. Go to **Import** tab for the **myauthors** table. Click **Choose File** and load the **mysql_table-myauthors_insert-data.sql** file from your local computer storage. The rest of the settings can be left as they are because you are importing a SQL script that is encoded with UTF-8.

    Then click **Go**. Notification of import success will appear.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.13.1.png)

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.13.2.png)

3. Go to the **Browse** tab for the **myauthors** table again to check the newly inserted rows appear along with previously inserted 2 rows.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20MySQL%20using%20phpMyAdmin/images/2.14.png)

## <h3> Congratulations! You have completed this lab, and you are ready for the next topic. <h3/>

<br>

**Author**: [Sandip Saha Joy](https://www.linkedin.com/in/sandipsahajoy/)

<img src="
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/6JWO8f_MMOGozgMVR3_sNw/SNIBMfooter.png"
alt="cognitiveclass.ai logo"><br/>

## Other Contributor(s)

- Kathy An
	
	
<h3> © IBM Corporation 2021. All rights reserved. <h3/>

<!--


## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2021-03-15 | 1.0 | Sandip Saha Joy | Created initial version |
| 2021-10-18 | 1.1 | Kathy An | Updated lab instructions |

-->
