::page{title="Hands-on Lab: Database Design using ERDs"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/images/IDSN-logo.png" width="300"><br>

##


**Estimated time needed:** 45 minutes

In this lab, you will learn how to design a database by creating an entity relationship diagram (ERD) in the PostgreSQL database service using the pgAdmin graphical user interface (GUI) tool. First, you will create an ERD of a database. Next, you will generate and execute an SQL script to create the database schema from its ERD. Finally, you will load the created database schema with data.

::page{title="Software used in this lab"}

In this lab, you will use <a href="https://www.postgresql.org/" target=_blank>PostgreSQL Database</a>. PostgreSQL is a Relational Database Management System (RDBMS) designed to efficiently store, manipulate, and retrieve data.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/postgresql.png" width="130" height="100">
<p>

To complete this lab, you will utilize the PostgreSQL relational database service available as part of IBM Skills Network Labs (SN Labs) Cloud IDE. SN Labs is a virtual lab environment used in this course.

::page{title="Database used in this lab"}

The HR database used in this lab comes from the following source: [HR Sample Database](https://docs.oracle.com/en/database/oracle/oracle-database/19/comsc/introduction-to-sample-schemas.html#GUID-4DE9844F-0B28-4713-9AFC-CCD8D6249D76) [Copyright 2021 - Oracle Corporation].

You will use a modified version of the database for the lab. To follow the lab instructions successfully, please use the database provided with the lab, rather than the database from the original source.

The following ERD shows the tables of the HR database:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/HR_Database/HR_Proper/HR_tables.png" width="700" height="700">

::page{title="Objectives"}


After completing this lab, you will be able to use pgAdmin with PostgreSQL to:

- Create an ERD of a database.
- Generate and execute an SQL script from an ERD to create a schema.
- Load the database schema with data.

This lab is divided into two exercises, _Example Exercise_ and _Practice Exercise_.

::page{title="Example Exercise"}


In this example exercise, you will first create a partial ERD of the HR database. Next, you will generate and execute an SQL script to create the partial schema of the HR database from its ERD. Finally, you will load the created database schema with data by using the Restore feature.

::page{title="Task A: Create an Entity Relationship Diagram (ERD) of a database"}


In this task of the Example Exercise, you will create a partial ERD of the HR database.


To get started with this lab, launch PostgreSQL using the Cloud IDE. You can do this by following these steps:

1. Click the Skills Network extension button on the left side of the window.

2. Open the **DATABASES**  menu and click **PostgreSQL**.

3. Click **Create**. PostgreSQL may take a few moments to start.

    ![postgres start pic.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/4zLhpz5CI5tmSl-DH7NRXQ/postgres%20start%20pic.png)
4. Note down your PostgreSQL service session password because you may need to use it later in the lab.

5. Click the pgAdmin button in the same window where you started PostgresSQL.


6. You will see the pgAdmin GUI tool.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.4.png)

7. In the tree-view, expand **Servers** > **postgres** > **Databases**. Enter your PostgreSQL service session password if prompted during the process. Right-click on **Databases** and go to **Create > Database**. Type **HR** as the name of the database and click **Save**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.5.1.png)

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.5.2.png)

8. In the tree-view, expand **HR**. Right-click on **HR** and select **Generate ERD (Beta)**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.6.png)

9. Click **Add table**. On the **General** tab, in the **Name** box, type **employees** as the name of the table. Don&#39;t click **OK**, proceed to the next step.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.7.1.png)

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.7.2.png)

10. Switch to the **Columns** tab and click **Add new row** to add the necessary column placeholders. Now enter the **employees** table definition information as shown in the image below to create its entity diagram. Then click **OK**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.8.1.png)

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.8.2.png)

11. Similarly, create entity diagrams for the other three tables following steps 9 and 10:

    <details>
    <summary>[Click here] Create an entity diagram for the jobs table</summary>

    > Click **Add table** icon. On the **General** tab, in the **Name** box, type **jobs** as the name of the table. Don&#39;t click **OK**. Switch to tab **Columns** and click **Add new row** to add the necessary column placeholders. Now enter the **jobs** table definition information as shown in the image below to create its entity diagram. Then click **OK**.

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.9.A.1.png)

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.9.A.2.png)

    </details>

    <details>
    <summary>[Click here] Create an entity diagram for the departments table</summary>

    > Click **Add table** icon. On the **General** tab, in the **Name** box, type **departments** as the name of the table. Don&#39;t click **OK**. Switch to tab **Columns** and click **Add new row** to add the necessary column placeholders. Now enter the **departments** table definition information as shown in the image below to create its entity diagram. Then click **OK**.

    <p>
    
    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.9.B.1.png)

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.9.B.2.png)

    </details>

    <details>
    <summary>[Click here] Create an entity diagram for the locations table</summary>

    > Click **Add table** icon. On the **General** tab, in the **Name** box, type **locations** as the name of the table. Don&#39;t click **OK**. Switch to tab **Columns** and click **Add new row** to add the necessary column placeholders. Now enter the **locations** table definition information as shown in the image below to create its entity diagram. Then click **OK**.

    <p>
    
    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.9.C.1.png)

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.9.C.2.png)

    </details>

