from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import re


def main():
    # Configure browser options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # Set browser
    driver = webdriver.Chrome(options=options)
    url: str = "https://www.global-rates.com/fr/inflation/historique/"
    driver.get(url)

    # Find links to pages to scrap
    url_links: list[WebElement] = driver.find_elements(By.XPATH, "//a[contains(@href, 'inflation/historique')]")
    url_links = url_links[1:-1]

    urls_storage = []

    for link in url_links:
        urls_storage.append(link.get_attribute("href"))

    # Set browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver_2 = webdriver.Chrome(options=options)

    dict_inflation = {}

    for url in urls_storage:
        driver_2.get(url)

        year = re.search(r'(\d{4})', url).group(1)

        first_table = driver_2.find_element(By.TAG_NAME, "table")
        rows = first_table.find_elements(By.TAG_NAME, "tr")
        dict_inflation[year] = []

        for row in rows[1:]:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) >= 4:
                country = columns[1].get_attribute("textContent").strip()
                inflation = columns[3].get_attribute("textContent").strip()
                dict_inflation[year].append((country, inflation))

    print(dict_inflation)

    driver_2.quit()


if __name__ == "__main__":
    main()
