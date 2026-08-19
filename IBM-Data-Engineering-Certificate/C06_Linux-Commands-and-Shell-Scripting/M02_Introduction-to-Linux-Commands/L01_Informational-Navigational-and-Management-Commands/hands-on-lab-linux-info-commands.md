::page{title="Hands-on Lab: Informational Commands"}


<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/images/IDSN-logo.png" width="300" alt="cognitiveclass.ai logo">


Estimated time needed: **30** minutes

## Learning Objectives

After completing this lab, you will be able to use commands to display:

- System and user information
- User and group identity info
- Information about running processes and system resource usage 
- Custom messages
- The current date and time
- The reference manual for a command

::page{title="About Skills Network Cloud IDE"}

Skills Network Cloud IDE (based on Theia and Docker) provides an environment for hands on labs for course and project related labs. Theia is an open source IDE (Integrated Development Environment), that can be run on desktop or on the cloud. To complete this lab, you will be using the Cloud IDE based on Theia.

## Important notice about this lab environment

Please be aware that sessions for this lab environment are not persisted. Thus, every time you connect to this lab, a new environment is created for you and any data or files you may have saved in a previous session will be lost. To avoid losing your data, plan to complete these labs in a single session.

::page{title="Exercise 1 - Informational Commands"}

In this exercise, you will familiarize yourself with useful commands for providing system and user information.

### 1.1.  Display the name of the current user

**`whoami`**

Enter the `whoami` command to return your current username.

```
whoami
```

It will display the user name as `theia` because you are logged into this lab as `theia`.

You can get a list of currently logged in users using the command `who`, but this command doesn\'t work in the Theia environment yet.

### 1.2. Get basic information about the operating system

**`uname`**

By default the command prints the kernel name. The `u` in `uname` refers to \"unix-like 0S\".

```
uname
```

If you enter the command `uname`, you will see `Linux` printed in the output.

Using the `-a` option prints all the system information.

```
uname -a
```

You will see system information listed in the following order: 

- Kernel name
- Network node hostname
- Kernel release date
- Kernel version
- Machine hardware name
- Hardware platform
- Operating system

### 1.3. Obtain the user and group identity information

**`id`**

This command displays the user id and group id information of the current user.

```
id
```

It will display the `uid` (user id) and `gid` (group id) for the user `theia`.

### 1.4 Get available disk space

**`df`**

The `df` command is used to display available disk space.

```
df
```

This command will display available disk space in 512-byte blocks. To get available disk space in a \"human-readable\" format, enter:

```
df -h
```

This will return the available disk space in units like gigabytes and terabytes.

### 1.5. View currently running processes

**`ps`**

The `ps` command lists each process that is currently running and its `PID` (process id).

```
ps
```

However, the output only contains the processes that are owned by you.

By using the `-e` option, you can display all of the processes running on the system. The includes processes owned by other users.

```
ps -e
```

### 1.6. Get information on the running processes and system resources

**`top`**

The `top` or \"table of processes\" command provides a dynamic, real-time view of your system.

```
top
```

The `top` command displays a table of detailed information related to the processes or threads which are currently running and managed by the kernel. Additionally, it also provides information related to CPU and memory usage per process.

When you start `top`, you\'ll be presented with the following elements on the main `top` screen:

- Summary area - shows information like system uptime, number of users, load average, and overall memory usage
- Column header - attribute names 
- Task area - displays the data for each process, or `PID`

The output keeps refreshing until you press `q` or `Ctrl` + `c`.

If you want to exit automatically after a specified number of repetitions, use the `-n` option as follows:

```
top -n 10
```

You can press the following keys with `Shift` while `top` is running to sort the table:

| Key | Sorts by        |
| -- | ---------------- |
|`m` | Memory Usage     |
|`p` | CPU Usage        |
|`n` | Process ID (PID) |
|`t` | Running Time     |

For example, you can find out which process is consuming the most memory by entering `Shift` + `m`. 

### 1.7. Display Messages

**`echo`**

