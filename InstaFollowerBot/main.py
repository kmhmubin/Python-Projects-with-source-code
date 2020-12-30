import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\chromedriver\chromedriver.exe"
SIMILAR_ACCOUNT = "akifahi"
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        # send the keys
        username.send_keys(USERNAME)
        time.sleep(1)
        password.send_keys(PASSWORD)
        time.sleep(2)

        password.send_keys(Keys.ENTER)

    def find_follower(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        # find the followers button
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(3)

        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')

        for i in range(10):
            # execute JavaScript script for scroll the top of the modal
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)

    def follow(self):
        pass


# main driver

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_follower()
bot.follow()
