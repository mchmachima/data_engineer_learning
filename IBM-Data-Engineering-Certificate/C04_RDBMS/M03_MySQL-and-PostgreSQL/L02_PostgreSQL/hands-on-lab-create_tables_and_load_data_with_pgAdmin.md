::page{title="  Hands-on Lab: Create Tables and Load Data in PostgreSQL using pgAdmin"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/images/IDSN-logo.png" width="300"><br>

##

**Estimated time needed:** 20 minutes

In this lab, you will learn how to create tables and load data in the PostgreSQL database service using the pgAdmin graphical user interface (GUI) tool. The pgAdmin GUI provides an alternative to the command line for interacting with a PostgreSQL database using a graphical interface. This GUI provides a number of key features for interacting with a PostgreSQL database in an easy to use format.

# Software used in this lab

In this lab, you will use <a target="_blank" href="https://www.postgresql.org/">PostgreSQL Database</a>. PostgreSQL is a Relational Database Management System (RDBMS) designed to efficiently store, manipulate, and retrieve data.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/postgresql.png" width="130" height="100">
<p>

To complete this lab you will utilize the PostgreSQL relational database service available as part of IBM Skills Network Labs (SN Labs) Cloud IDE. SN Labs is a virtual lab environment used in this course.

::page{title="Database used in this lab"}

You will use the Books database in this lab.

The following diagram shows the structure of the &#34;myauthors&#34; table from the Books database:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/Books/Books_schema.png" width="245" height="100">

::page{title="Objectives"}

After completing this lab, you will be able to use pgAdmin with PostgreSQL to:

- Create databases and tables in a PostgreSQL instance
- Load data into tables manually using the pgAdmin GUI
- Load data into tables from a text/script file

    

## Lab Structure

In this lab, you will complete several tasks in which you will learn how to create tables and load data in the PostgreSQL database service using the pgAdmin graphical user interface (GUI) tool.

::page{title="Task A: Create a database"}

First, to create a database on a PostgreSQL server instance, you\'ll first launch a PostgreSQL server instance on Cloud IDE and open the pgAdmin Graphical User Interface.

1. Click the Skills Network extension button on the left side of the window.

2. Open the **DATABASES**  menu and click **PostgreSQL**.

3. Click **Create**. PostgreSQL may take a few moments to start.

     ![postgres start pic.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/4zLhpz5CI5tmSl-DH7NRXQ/postgres%20start%20pic.png)

4. Next, open the pgAdmin Graphical User Interface by clicking **pgAdmin** in the Cloud IDE interface.

     ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ZnZiQafAH3ZwT4V6Wz7fYw/pgadmin%20.png)

5. Once the pgAdmin GUI opens, click **Servers** tab on the left side of the page. You will be prompted to enter a password.

    ![pgAdmin_2](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/pgAdmin_2.png)

6. To retrieve your password, click **PostgreSQL** tab near the top of the interface and select **Connection Information** tab.


     ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/priMDdmsl6kx9EFaQ2kHGA/pgadmin-pass1.png)
	
7. Scroll down and click the Copy icon on the left of your password to copy the session password onto your clipboard.
	
	 ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/EfhCH4BlDAZOTsvjRhHw3Q/pgadmin-pass2.png)

8. Navigate back to the **pgAdmin** tab and paste in your password, then click **OK**.

9. You will then be able to access the pgAdmin GUI tool.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/1.5.png)

10. In the tree-view, expand **Servers** > **postgres** > **Databases**. If prompted, enter your PostgreSQL service session password. Right-click on **Databases** and go to **Create > Database**. In the **Database** box, type **Books** as the name for your new database, and then click **Save**. Proceed to Task B.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/2.5.1.png)

    <p>

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/2.5.2.png)

::page{title="Task B: Create tables"}

Now that you have your PostgreSQL service active and have created the **Books** database using pgAdmin, let\'s create a few tables to populate the database and store the data that you wish to eventually upload into it.

1. In the tree-view, expand **Books** > **Schemas** > **public**. Right-click on **Tables** and go to **Create > Table**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/2.6.png)

2. On the **General** tab, in the **Name** box, type **myauthors** as name of the table. Don\'t click **Save**, proceed to the next step. 
    
    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/2.7.png)

3. Switch to the tab **Columns** and click the **Add new row** button four times to add 4 column placeholders. Don\'t click **Save**, proceed to the next step. 

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/2.8.png)

4. Enter the **myauthors** table definition structure information as shown in the image below in the highlighted boxes. Then click **Save**. Proceed to Task C.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/2.9.png)

::page{title="Task C: Load data into tables manually using the pgAdmin GUI"}

You now have a database and have created tables within it. With the pgAdmin GUI, you can insert values into the tables manually. This is useful if you have a few new entries you wish to add to the database. Let\'s see how to do it.

1. In the tree-view, expand **Tables**. Right-click **myauthors** and go to **View/Edit Data > All Rows**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/2.10.png)

