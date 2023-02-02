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
* python 3.10
* pip 22.0.2
* venv latest

#### Environment
The test environment is a virtual environment consisting of:
* pytest 7.2.1
* selenium 4.8.0
* pickle5 0.0.11
The environment is managed with venv, pip and a requirements.txt file.

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



