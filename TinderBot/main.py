# Tinder Bot

from selenium import webdriver
from time import sleep

# constant values
EMAIL = "kmhmubin@gmail.com"
PASSWORD = "01515621057"

chrome_driver_path = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

sleep(5)
# go to tinder website
driver.get("https://tinder.com")
# sleep 7 sec
sleep(6)

# accept the cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

sleep(6)

# press the main login button
login_btn = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_btn.click()

sleep(7)

# select the google login option
google_login = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
google_login.click()

sleep(8)

# save the main window
base_window = driver.window_handles[0]
# switching the google login window
temp_window = driver.window_handles[1]
driver.switch_to.window(temp_window)

sleep(3)

input_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
input_email.send_keys(EMAIL)

sleep(1)
# click the next button
email_next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
email_next.click()

sleep(2)
# select the password input box
pass_input = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pass_input.send_keys(PASSWORD)

sleep(4)
# click the next button
pass_next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
pass_next.click()

sleep(5)

# go back to original window
driver.switch_to.window(base_window)

sleep(10)

# allow popups
location = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location.click()

sleep(2)

# match popup
match = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
match.click()

sleep(5)

