from selenium import webdriver
import time
import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
valid = input("Are you Anurag? Y or N:")
if(valid=='Y'):
    email = 'Your email'
    password = 'your password'
else:
    email = input("Enter your gmail id:")
    password = getpass.getpass("Enter your password:")
driver = webdriver.Firefox()
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
assert "Gmail" in driver.title
e_id = driver.find_element_by_id("identifierId")
e_id.clear()
e_id.send_keys(email)
wait_time = 1
element = WebDriverWait(driver, wait_time).\
    until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
element.click()
time.sleep(3)
passwd = driver.find_element_by_name("password")
passwd.clear()
passwd.send_keys(password)

element = WebDriverWait(driver, wait_time).\
    until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
element.click()

assert "No results found." not in driver.page_source

