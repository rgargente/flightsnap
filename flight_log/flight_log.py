from calendar import timegm
from time import time
import pandas as pd
from pandas.core.frame import DataFrame
from attr import define
from attrs import define
from bs4 import BeautifulSoup
import re
from datetime import time


@define
class FlightLog:
    data: DataFrame

    @classmethod
    def from_html_file(cls, path):
        with open(path) as f:
            table = BeautifulSoup(f, 'lxml').select('#tracklogTable', limit=1)
        df = pd.read_html(str(table))[0]
        _parse(df)
        return cls(df)

    def by_time(self, time: time):
        i = self.data.time.searchsorted(time)  # type: ignore
        # i is the where we would insert time to maintain order
        # TODO Let's just take the previous one for now, we might want to take either i-1 or i, whichever is closer
        if i > 0: i -= 1
        return self.data.iloc[i]


def _parse(df: DataFrame):
    df['time'] = df['Time (BST)BST'].apply(_extract_time)
    df['lat'] = df['LatitudeLat'].apply(_extract_lat_lon)
    df['lon'] = df['LongitudeLon'].apply(_extract_lat_lon)

def _extract_time(time: str):
    match = re.search(r'\d{2}:\d{2}:\d{2}', time)
    if match:
        t = match.group()
        am_pm = time[-2:]
        return pd.Timestamp(f"{t}{am_pm}").time()
    else:
        return None

def _extract_lat_lon(latlon: str):
    match = re.search(r".*?\.\d{4}", latlon)
    if match:
        return float(match.group())
    else:
        return None