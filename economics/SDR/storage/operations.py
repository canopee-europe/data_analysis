import time
from datetime import timedelta

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from economics.SDR.models.CurrencyData import CurrencyData


def generate_dates(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)


def select_date(driver, date):
    """
    Sélectionne la date dans les listes déroulantes.
    """
    # Sélectionner l'année
    year_select = Select(driver.find_element(By.NAME, "ddlYear"))
    year_select.select_by_value(str(date.year))

    # Sélectionner le mois
    month_select = Select(driver.find_element(By.NAME, "ddlMonth"))
    month_select.select_by_value(str(date.month))

    # Sélectionner le jour
    day_select = Select(driver.find_element(By.NAME, "ddlDay"))
    day_select.select_by_value(str(date.day))

    print(f"Date sélectionnée : {date.strftime('%Y-%m-%d')}")


def validate_selection(driver):
    submit_button = driver.find_element(By.NAME, "btnGo")
    submit_button.click()
    time.sleep(2)


def read_table(driver, date, data_collected):
    """
    Lit le tableau et récupère les données valides.
    """
    date = date.strftime("%d/%m/%Y")
    try:
        tables = driver.find_elements(By.TAG_NAME, "table")
        print(f"Nombre de tables trouvées sur la page : ", len(tables))
        for table in tables:
            if "tightest" in table.get_attribute("class"):
                print("Cette table contient des données.")
                tbody = table.find_element(By.TAG_NAME, "tbody")  # Trouver le tbody
                rows = tbody.find_elements(By.TAG_NAME, "tr")  # Trouver toutes les lignes

                first_valid_row = True
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")  # Trouver toutes les colonnes
                    if len(cols) == 5:
                        if first_valid_row:
                            first_valid_row = False
                            continue
                        else:
                            currency = cols[0].text.strip()
                            exchange_rate = cols[1].text.strip()
                            usd_equivalent = cols[2].text.strip()
                            percent_change = cols[3].text.strip()

                            data_collected.append((date, currency, exchange_rate, usd_equivalent, percent_change))

            else:
                print("Cette table n'est pas la table des données. Passage à la table suivante.")
    except Exception as e:
        print(e)
