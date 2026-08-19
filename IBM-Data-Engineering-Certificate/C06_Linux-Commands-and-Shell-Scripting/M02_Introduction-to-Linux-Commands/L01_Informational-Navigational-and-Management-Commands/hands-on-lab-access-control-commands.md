::page{title="Hands-on Lab: Access Control Commands"}


<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/images/IDSN-logo.png" width="300" alt="cognitiveclass.ai logo">


Estimated time needed: **10** minutes

## Learning Objectives

After completing this lab, you will be able to:

- Understand the various access permissions a file or directory can have
- View the permissions for all files and directories within a directory
- Modify permissions for a file by user
- Describe the effect of changing permissions on a directory

::page{title="About Skills Network Cloud IDE"}

Skills Network Cloud IDE (based on Theia and Docker) provides an environment for hands on labs for course and project related labs. Theia is an open source IDE (Integrated Development Environment), that can be run on desktop or on the cloud. To complete this lab, you will be using the Cloud IDE based on Theia.

## Important notice about this lab environment

Please be aware that sessions for this lab environment are not persisted. Thus, every time you connect to this lab, a new environment is created for you and any data or files you may have saved in a previous session will be lost. To avoid losing your data, plan to complete these labs in a single session.

::page{title="Exercise 1 - Viewing and modifying file access permissions"}

### 1.1 View file access permissions

#### Required files:

Run the following code to download the required files for this exercise:

```
cd /home/project
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/usdoi.txt
```

Each file and each directory in your Linux system has permissions set for three permission categories: the \'user\', the \'group\', and \'all users\' (or \'other\').

The following permissions are set for each file and directory:

| Permission | Symbol |
|----------- | ------ |
|read        | `r`    |
|write       | `w`    |
|execute     | `x`    | 

To see the permissions currently set for a file, run the `ls` command  with the `-l` option. 

For example, to see the permissions for the file named `usdoi.txt` in your current directory, enter the following:

```
ls -l usdoi.txt
```

A sample output looks like the following:

`-rw-r--r-- 1 theia theia 8121 May 31 16:45 usdoi.txt`

The permissions set here are `rw-r--r--`. The `-` preceeding these permissions indicates that `usdoi.txt` is a file. If it were a directory, you would see a `d` instead of the `-`.

The first three entries correspond to the current user, the next three correspond to the group, and the last three are for all others. You can see the user has read and write permissions, while the user group only has read permission, and all other users have only read permission. No users have execute permission, as indicated by the `-` instead of an `x` in the third position for each user category.

### 1.2 Change file access permissions

**`chmod`**

The `chmod` or *change mode* command lets you change the permissions set for a file.

Specify which permissions to change with a combination of the following characters: <br>

| Option            | Description                                                |
| ----------------- | ---------------------------------------------------------- |
| `r`, `w`, `x`  | **Permissions**: read, write, and execute       |
| `u`,`g`, `o `  | **User categories**: user, group, and all others  |
| `+`, `-`          | **Operations**: grant and revoke          |


The following command *revokes* read permissions for *all users* (user, group, and other) on the file `usdoi.txt`:

```
chmod -r usdoi.txt               
```

You can verify the changed permissions by entering:

```
ls -l usdoi.txt
```

To grant read access to *all users* on `usdoi.txt`, enter:<br>

```
chmod +r usdoi.txt                
```

Verify the changed permissions again with the following:

```
ls -l usdoi.txt
```

Now to remove the read permission only for \'other\' category, enter the following:

```
chmod o-r usdoi.txt
```

Verify the changed permissions as follows:

```
ls -l usdoi.txt
```

::page{title="Exercise 2 - Understanding directory access permissions"}

### 2.1 View default directory access permissions

Recall the following table, which illustrates the meanings of each permission for directories with examples of allowable operations for a given directory.

| Directory Permission  | Permissible action(s)                          |
| --------------------- | ---------------------------------------------- |
| `r`                   | list directory contents using `ls` command     |
| `w`                   | add/remove files or directories from directory |
| `x`                   | enter directory using `cd` command             |

For this exercise, first move to your `project` directory and create a new directory called `test`:

```
cd /home/project
mkdir test
```

Check the default permissions that the system sets for your new `test` directory:

```
ls -l
```

As you can see from the resulting output:

```
total 12
drwxr-sr-x 2 theia users 4096 May 15 14:06 test
-rw-r----- 1 theia users 8121 Sep 28  2022 usdoi.txt
```

You, \"theia\", as the owner of `test`, have read, write, and execute permissions set by default. But all others only have read and execute permissions set and cannot write to your `test` directory. This means users outside your group can\'t add or remove files from `test`. They can, however, explore your directory to see what files and directories exist there.

> **Note:** You might be wondering what that `s` permission is in the execute slot for your group. The `s` stands for \"*special* permission\". It means that any new files created within the directory will have their group ownership set to be the same as the directory owner. We won\'t go into this level of detail in this course, but you can learn more about advanced Linux permissions here: [Linux permissions: SUID, SGID, and sticky bit](https://www.redhat.com/sysadmin/suid-sgid-sticky-bit#:~:text=Commonly%20noted%20as%20SUID%2C%20the,use%20an%20uppercase%20S%20here.).

