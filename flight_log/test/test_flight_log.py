import os

from flight_log.flight_log import FlightLog
from datetime import time


def test_get_lat_lon_by_time():
    path = os.path.join(os.path.dirname(
        __file__), "Flight Track Log VLG82HD 03-Apr-2022 (BIO _ LEBB-LGW _ EGKK) - FlightAware.html")
    log = FlightLog.from_html_file(path)

    row = log.by_time(time(13, 45, 59))
    print(row)
    assert row.LatitudeLat == '48.575748.58'  # type: ignore
    assert row.LongitudeLon == '-1.9022-1.90'  # type: ignore


# https://www.google.co.uk/maps/@48.634748,-1.8852,14z
# https://www.google.co.uk/maps/@48.6319367,-1.9348852,24549m/data=!3m1!1e3