from collections import Counter
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
count = 1
while True:
    driver.get(
        "https://www.oneroof.co.nz/search/houses-for-sale/region_auckland-35_page_" + str(count))
    all_listings = driver.find_elements(By.TAG_NAME, "a")

    print("Page " + str(count))
    expression = '^(https:\/\/www\.oneroof\.co\.nz\/)([0-9]+)([\S]*)$'
    with open('listings.txt', 'a') as file:
        for listing in all_listings:
            link = listing.get_attribute("href")
            if re.search(expression, link):
                # file.write(link+"\n")
                print(link+"\n")
    count += 1
