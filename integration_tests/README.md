# Hudl Candidate Project - Integration Tests

## Integration Tests Overview

### Objectives

* Set up an automation environment using Selenium
* Automate cases to test the functionality of logging into [hudl.com](https://www.hudl.com/)
* Document the tests with comments and a README.md file
* Push tests and documentation to a public GitHub repository
* Share the link to the repo

### Assumptions
* Valid login credentials will be provided by Hudl

### Constraints
* Credentials must be kept secure and must not be pushed to GitHub

### Approach
#### Prerequisites
* git (latest) Or git bash for Windows
* python 3.10
* pip 22.0.2
* venv (latest)

#### Environment
The test environment is a virtual environment consisting of:
* pytest 7.2.1
* selenium 4.8.0
* pickle5 0.0.11
The environment is managed with venv, pip and a requirements.txt file.
The tests were developed and validated on Ubuntu 22.04 running in Windows Subsystem for Linux version 2 on Windows 11. However, they should run in any Windows, Mac or Linux environment that has the prerequisites installed.

### Framework
* The test framework is based on Pytest and Selenium is used to automate browser actions.
* All framework and test code is in Python except where Javascript snippets are executed in Selenium for specific pruposes.
* The test framework will be configured to support both Chrome and Firefox browsers to demonstrate multiple browser support.

### Architecture
In order to develop robust and extensible tests the following are implemented:
* Page Object Model with a Base page class.
- The pages encapsulate and abstract the details of the page implmenetation to make tests more robust against changes
* A Datamanager class is used to encapsulate and abstract functionality associated with the driver, borwser, window manipulation, etc.
* Data-driven tests are used to implement similar tests (differ primarily in test data) with minimal code repetition
Note that no Base test class is implemented. Since there is only one test class currently, it is not clear yet what functionality for tests should be pushed down to a Base class.

### Analysis
A matrix was used for identifying possible test cases.
The horizontal axis includes all actions that were enabled on the Login page, plus Logout, which is closely related.
Since Testing the effect of closing a window and a session are similar tests to the logout test, they are also included.
The vertical axis identifes possible variations of tests and the intersection represents possible tests.
Not all combinations are valid tests. These marked 'na'.
Valid test combinations are marked with a T.
Notes are added to each row and column as required for clarity.
A total of 15 tests are identifed and implemented.
The matrix is shown below.
All of these tests were run successfully manually as part of the automation effort.

|                     |Notes                    |Login                 |Need help?   |Sign up   |Remember me           |Logout |Close window   |End session  |
|---------------------|-------------------------|:--------------------:|------------:|:--------:|:--------------------:|:-----:|:-------------:|:-----------:|
|Valid                |                         |T                     |na           |na        |na                    |na     |na             |na           |
|Bad email            |                         |T                     |na           |na        |na                    |na     |na             |na           |
|Bad password         |                         |T                     |na           |na        |na                    |na     |na             |na           |
|Case insensitive email|                        |T                     |na           |na        |na                    |na     |na             |na           |
|Case sensitive password - upper|               |T                     |na           |na        |na                    |na     |na             |na           |
|Case sensitive password - lower|               |T                     |na           |na        |na                    |na     |na             |na           |
|Mismatched valid email and valid password|     |T                     |na           |na        |na                    |na     |na             |na           |
|Click                 |                        |na                    |T            |T         |na                    |na     |na             |na           |
|Remember me - checked |See limitations below   |na                    |na           |na        |See note              |T      |T              |T            |
|Remember me - unchecked|See limitations below  |na                    |na           |na        |See note              |T      |T              |T            |
|Notes                 |                        |Data-driven tests.    |             |          |Rember me tested with |na     |               |             |
|                      |                        |Adding tests is easy. |             |          |logout related tests  |na     |               |             |

### Limitations
It was not possible in the time available to determine how to replicate/simulate the 'Remeber me' functionality.
The implementation is not know. An attempt was made to save and restore cookies across a browser session, but this did not seem to replicate the desired behavior.
This invalidates the following tests:
* Logout with "Remember me' checked
* Close window with "Remember me' checked
* End session with "Remember me' checked
Also the following test fails but cannot be marked as an xfail because it is a data-driven test:
* End session with "Remember me' checked
If the 'Remember me' cannot be duplocated in an automated test, these tests will have to be tested manually.

## How to Run Tests

### Initial Setup

1. Ensure that prerequisites are installed.
- Python can be downloaded from [here](https://www.python.org/downloads/). The installation of of Python for all platforms is covered by many sources. One example is [Install Python: Detailed Instructions for Window, Mac, and Linux](https://python.land/installing-python).
- Usually pip and venv are installed with Python3. However, if they are not install pip according to instructions for your OS, then use pip to install venv.
- The installation of of Git for all platforms is also covered by many sources. One example is from GitHub [Install Git](https://github.com/git-guides/install-git) or there is a very detailed one from Atlassian [Install Git](https://www.atlassian.com/git/tutorials/install-git).
3. Clone or fork and clone this repository, or download and extract the zip file.
- To fork the repository in GitHub use the `Fork` dropdown in the upper right hand corner of the window.
- To clone either the original or the fork copy the HTTPS URL for the repo from the green `<>Code` dropdown button.
- Change to the direcxtory you want to be the parent of the repo. Use the command:
```git clone <url>```
4. This will give you a subfolder/subdirectory `hudl-candidate-project`. Navigate to to the `hudl-candidate-proj/integration_tests` subdirectory.
5. Create a Python virtual environment.
- Use the following command:
```python3 -m venv .venv```
(You can use any name in for your environment rather than `.venv`. The `.` is optional).
- Activate your envirnment with the command
```source .venv/bin/activate``` 
in Bash on Linux and Mac, and 
```.venv\bin\Activate.ps1``` 
in Powershell on Windows. If you did not use `.venv` for your environment name, substitute what you did use. You should see your command line prefixed with the environment name.
- Install other requirements using the command
```pip install -r requirements.txt```
6. Set up your Hudl credentials.
- Using the editor or IDE of your choice, create a file call `user_creds.py` in the `integration_tests` directory.
- In the file enter
``` python
email = "<your email>"
password = "<>your password"
```
- This file will be ignored by Git.

### Executing Tests

1. In the `integration_tests` directory you can execute all the tests simply using the command ```pytest```
2. There are other ways of running tests with pytest as covered in the pytest documentation [Usage and Invocations](https://docs.pytest.org/en/6.2.x/usage.html)
- One of the most useful standard commmand line options is `-k="some string to match`. It will cause pytest to only run tests with the string to match in it. For example:```pytest -k="login"``` only runs tests with "login" in their name.
3. Some custom options that have been implemented:
- `--baseurl="base url"` This is useful for testing in different environments or international versions of the site. It defaulst to `https://www.hudl.com`. An example usage would be `pytest --baseurl="https://es.hudl.com"` or `baseurl="https://staging.hudl.com"`
- `--browser="browswer name"` Chrome and Firefox are currently supported. It defaults to Chrome. An example usage would be `pytest --browser="firfox"`




