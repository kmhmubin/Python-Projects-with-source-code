from selenium import webdriver

CHROME_DRIVER_PATH = "C:\chromedriver\chromedriver.exe"
SIMILAR_ACCOUNT = "akifahi"
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        pass

    def find_follower(self):
        pass

    def follow(self):
        pass


# main driver

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_follower()
bot.follow()