2. You will insert 2 rows of data into the **myauthors** table. In the lower **Data Output** pane, enter **myauthors** table data information for 2 rows as shown in the highlighted boxes in the image below. Then click the **Save Data Changes** icon. Proceed to Task D.

    ![add row image.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/SQjZFewJYyqqJh14M5zkHw/add%20row%20image.png)

3. Enter the values into the table as shown below:
		![Values to add.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/yHmh38iJjo5kIlEUn9c4RA/Values%20to%20add.png)

		![add values.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/9sJPLQDPOj9qUvaqBKnkmQ/add%20values.png)

4. Save the values.
		![save the values.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/v9HZI5JpCJp7tpIEcvgsBg/save%20the%20values.png)

::page{title="Task D: Load data into tables using a text/script file"}

In the previous task, you entered some data entries into a table manually with pgAdmin. While this method can be useful for small additions, if you wish to upload large amounts of data at once, the process becomes tedious. An alternative is to load data into tables from a text or script file containing the data you wish to enter. Let\'s take a look at how to do this.

1. You will import the remainder of the **myauthors** table data from a csv text file. Download the csv file below to your local computer:
    
    - [myauthors.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/Books/myauthors.csv)

2. In the tree-view, right-click on **myauthors** and go to **Import/Export**.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/2.13.png)

3. Follow the instructions below to import:

    1. Make sure **Import/Export** is set to **Import**, 
 	2. **Format** = **csv**. 
	3. Then click **Select file** icon by the **Filename** box.

        ![import image.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/gjaRLvySOSvLf25cOmh-CQ/import%20image.png)

    4. Steps to **Upload File**.
     - Step 1: Initially make sure the folder details empty and select the var option from the list as shown in the screenshot below. Select var folder
		![var select.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/xp-4WkbEbRZLzhZHcnO5tA/var%20select.png)
	 - Step 2: Select lib folder.
		
		![lib select.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/C6sBsBM2GS-2zo5KNyDGNQ/lib%20select.png)
	 -   Step 3: Select pgadmin folder. Here you could notice the folders are locked except the pgadmin folder. 
		![pgadmin  select.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/q7fnWDkF9UcAzaFeK4w3qw/pgadmin%20%20select.png)
		
	- Step 4: Now select upload as mentioned here.
		![upload file.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/2BZroCBPXKC8FUX3aW8JWA/upload%20file.png)
		
	- Step 5: Now Drag and drop the file from your downloads on your local machine.
		![drag and drop.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/2ritAar-9gm_RyhQQcuN-Q/drag%20and%20drop.png)
		
	- Step 6: Finally, the upload is successful. When the upload is complete, close the drop files area by clicking **X**.
		
		![upload success.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/hXbmjSwA_VEkvRvhjv520Q/upload%20success.png)

    

    

    - Select the uploaded **myauthors.csv** file from the list and click **Select**.

        ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/2.14.5.png)

    - Ensure the file has selected.
		![final import okay.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/wrSbw7Tj_2WcwYEuHMxkZw/final%20import%20okay.png)
    - Under **Options** enable **Header** and Click OK and notification of import success will appear.

        ![import click okay.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/6sy-0AITcIicXKhWqXMHHg/import%20click%20okay.png)
		

        <p>

        ![final success message.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/B60Zy3nh43HRhU74GkjcmQ/final%20success%20message.png)

4. Repeat Task C Step 1 to check that the newly imported data rows appear along with your previously inserted 2 rows.

    ![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/labs/Lab%20-%20Create%20Tables%20and%20Load%20Data%20in%20PostgreSQL%20using%20pgAdmin/images/2.15.png)

    As you can see, the data contained in the **csv** file was successfully uploaded into the table and you did not have to manually input hundreds of entries.

::page{title="Conclusion"}

Congratulations! You have completed this lab, and you have learned how to create databases and tables in a PostgreSQL instance, load data into tables manually using the pgAdmin GUI, and load data into tables from a text/script file. 
<br>

## Author

- [Sandip Saha Joy](https://www.linkedin.com/in/sandipsahajoy/)

## Other Contributors

- [David Pasternak](https://www.linkedin.com/in/david-pasternak-6b84a2208/)

<img src="
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/6JWO8f_MMOGozgMVR3_sNw/SNIBMfooter.png"
alt="cognitiveclass.ai logo"><br/>

## <h3 align="center"> © IBM Corporation. All rights reserved. <h3/>

<!---
## Changelog
 © IBM Corporation 2020.
| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2021-03-15 | 1.0 | Sandip Saha Joy | Created initial version |
| 2021-10-18 | 1.1 | David Pasternak | Updated lab instructions |
| 2024-01-31 | 1.2 | Anita Narain | ID review |
| 2024-01-31 | 1.3 | Mercedes Schneider | QA review |
| 2024-08-30 | 1.4 |Anita Verma | Updated lab instructions and screenshots |

-->



