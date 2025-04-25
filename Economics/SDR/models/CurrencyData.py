from dataclasses import dataclass
from datetime import datetime


@dataclass
class CurrencyData:
    date: datetime
    currency: str
    exchange_rate: float
    usd_equivalent: float
    percent_change: float

    def __init__(self,
                 date: datetime,
                 currency: str,
                 exchange_rate: float,
                 usd_equivalent: float,
                 percent_change: float):
        self.date = date
        self.currency = currency
        self.exchange_rate = exchange_rate
        self.usd_equivalent = usd_equivalent
        self.percent_change = percent_change