The `echo` command displays the given text on the screen. For example, entering: <br>

```
echo "Welcome to the linux lab"
```

prints:
```
Welcome to the linux lab.
```

These special characters help you better format your output:<br>

| Special Character |  Effect |
| --- | ----------------------|
|`\n` | Start a new line |
|`\t` | Insert a tab |

Use the `-e` option of the `echo` command when working with special characters. For example:

```
echo -e "This will be printed \nin two lines"
```

will print:

```
This will be printed
in two lines
```

### 1.8. Display date and time

**`date`**

The `date` command displays the current date and time.

```
date
```

It has several options which allow you to display the current date and time in different formats. <br>
For example, the following command displays the current date in `mm/dd/yy` format:

```
date "+%D"
```

Here are some popular format specifiers that you can try out:

| Specifier | Explanation |
| -- | ------------------------------------------------ |
| `%d` | Displays the day of the month (01 to 31)        |
| `%h` | Displays the abbreviated month name (Jan to Dec)      |
| `%m` | Displays the month of year (01 to 12)       |
| `%Y` | Displays the four-digit year                     |
| `%T` | Displays the time in 24 hour format as HH&#58;MM:SS |
| `%H` | Displays the hour                         |

### 1.9. View the Reference Manual For a Command

**`man`**

The `man` command displays the user manual for any command that you provide as its argument.

For example, to see the manual page for the `ls` command, enter: 

```
man ls
```

Scroll through the command\'s manual to find any info you may need. When you\'re done, press `q` to quit.

You will sometimes encounter a command that does not have a man page avaible on your system. To see all available `man` pages with a brief description of each command, enter:

```
man -k .
```

::page{title="Practice exercises"}

##### 1. Get basic information about the operating system.

<details>
<summary>Click here for Hint</summary>

> Use the `uname` command.

</details>

<details>
<summary>Click here for Solution</summary>

```
uname
```
</details>

##### 2. View all running processes on the system.

<details>
<summary>Click here for Hint</summary>

> Use the `ps` command with the appropriate option to see all processes, not only those owned by you.

</details>

<details>
<summary>Click here for Solution</summary>

```
ps -e
```
</details>

##### 3. Get the table of processes and sort by memory usage.

<details>
<summary>Click here for Hint</summary>

> Use `top`, then sort by memory usage by pressing `Shift` + `m`.

</details>

<details>
<summary>Click here for Solution</summary>

```
top
```
Then press `Shift`+`m`.
</details>

##### 4. Display the current time.

<details>
<summary>Click here for Hint</summary>

> Use the format option `%T` of the `date` command.

</details>

<details>
<summary>Click here for Solution</summary>

```
date "+%T"
```
</details>

##### 5. Using one command, display the messages `"Hello!"` and `"Goodbye!"` separated by a new line.

<details>
<summary>Click here for Hint</summary>

> Use the `echo` command with the `-e` option and the `\n` new line character.

</details>

<details>
<summary>Click here for Solution</summary>

```
echo -e "Hello! \nGoodbye!"
```
</details>

::page{title="Summary"}

In this lab, you learned that you can use the commands:

- `whoami` to return your username
- `uname` to print the kernel name
- `id` to display the user and group id
- `df` to print available disk space
- `ps` to list running processes and their process id
- `top` to view a real-time table of processes
- `echo` to print given text
- `date` to display the current time and date
- `man` to get the user manual for a command

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
| 2023-05-04        | 3.2     | Benny Li         | QA Pass                        |
| 2023-04-10        | 3.1     | Nick Yi           | ID Review                          |
| 2023-01-11        | 3.0     | Jeff Grossman     | Split lab and expand content       |
| 2021-12-02        | 2.1     | Jeff Grossman     | Review and Update lab              |
| 2021-11-29        | 2.0     | Sam Prokopchuk    | Update lab contents and split      |
| 2021-05-30        | 1.0     | Ramesh Sannareddy | Created initial version of the lab |

 Copyright (c) 2021-23 IBM Corporation. All rights reserved.-->
 
 <h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>

