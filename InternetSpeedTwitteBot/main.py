from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 100
PROMISED_UP = 100

CHROME_DRIVER_PATH = "C:\chromedriver\chromedriver.exe"

TWITTER_USERNAME = "Your Twitter username"
TWITTER_PASSWORD = "Your twitter password"


class InternetSpeedTwitteBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def GetInternetSpeed(self):
        # speed test website
        self.driver.get("https://www.speedtest.net")
        time.sleep(8)
        # click the go button
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()

        # wait 60s
        time.sleep(60)

        # grab the download speed
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Down: {self.down}")
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                    '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(f"Up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(3)

        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_USERNAME)
        password.send_keys(TWITTER_PASSWORD)

        time.sleep(3)
        # press enter 
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


# main driver

bot = InternetSpeedTwitteBot(CHROME_DRIVER_PATH)
bot.GetInternetSpeed()
bot.tweet_at_provider()
