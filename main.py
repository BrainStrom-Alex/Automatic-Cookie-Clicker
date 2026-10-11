from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time, sleep
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(2)
language = driver.find_element(By.ID, value="langSelect-EN")
language.click()

wait_time = 5
timeout = time() + wait_time  # Check for purchases every 5 seconds
five_min = time() + 60 * 5  # Run for 5 minutes

sleep(2)
while True:
    button = driver.find_element(By.ID, value="bigCookie")
    button.click()

    if time() > timeout:
        cookies_count = driver.find_element(By.ID, value="cookies").text
        cookie = int(cookies_count.split(" ")[0])
        products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

        best_item = None
        for product in reversed(products):  # Start from most expensive (bottom of list)
            # Check if item is available and affordable (enabled class)
            if "enabled" in product.get_attribute("class"):
                best_item = product
                break

        if best_item:
            best_item.click()

        timeout = time() + wait_time
    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break

