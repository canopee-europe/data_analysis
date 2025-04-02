import pickle
from datetime import datetime

import pandas as pd
from selenium import webdriver

from economics.SDR.models.CurrencyData import CurrencyData
from economics.SDR.storage.operations import generate_dates, select_date, validate_selection, read_table, \
    parallel_scraping


def main():
    start_date: datetime = datetime(1981, 1, 1)
    # end_date: datetime = datetime(1981, 2, 1)
    end_date = datetime.today()

    data_collected: list = parallel_scraping(start_date, end_date, 8)

    print("Données récupérées : ", data_collected)
    return data_collected


if __name__ == "__main__":
    data_collected = main()

    columns = ["Date", "Currency", "Exchange Rate", "USD Equivalent", "Percent Change"]

    # Créer le DataFrame à partir de data_collected
    df = pd.DataFrame(data_collected, columns=columns)

    # Sauvegarder le DataFrame en CSV
    df.to_csv("imf_exchange_rates.csv", index=False, encoding="utf-8")

    print("Les données ont été enregistrées dans 'imf_exchange_rates.csv'")