10. After creating all four entity diagrams, the entities of the ERD are complete.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.10.png)

11. Next, you will create relationships between the entities by adding foreign keys to the tables. Select the entity diagram **employees** and click **One-to-Many link**. Now enter the definition information for a foreign key on the **employees** table as shown in the image below to create the relationship. Then click **OK**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.11.1.png)

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.11.2.png)

<br>

12. Similarly, create the other relationships between the tables following the instructions in step 13:
    
    <details>
    <summary>[Click here] Create a relationship between employees and jobs</summary>

    > Select the entity diagram **employees** and click **One-to-Many link**. Now enter the definition information for a foreign key on the **employees** table as shown in the image below to create the relationship. Then click **OK**.

    <p>
    
    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.12.1.png)

    </details>

    <details>
    <summary>[Click here] Create a relationship between departments and locations</summary>

    > Select the entity diagram **departments** and click **One-to-Many link**. Now enter the definition information for a foreign key on the **departments** table as shown in the image below to create the relationship. Then click **OK**.

    <p>
    
    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.12.2.png)

    </details>

    <details>
    <summary>[Click here] Create a relationship between departments and employees</summary>

    > Select the entity diagram **departments** and click **One-to-Many link**. Now enter the definition information for a foreign key on the **departments** table as shown in the image below to create the relationship. Then click **OK**.

    <p>
    
    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.12.3.png)

    </details>

13. After creating all four relationships, you have completed the ERD for this exercise. Proceed to Task B.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.A.13.png)

::page{title="Task B: Generate and execute SQL script from ERD to create the schema"}


In this task of the Example Exercise, you will generate and execute a SQL script from the ERD you created in Task A of the Example Exercise.

1. In the **Generate ERD (Beta)** window, click **Generate SQL**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.B.1.png)

2. A new Query Editor window will open containing a SQL script generated from the ERD. Click **Execute/Refresh** to run the script. Proceed to Task C.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.B.2.png)

::page{title="Task C: Load the database schema with data"}


In this task of the Example Exercise, you will load the database schema you created in Task B of the Example Exercise with data using the pgAdmin Restore feature.

1. Download the **HR_pgsql_dump_data_for_example-exercise.tar** PostgreSQL dump file (containing the partial HR database data) using the link below to your local computer.

    - [HR_pgsql_dump_data_for_example-exercise.tar](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/HR_Database/HR_Proper/HR_pgsql_dump_data_for_example-exercise.tar)

2. Follow the instructions below to import/restore the data: 

    - In the tree-view, expand **HR**. Right-click **HR** and click **Restore**.

        ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.C.2.png)

    - On the **General** tab, click **Select file** by the Filename box.

        ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.C.3.png)
	- Initially make sure the folder details empty and select the var option from the list as shown in the screenshot below. Select var folder.
	 
		![var select.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ttVzrPKvanT-8BivkUchmg/var%20select.png)
		
	- Select lib folder.
		
		![lib select.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/lTesko6mei9vQPWhTqQFwg/lib%20select.png)

	- Select pgadmin folder. Here you could notice the folders are locked except the pgadmin folder. 
		![pgadmin  select.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/cIKHV4OFhUrMokVVsO8IVA/pgadmin%20%20select.png)
	- Click **Upload File**. Now select upload as mentioned here.
		![upload file.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/2Vp7cFFnGNKj4lLqmARL9Q/upload%20file.png)
	

    - Double-click on the drop files area and load the **HR_pgsql_dump_data_for_example-exercise.tar** you downloaded earlier on your local computer.
		
	>	Note: Ensure that you upload the files to this path: /var/lib/pgadmin/
		
		

      ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.C.5.png)

    - When the upload is complete, close the drop files area by clicking **X**.

        ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.C.6.png)

    - Ensure **Format** is set to **All Files**, select the uploaded **HR_pgsql_dump_data_for_example-exercise.tar** file from the list, and then click **Select**.

        ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.C.7.png)

    - Now switch to the **Restore options** tab.

        ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.C.8.png)

    - Under **Disable**, set the **Trigger** option to **Yes**. Then click **Restore**.

        ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/1.C.9.png)

