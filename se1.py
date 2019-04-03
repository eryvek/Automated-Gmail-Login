from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://vtop.vit.ac.in/student/stud_login.asp")
assert "Login" in driver.title
reg = driver.find_element_by_name("regno")
reg.clear()
reg.send_keys("16BIT0178")
passwd = driver.find_element_by_name("passwd")
passwd.clear()
passwd.send_keys("AnuhaR123098#$")
sub = driver.find_element_by_class_name("submit3")
sub.click()
assert "No results found." not in driver.page_source

