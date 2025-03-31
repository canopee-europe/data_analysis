import time
from datetime import datetime

from selenium import webdriver

from economics.SDR.models.CurrencyData import CurrencyData
from economics.SDR.storage.operations import generate_dates, select_date, validate_selection, read_table


def main():
    # Set Selenium driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.imf.org/external/np/fin/data/rms_sdrv.aspx")

    start_date = datetime(1981, 1, 1)
    # end_date = datetime(1981, 1, 5)
    end_date = datetime.today()

    data_collected = []

    for date in generate_dates(start_date, end_date):
        select_date(driver, date)
        validate_selection(driver)
        read_table(driver, date, data_collected)

    # Fermer le navigateur à la fin
    driver.quit()

    print("Données récupérées : ", data_collected)


if __name__ == "__main__":
    main()