<br>

::page{title="Practice Exercise"}


In this practice exercise, first you will finish creating a partially complete ERD for the HR database. Next, you will generate and execute an SQL script to build the complete schema of the HR database from its ERD. Finally, you will load the complete database schema with data by using the Restore feature.

1. Download the **HR_pgsql_ERD_for_practice-exercise.pgerd** ERD file (containing a partial HR database ERD based on the one that you created in Task A of the Example Exercise) below to your local computer.

    - [HR_pgsql_ERD_for_practice-exercise.pgerd](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/HR_Database/HR_Proper/HR_pgsql_ERD_for_practice-exercise.pgerd)

2. In pgAdmin, create a new database named **HR_Complete**.

3. Open the ERD Tool and use **Load from file** to load the **HR_pgsql_ERD_for_practice-exercise.pgerd** file. 

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/2.3.png)

    <p>

    > **Tip:** Follow Example Exercise Task C for how to load any file in pgAdmin.

4. You will see the previous four entity diagrams along with relationships that you created in the Example Exercise. You will also see three new entity diagrams for the **job_history**, **regions**, and **countries** tables and one new relationship within the entity diagram of the **employees** table between _manager_id_ as local column and _employee_id_ as referenced column.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/2.4.png)

5. Create the remaining relationships between the tables:
    
    <details>
    <summary>[Click here] Create a relationship between countries and regions</summary>

    > Select the entity diagram **countries** and click **One-to-Many link**. Now enter the definition information for a foreign key on the **countries** table as shown in the image below to create the relationship. Then click **OK**.

    <p>
    
    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/2.5.1.png)

    </details>

    <details>
    <summary>[Click here] Create a relationship between job_history and departments</summary>

    > Select the entity diagram **job_history** and click the **One-to-Many link** button. Now enter the definition information for a foreign key on the **job_history** table as shown in the image below to create the relationship. Then click **OK**.

    <p>
    
    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/2.5.2.png)

    </details>

    <details>
    <summary>[Click here] Create a relationship between job_history and employees</summary>

    > Select the entity diagram **job_history** and click **One-to-Many link**. Now enter the definition information for a foreign key on the **job_history** table as shown in the image below to create the relationship. Then click **OK**.

    <p>
    
    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/2.5.3.png)

    </details>

    <details>
    <summary>[Click here] Create a relationship between job_history and jobs</summary>

    > Select the entity diagram **job_history** and click **One-to-Many link**. Now enter the definition information for a foreign key on the **job_history** table as shown in the image below to create the relationship. Then click **OK**.

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/2.5.4.png)

    </details>

    <details>
    <summary>[Click here] Create a relationship between locations and countries</summary>

    > Select the entity diagram **locations** and click **One-to-Many link**. Now enter the definition information for a foreign key on the **locations** table as shown in the image below to create the relationship. Then click **OK**.

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/2.5.5.png)

    </details>

    <p>

    > **Tip:** Follow Example Exercise Task A for how to create relationships between the entities by adding foreign keys to the tables.

6. After creating the remaining relationships, the complete ERD of the HR database will look like the following image:

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Database%20Design%20using%20ERDs%20/images/2.6.png)

7. Generate and execute an SQL script from the ERD to create the schema of the **HR_Complete** database.

    > **Tip:** Follow Example Exercise Task B.

8. Download the **HR_pgsql_dump_data.tar** PostgreSQL dump file (containing the complete HR database data) below to your local computer. Use the dump file to restore/import the data to the **HR_Complete** database.

    - [HR_pgsql_dump_data.tar](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/HR_Database/HR_Proper/HR_pgsql_dump_data.tar)

    <p>

    > **Tip:** Follow Example Exercise Task C.

<br>

::page{title="Conclusion"}

Congratulations! You have completed this lab, and you have learned how to create an ERD of a database, generate and execute an SQL script from an ERD to create a schema, and load the database schema with data. 

<br>

## Author(s)

- [Sandip Saha Joy](https://www.linkedin.com/in/sandipsahajoy/)

## <h3 align="center"> © IBM Corporation. All rights reserved. <h3/>


<!--

## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2021-03-31 | 1.0 | Sandip Saha Joy | Created initial version |
| 2024-01-29 | 1.2 | Anita Narain | ID review |
| 2024-01-30 | 1.3 | Mercedes Schneider | QA pass with edits |
| 2024-01-30 | 1.4 | Sydney Marsing | UXQA, repaired ToC |

-->