import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# assign the chrome driver path
CHROME_DRIVER_PATH = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

# assign the headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# adding target website
response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D"
                        "%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C"
                        "%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37"
                        ".857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B"
                        "%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22"
                        "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D"
                        "%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf"
                        "%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B"
                        "%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1"
                        "%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D", headers=HEADERS)

# grabbing the data from website
data = response.text
soup = BeautifulSoup(data, "html.parser")

# target the list element for extraction
all_link_elements = soup.select(".list-card-top a")

# creating empty list
all_link = []

# garb all the link and save it into the list
for link in all_link_elements:
    href = link["href"]
    # print(href)
    # if http not found then append in the list
    if "http" not in href:
        all_link.append(f"https://www.zillow.com{href}")
    else:
        all_link.append(href)

# grab all the address of the links
all_address_elements = soup.select(".list-card-info address")
all_address = [address.get_text().split(" | ")[-1] for address in all_address_elements]
# print(all_address)

# grab all the prices from link
all_price_elements = soup.select(".list-card-details li")
all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]
# print(all_prices)
