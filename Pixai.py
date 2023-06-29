import sys
import time
import csv
import threading
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoadingAnimation(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def run(self):
        symbols = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        index = 0
        while not self._stop_event.is_set():
            sys.stdout.write('\r' + 'Loading ' + symbols[index % len(symbols)])
            sys.stdout.flush()
            time.sleep(0.1)
            index += 1

def process_symbol():
    sys.stdout.write('⠶')
    sys.stdout.flush()
    time.sleep(0.5)

def completed_symbol():
    sys.stdout.write('✓\n')
    sys.stdout.flush()

class PixAi:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.credit = 0
        self.last_claimed = ""

    def login(self):
        process_symbol()
        print(" ✅ Logging In.")
        driver.get('https://pixai.art/login')
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in with email')]")
        login_button.click()
        email_input = driver.find_element(By.ID, 'email-input')
        email_input.send_keys(self.email)
        password_input = driver.find_element(By.ID, 'password-input')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)

    def open_credit(self):
        process_symbol()
        print(" ✅ Opening Tab.")
        profile = driver.find_element(By.XPATH, "//div[2]/div/div")
        profile.click()

        opening_profile = driver.find_element(By.XPATH, "//li[contains(.,'Profile')]")
        opening_profile.click()

        time.sleep(1)

        Credit_tab = driver.find_element(By.XPATH, "//span[contains(.,'Credits')]")
        Credit_tab.click()

    def claim_points(self):
        process_symbol()
        print(" ✅ Claiming daily points.")
        try:
            time.sleep(1)
            button = driver.find_element(By.XPATH, "//button[contains(.,'Claim them!')]")
            if button.is_enabled():
                button.click()
                print("[🪙] Credits claimed successfully!")
                time.sleep(1.75)
                closing_toastify = driver.find_element(By.CSS_SELECTOR, ".Toastify__close-button > svg")
                closing_toastify.click()
            else:
                print("Button is not clickable.")
        except NoSuchElementException:
            print("Already Claimed. Come tomorrow.")

    def logout(self):
        process_symbol()
        print(" ✅ Logging Out.")
        time.sleep(1)
        profile = driver.find_element(By.XPATH, "//div[2]/div/div")
        profile.click()

        time.sleep(1)
        menu_element = driver.find_element(By.XPATH, "//div/div[3]/div/div")
        menu_element.click()
        time.sleep(0.75)
        logout_menu_item = driver.find_element(By.XPATH, "//li[10]")
        logout_menu_item.click()
        time.sleep(2)

    def process_account(self):
        self.login()
        self.open_credit()
        self.claim_points()
        self.logout()

def update_points():
    print("Updating and claiming daily points.")
    for i, account in enumerate(accounts):
        print(f"Processing account {i+1}/{len(accounts)}")
        loading_animation = LoadingAnimation()
        loading_animation.start()
        pixai = PixAi(account['email'], account['password'])
        pixai.process_account()
        loading_animation.stop()
        loading_animation.join()
        completed_symbol()

# List of account credentials
accounts = []

with open('logins.csv', 'r') as file:
    reader = csv.DictReader(file)
    file.seek(0)  # Reset the file pointer to the beginning
    for row in reader:
        email = row['username']
        password = row['password']
        account = {'email': email, 'password': password}
        accounts.append(account)

# Initialize the WebDriver using geckodriver for Firefox
driver = webdriver.Firefox()  # Assumes geckodriver is in your system PATH

time.sleep(5)

# Main program loop
update_points()

# Close the browser
driver.quit()
