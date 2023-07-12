# Login using Selenium WebDriver and Python

This project demonstrates how to automate the login process using Selenium WebDriver and Python. It includes capturing screenshots for failed scenarios and logging relevant information to a text file.

## Prerequisites

Before running the code, ensure that you have the following installed:

- Python 3.x
- Selenium WebDriver
- WebDriver executable (e.g., ChromeDriver for Google Chrome)

## Setup

1. Clone the repository or download the code files.

2. Install the necessary Python dependencies:
```
pip install selenium
```

3. Download the appropriate WebDriver executable for your browser (e.g., ChromeDriver) and ensure it is accessible in your system's PATH.

## Test Scenarios

#### 1. Failed Login:
  - Inputs wrong credentials.
  - Verifies the failed login alert and takes a screenshot.

#### 2. Successful Login:
  - Inputs correct credentials.
  - Verifies the successful login and takes a screenshot.

#### 3. Logout and Forgot Password:
  - Logs out from the system.
  - Clicks on the forgot password option.
  - Verifies the functionality of the cancel button and takes a screenshot.
  - Clicks on the forgot password option again.
  - Fills up the username to reset and clicks on the reset password button.
  - Verifies the successful password reset notice and takes a screenshot.

## Usage

1. Open the `login.py` file in your preferred text editor.

2. Modify the `USERNAME` and `PASSWORD` variables with your login credentials.

3. Run the script:
```
python login.py
```

4. The script will perform the login process and generate the following files in the project directory:

- `fail_Alert.png`: Captured screenshot of the alert that displayed the login failure.
- `fail_Login.png`: Captured screenshot of the login attempt fails.
- `success_Login.png`: Captured screenshot of the successful login.
- `this_REPORT.txt`: Log file containing relevant information about the login process.

## Configuration

- To use a different browser, modify the WebDriver initialization in the script (`webdriver.Chrome()` for Chrome, `webdriver.Firefox()` for Firefox, etc.).

- If you want to change the location or name of the generated files, update the corresponding file paths and names in the script.

## Troubleshooting

- If you encounter any issues during the execution, ensure that you have the correct WebDriver executable for your browser version.

- Verify that the login process is compatible with the target website. You may need to modify the script accordingly to handle different login scenarios.

- For further assistance or troubleshooting, feel free to contact the project maintainer.

## Contributing

Contributions to this project are welcome. If you encounter any bugs, have feature requests, or want to make improvements, please submit an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