Go ahead and verify for yourself that you have permission to run the following commands. Change the directory to your `test` directory, create a new directory within it, then return to your parent directory:

```
cd test
mkdir test2
cd ../
```

### 2.2 Remove user execute permissions on your `test` directory

Remove your user execute permissions on `test` using the following command:

```
chmod u-x test
```

Now, what happens when you try to change directories to `test`?

```
cd test
```

You get an error message!

`bash: cd: test: Permission denied`

As you just removed execute permissions for yourself on your `test` directory, you can no longer make it your present working directory. However, you can still \"read\" it with the `ls` command:

```
ls -l
```

Even though you have \"write\" permissions set, you can\'t actually create a new directory within `test`, because removing execute permissions overrides write permissions. For example, entering,

```
mkdir test/test3
```

throws an error:

`mkdir: cannot create directory ‘test/test’: Permission denied`

This time, try restoring execute permissions on `test` and denying write permissions. Then verify your changes:

```
chmod u+x test
chmod u-w test
ls -l
```

Now you can go into `test`, but you still can\'t write to it! Entering

```
cd test
mkdir test_again
```

throws the error:

`mkdir: cannot create directory ‘test_again’: Permission denied`

::page{title="Practice exercises"}

#####  1. List the permissions set for the file `usdoi.txt` that you downloaded to your project directory at the beginning of the lab.

<details>
<summary>Click here for Hint</summary>

> Use the `ls` command with the correct option and argument.

</details>

<details>
<summary>Click here for Solution</summary>

```
cd /home/project
ls -l usdoi.txt
```

</details>

#####  2. Revoke the write permission on `usdoi.txt` for the user, and verify your result.

<details>
<summary>Click here for Hint</summary>

> Use the `chmod` and `ls` commands with the right options.

</details>

<details>
<summary>Click here for Solution</summary>

```
chmod u-w  usdoi.txt
ls -l usdoi.txt
```

You should only see read permissions set for all three user categories.

</details>

#####  3. What happens if you try to delete `usdoi.txt` after revoking write permissions for the user?

<details>
<summary>Click here for Hint</summary>

> Use the `rm` command to find out.

</details>

<details>
<summary>Click here for Solution</summary>

If you run the following command:

```
rm usdoi.txt 
```

You should see the following prompt:

```
rm: remove write-protected regular file \'usdoi.txt\'?
```

Entering `y` will override the write protection and delete the file, which you can verify as follows:

```
ls usdoi.txt
```

</details>

#####  4. Create a new directory called `tmp_dir` in your home directory.

<details>
<summary>Click here for Hint</summary>

> Use the `mkdir` command.

</details>

<details>
<summary>Click here for Solution</summary>

```
mkdir tmp_dir
```

</details>

#####  5. View the permissions of the newly created directory, `tmp_dir`.

<details>
<summary>Click here for Hint</summary>

> Use the `-d` and `-l` options of the `ls` command.

</details>

<details>
<summary>Click here for Solution</summary>

```
ls -ld tmp_dir
```

</details>

#####  6. Revoke the user write permission for `tmp_dir`.

<details>
<summary>Click here for Hint</summary>

> Use the `u` and `w` options of the `chmod` command.

</details>

<details>
<summary>Click here for Solution</summary>

```
chmod u-w tmp_dir
```

</details>

#####  7. Check whether you can create a subdirectory of `tmp_dir` called `sub_dir`.

<details>
<summary>Click here for Hint</summary>

> Use the `cd` and `mkdir` commands or just the `mkdir` command.

</details>

<details>
<summary>Click here for Solution 1</summary>

```
cd tmp_dir
mkdir sub_dir
```

You should be able to enter the directory with the `cd` command, but you should see a \"permission denied\" error after entering the mkdir command.

</details>

<details>
<summary>Click here for Solution 2</summary>

```
mkdir tmp_dir/sub_dir
```

Again, you should see a \"permission denied\" error for the mkdir command.

</details>

::page{title="Summary"}

In this lab, you learned that:
- Files and directories can have read, write, and execute permissions for the user, group, and others
- You can view the permissions for all files and directories within a directory by using `ls -l`
- You can modify permissions for a file by using `chmod`
- Changing permissions on a directory will change who can do what to the directory and its files


## Authors

Ramesh Sannareddy  
Sam Prokopchuk  
Jeff Grossman  

### Other Contributors

Rav Ahuja
<!--
## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2023-04-17        | 3.3     | Steve Hord        | QA pass with edits                  |
| 2023-04-13        | 3.2     | Nick Yi		      | ID Review					       |
| 2023-01-12        | 3.1     | Jeff Grossman     | Expand content, add exercises      |
| 2023-01-11        | 3.0     | Jeff Grossman     | Split lab and expand content       |
| 2021-12-02        | 2.1     | Jeff Grossman     | Review and Update lab              |
| 2021-11-29        | 2.0     | Sam Prokopchuk    | Update lab contents and split      |
| 2021-05-30        | 1.0     | Ramesh Sannareddy | Created initial version of the lab |

 Copyright (c) 2021-23 IBM Corporation. All rights reserved.-->
 
 <h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>

