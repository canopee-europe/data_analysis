import pickle
from datetime import datetime, timedelta

import pandas as pd
from pandas import DataFrame
from pandas.core.interchange.dataframe_protocol import DataFrame
from selenium import webdriver

from economics.SDR.models.CurrencyData import CurrencyData
from economics.SDR.storage.operations import generate_dates, select_date, validate_selection, read_table, \
    parallel_scraping


def main():
    file: str = "data/imf_exchange_rates_brut.csv"

    df = pd.read_csv(file)

    df["Date"] = pd.to_datetime(df["Date"])

    # Get last date of df
    last_row = df.tail(1)
    last_date = last_row['Date'].iloc[0].date()

    # Set today's date
    today = datetime.today().date()

    print(last_date)
    print(today)

    # Launch program condition
    if last_date < today:
        next_date = last_date + timedelta(days=1)

        data_collected = parallel_scraping(next_date, today, 4)

        # Add new lines to df
        new_data = pd.DataFrame(data_collected,
                                columns=["Date", "Currency", "Currency Amount", "Exchange Rate", "USD Equivalent"])

        df_concat = pd.concat([df, new_data], ignore_index=True)

        # Save to .csv file
        df_concat.to_csv(file, index=False)

    else:
        print("Les données sont déjà à jour.")


if __name__ == "__main__":
    main()

