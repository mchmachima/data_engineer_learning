::page{title="Hands-on Lab: Static Code Analysis"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/images/IDSN-logo.png" width="200" alt="cognitiveclass.ai logo">

##

Estimated time needed: **30** minutes

## Objectives

 After completing this lab you will be able to:

-   Install pylint package
-   Run Static Code Analysis on a python program
-   Check the compliance score of a python program.
-   Fix common mistakes and improve the compliance score.

::page{title="Install the pylint package"}

1. Open a new terminal.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/new-terminal.png">
2. At the terminal run the following command to install pylint.

```
pip3 install pylint==2.11.1
```

3. This should install the pylint package.
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/pylint_pip.png">

::page{title="Create a sample python file for static code analysis"}

Create a new file named **sample1.py**

Copy and paste the below code into **sample1.py**

```python
# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
def add(number1, number2):
    # The function returns the sum of 'number1' and 'number2'.
    return number1 + number2

# Initialize the variable 'num1' with the value 4.
num1 = 4

# Initialize the variable 'num2' with the value 5.
num2 = 5

# Call the 'add' function with 'num1' and 'num2' as arguments and store the result in 'total'.
total = add(num1, num2)

# Print the result of adding 'num1' and 'num2' using the 'format' method to insert the values into the string.
print("The sum of {} and {} is {}".format(num1, num2, total))

```

Save the file **sample1.py**

::page{title="Run pylint"}

* Open a terminal
* Run the below command
```shell
 pylint sample1.py
 ```
* Pylint goes through every line of code and gives you a list all the non-compliant lines.
* Pylint gives you a compliance score (10 being maximum).

::page{title="Correct the mistakes identified by pylint."}

* Based on the report given by pylint, changes were made to this code to address the following issues.
    * Missing module-level docstring (`missing-module-docstring`)
    * Missing function docstring (`missing-function-docstring`)
    * Invalid constant naming — module-level variables should follow `UPPER_CASE` naming convention (`invalid-name`)
    * Line too long — one of the comment lines exceeds the default 100-character limit (`line-too-long`)
    * Missing final newline at the end of the file (`missing-final-newline`)
    * Use of `.format()` where an f-string is preferred (`consider-using-f-string`)

> **Note on constant naming:** Pylint treats all variables defined at the module level (outside of functions or classes) as constants and expects them to follow `UPPER_CASE` naming. This applies even to variables that store the result of a function call, such as `total`. To satisfy pylint, either name them in `UPPER_CASE` (e.g., `TOTAL`) or add an inline `# pylint: disable=invalid-name` comment on that line.

* Create a new file named **sample2.py**
* Copy and paste the below code into **sample2.py**

```python
"""This module demonstrates a simple addition operation using a helper function."""

# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
# The purpose of this function is to add the two numbers and return the result.
def add(number1, number2):
    """Return the sum of number1 and number2."""
    # Return the sum of 'number1' and 'number2'.
    # This line computes the addition of the two input numbers and outputs the result.
    return number1 + number2

# Initialize the constant variable 'NUM1' with the value 4.
# Constants are usually written in uppercase letters to indicate that they should not be changed.
NUM1 = 4

# Initialize the constant variable 'NUM2' with the value 5.
# This variable will be used as the second input to the 'add' function.
NUM2 = 5

# Call the 'add' function with 'NUM1' and 'NUM2' as arguments.
# The result of this addition operation is stored in the variable 'TOTAL'.
TOTAL = add(NUM1, NUM2)

# Print a formatted string that displays the sum of 'NUM1' and 'NUM2'.
# An f-string is used to insert the values of 'NUM1', 'NUM2', and 'TOTAL' into the string.
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
```

Save the file **sample2.py**

::page{title="Run pylint"}

* Open a terminal
* Run the below command
```shell
pylint sample2.py
```
* This will give you the compliance score.
* This time you should see the score improve significantly — aiming for a perfect 10.

::page{title="Your task"}

Improve the score in sample2.py to a perfect 10 by correcting all the issues pointed out by pylint. If you can't figure out how to solve some issues it is helpful to google the pylint message.

<details><summary>  Hints for common issues:</summary>

* **`missing-module-docstring`** — A module docstring is a short description placed at the very top of the file (the first line), before any code. It is written between triple quotes. For example: `"""This module does X."""`

* **`missing-function-docstring`** — A function docstring is a short description placed as the very first line inside a function, written between triple quotes. For example, right after `def add(number1, number2):`, add a new line: `"""Return the sum of number1 and number2."""`

* **`invalid-name`** — Pylint expects all module-level variables (variables defined outside of any function) to be named in `UPPER_CASE`. This includes variables that store computed results. For example, rename `num2` to `NUM2` and `total` to `TOTAL`.

* **`consider-using-f-string`** — Instead of `"...{}...".format(value)`, use an f-string: `f"...{value}..."`. F-strings are simpler to read and are the modern preferred style in Python.

* **`missing-final-newline`** — Make sure your file ends with a blank line by pressing Enter once after the last line of code before saving.

* **`line-too-long`** — Each line of code or comments must be no longer than 100 characters. If a comment is too long, split it across two shorter lines.
</details>

::page{title="Congratulations!"}

 You now know how to perform static code analysis.

## Author(s)

Ramesh Sannareddy

### Other Contributors

Rav Ahuja

<!--
## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2020-11-25        | 1.0     | Ramesh Sannareddy | Created initial version of the lab |
| 2020-01-29        | 1.1     | Rav Ahuja | Formatting & license changes |
| 2022-10-21 | 2.0 | Ratima | Updated Skill Network Logo screenshot|
| 2026-03-23 | 3.0 | Rajashree | Updated Sample2 file's code for better linting score and added hints |
-->

<h3 align="center"> &#169; IBM Corporation. All rights reserved. <h3/>
