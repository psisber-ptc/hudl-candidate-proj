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

## Initial Setup

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

## Executing Tests

1. In the `integration_tests` directory you can execute all the tests simply using the command ```pytest```
2. There are other ways of running tests with pytest as covered in the pytest documentation [Usage and Invocations](https://docs.pytest.org/en/6.2.x/usage.html)
- One of the most useful standard commmand line options is `-k="some string to match"`. It will cause pytest to only run tests with the string to match in it. For example:```pytest -k="login"``` only runs tests with "login" in their name.
3. Some custom options have been implemented:
- `--baseurl="base url"` This is useful for testing in different environments or international versions of the site. It defaulst to `https://www.hudl.com`. An example usage would be `pytest --baseurl="https://es.hudl.com"` or `baseurl="https://staging.hudl.com"`
- `--browser="browswer name"` Chrome and Firefox are currently supported. It defaults to Chrome. An example usage would be `pytest --browser="firfox"`
**NOTE: The final test will fail due to the issue with replicating the 'Remember me' functionality**

## Developing Tests

### Source Code Managment with Git and Gitflow

1. Refer Git documentation sources for details on using Git. Atlassian has a good tutorial [Getting Started](https://www.atlassian.com/git/tutorials/setting-up-a-repository) and a cheat sheet [Git cheat sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
2. An overview of Gitflow is available from Atlassian [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

### Working on a Jira Ticket

1. As part of your scrum team activities you will be assigned to write tests for developer Jira Stories.
- You might collaborate on a Story which includes development and testing, and be assigned one or more Subtasks.
- You might be assigned your own Jira Story or Task that is purely for testing. However, even in this case your Jira ticket should be linked to one or more developer tickets that are to be tested.
2. With the repository cloned to your local machine (part of the setup instructions) you should ensure that your code is up to date.
- You should always start from the `develop` branch, but NEVER work on the `develop` branch.
- Before starting any work, you should update your copy of the `develop` branch with the `develop` branch on GitHub. You can do this with:
`git checkout develop`
`git fetch`
`git status` (To see how far behind the remote `develop` branch you are)
`git pull`
3. Now you need a branch to work on.
4. If the code you need to test has been merged to `develop`, then you should create a new branch from `develop` with:
`git checkout -b <name of new branch>`
- The branch name should be be unique, descriptive, not too long, have no spaces (use `-` to separate words) and be all lower case except perhaps for the Jira project indicator. It should include the Jira ticket ID.
5. Sometimes the code you need to test has not been merged to develop.
- You need to checkout the branch that has the code to be tested. do this with:
`git checkout <branch name>`
- You may also need to do do a `git fetch -all` before the checkout:
`git fetch --all`
`git checkout <branch name>`
- If you are collaborating closely with the developer, you can work on this branch.
- More likely though you will be working on your own branch which you will create from the developers branch with:
`git checkout -b <new branch name>`
- The same requirements for the branch name previously mentioned apply.
6. At this point you are ready to develop automated tests. However, you need an environment to develop your and test your tests against.

### Test Development Environment

1. It is assumed that you will be developing your automated tests on your own laptop.
2. It is also assumed that you can spin up a testable version of the application under test on your laptop, or you or someone else can build and deploy it to some other environment.

### Writing Automated Tests

1. Start by exploring the feature, function or fix that you need to develop a test for to become familiar with it.
- Not always, but typically the initial test is manual and the automated tests become part of nightly or other periodic tests regression test, or regressions tests for  aspecific phase or milestione of the development cycle.
- This should be a systemtic, efficient process. Might create a matrix or checklist to help you identify what to test, and to guide your exploratory testing.
- Use this phase to document the test cases you intend to automate in Jira according to defined guidelines.
- Also use this phase to identify the pages (or API endpoints because the exploratory testing could be testing an API with Postman) and the key items your tests will need to interact with.
- Documentation of testcases should be very high level. You will capture the testcase details in the comments and readability of your test code.
- It goes without saying that any failures you encounter in this phase (or ant any other time) should recorded in Jira according to established guidelines.
2. Next you should familiarize yourself with any existing automated tests for similar and/or related functionality. You may be able to levearge existing page objects (or endpoint abstractions) for your tests.
3. At thispoint you should start writing your tests.
- You should expand the framework in terms of page objects or similar API-related constructs, and simple helper functions.
- Avoid enhancing the core framework unless you have been assigned to do that.
- Avoid over design. Do not refactor anticpating a need, but only once there is a clear need for refactoring.
- Ensure that your tests do not have any dependencies on the implementation of the feature except for how it is structured (e.g. what pages are involved, what functionality is associated with a page and what the page transitions are).

### Contributing Your Code

1. You should be committing your code regularly locally with:
`git add <item(s) to be added>` to stage specific items or
`git add .` for all items (note this will not stage any changes in a parent directory)
folowed by
git commit [-m "Commit message"]
2. When you are ready to push your code to GitHub for the first time (sooner rather than later - it does not have to be complete), you can push your branch with
`git push -u origin <branch name>`
3. Subsequently you can simply use
`git push`
4. When you have developed and tested your test you are ready to merge your code in GitHub.
- Generally, but not alway,s this will be to the branch that was the starting point for your branch.
- Push your code again then create a Pull Request (PR) in GitHub according to defined guidelines.
5. Address the comments from reviewers. Make necessary changes and push the changes until your is approved and merged.


