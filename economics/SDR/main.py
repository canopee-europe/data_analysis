from datetime import datetime

from selenium import webdriver

from economics.SDR.models.CurrencyData import CurrencyData
from economics.SDR.storage.operations import generate_dates, select_date, validate_selection, read_table, \
    parallel_scraping

data_collected = []

def main():
    global data_collected

    start_date = datetime(1981, 1, 1)
    # end_date = datetime(1982, 1, 1)
    end_date = datetime.today()

    data_collected = parallel_scraping(start_date, end_date, 8)

    print("Données récupérées : ", data_collected)


if __name__ == "__main__":
    main()
