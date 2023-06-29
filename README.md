# PixAi Automation Script

## Overview
PixAi Automation Script is a Python script that automates the process of logging into the PixAi website, claiming daily points, and logging out. It uses the Selenium library to interact with the browser.

## Features
- Automated login to PixAi website using provided credentials
- Claiming daily points for each account
- Automated logout after completing the process for each account

## Prerequisites
Before running the script, ensure that you have the following prerequisites:
1. Python 3 installed on your machine
2. The Selenium library installed (you can install it using `pip install selenium`)
3. A compatible web browser installed (e.g., Firefox) and its respective web driver (e.g., geckodriver for Firefox) added to your system PATH 



## Installation and Usage
1. Clone the repository to your local machine:
```
git clone https://github.com/uuc110/PixAI-Point_Claiming_bot
```
2. Navigate to the project directory:
```
cd pixai-automation-script
```
3. Export your browser's password data to a CSV file named `logic.csv` with the following columns: `email` and `password`. Remove any unnecessary columns from the exported CSV file, keeping only these two columns.

4. Run the script:
```
python main.py
```

## Screenshots

![Screenshot](Screenshot\screenshot.png)

## Contributing
Contributions are welcome! If you would like to contribute to the project, please follow these guidelines:
- Fork the repository and create a new branch for your feature or bug fix.
- Ensure your code follows the project's coding style and conventions.
- Test your changes thoroughly.
- Make a pull request with a clear description of your changes and the problem it solves.


## Feedback

If you have any feedback, please make a issue and give your feedback there😄

## Disclaimer
This project is intended for educational purposes and self-learning. Please use this script responsibly and do not misuse it for any illegal activities or unauthorized access.



