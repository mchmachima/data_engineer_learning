::page{title=" Hands-on Lab: Unit Testing "}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="cognitiveclass.ai logo">

## Unit Testing Lab

**Estimated time needed: 30 minutes**

## Objectives

After completing this lab you will be able to:

-   Write unit tests to test a function.
-   Run unit tests and interpret the results.

::page{title="About the lab environment"}

Cloud IDE is an open-source IDE(Integrated Development Environment), that can be run on desktop or on cloud. You will be using the Cloud IDE to do this lab. When you log into the Cloud IDE environment, you are presented with a &#39;dedicated computer on the cloud&#39; exclusively for you. This is available to you as long as you work on the labs. Once you log off, this &#39;dedicated computer on the cloud&#39; is deleted along with any files you may have created. So, it is a good idea to finish your labs in a single session. If you finish part of the lab and return to the Theia lab later, you may have to start from the beginning. Plan to work out all your Theia labs when you have the time to finish the complete lab in a single session.

::page{title="Create a new python file named mymodule.py"}

On the window, Right click on the **Explorer** and select **New File** option, as shown in the image below.<br>

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/BdOq065I6y-k4xTPTm7MDQ/Python-newfile.png)

A pop up appears with title **New File**, as shown in the image below.<br>

![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/file_new_popup.png)

Enter "mymodule.py" as the file name and click **OK**.
![File Name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/file_new_popup2.png)

A file "mymodule.py" will be created for you.

You are now ready to add code to mymodule.py

Copy and paste the below code into mymodule.py

```
def square(number):
    """
    This function returns the square of a given number
    """
    return number ** 2

def double(number):
    """
    This function returns twice the value of a given number
    """
    return number * 2
```

You should see a screen like this now.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/module.png)

Save the file by using the Save option in the File Menu.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/save_file.png)

::page{title="Write Unit Tests"}

## Write the unit tests for square function

Let us write test cases for these three scenarios.

* When 2 is given as input the output must be 4.
* When 3.0 is given as input the output must be 9.0.
* When -3 is given as input the output must not be -9.

## Write the unit tests for double function

Let us write test cases for these three scenarios.

* When 2 is given as input the output must be 4.
* When -3.1 is given as input the output must be -6.2.
* When 0 is given as input the output must be 0.

## Create a new file and name it as test_mymodule.py

Copy and paste the below code into test_mymodule.py

```python
import unittest

from mymodule import square, double

class TestSquare(unittest.TestCase): 

    def test1(self): 
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.

class TestDouble(unittest.TestCase): 

    def test1(self): 
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.
        
unittest.main()
```

You should see a screen like this now.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/testcase.png)

### Understanding the code

**Imports:** We begin by importing the `unittest` module, which provides the tools needed to write and run tests. We also import the `square` and `double` functions from `mymodule` — these are the functions we want to test.

**TestSquare class:** In `unittest`, related tests are grouped into a class that inherits from `unittest.TestCase`. The `TestSquare` class contains a single test method `test1` — all test methods must start with the word `test` so the test runner can automatically detect and execute them. Inside `test1`, we use `assertEqual` to verify that `square(2)` returns 4 and that `square(3.0)` returns 9.0, confirming the function works correctly for both integer and float inputs. We use `assertNotEqual` to confirm that `square(-3)` does not return -9, since squaring a negative number must always yield a positive result.

**TestDouble class:** The `TestDouble` class follows the same structure and tests the `double` function. We verify that doubling 2 returns 4, that doubling the negative float -3.1 returns -6.2, and that doubling 0 returns 0 — this last case is an important edge case to confirm the function behaves correctly at the boundary.

**`unittest.main()`:** This line at the end tells Python to run all the test cases defined in the module when the script is executed directly. It automatically discovers and runs every method that starts with `test` across all `TestCase` classes in the file.

::page{title="Run tests"}

To run tests, click on the "Terminal" and then click on the "New Terminal"

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/images/000.png)

It will open the terminal 

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/images/abc.png)

Run command python3 test_mymodule.py and this will run the tests.

You should see a screen like this now.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/images/def.png)

An `OK` in the last line indicates that all tests passed successfully.

`FAILED` in the last line indicates that at least one test has failed, and python prints which test or tests failed.

::page{title="Write unit tests for the given function"}

Here is a function that accepts two arguments and returns their sum.

Copy and paste the below code into mymodule.py and the save the file.

```
def add(a,b):
    """
    This function returns the sum of the given numbers
    """
    return a + b

```

<br>
Write test cases for these scenarios.

* When 2 and 4 are given as input the output must be 6.

* When 0 and 0 are given as input the output must be 0.
* When 2.3 and 3.6 are given as input the output must be 5.9.
* When the strings 'hello' and 'world' are given as input the output must be 'helloworld'.
* When 2.3000 and 4.300 are given as input the output must be 6.6.
* When -2 and -2 are given as input the output must **not** be 0. (Hint : Use assertNotEqual)

## Author(s)

Ramesh Sannareddy

### Other Contributors

Rav Ahuja
<!--
## Changelog

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2020-11-25        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
| 2022-10-21        | 0.2     | Shivam Kumar      | Updated screenshots |
| 2026-03-24 | 0.3 | Rajashree Patil | Added description for the code |

-->
<h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>

