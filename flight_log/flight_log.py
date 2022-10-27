import pandas as pd
from pandas.core.frame import DataFrame
from attr import define
from attrs import define
from bs4 import BeautifulSoup

@define
class FlightLog:
    data: DataFrame

    @classmethod
    def from_html_file(cls, path):
        with open(path) as f:
            table = BeautifulSoup(f, 'lxml').select('#tracklogTable', limit=1)
        df = pd.read_html(str(table))[0]
        return cls(df)

    def by_time(self, time): 
        return None
