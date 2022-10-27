import os

from flight_log.flight_log import FlightLog
from datetime import time


def test_get_lat_lon_by_time():
    path = os.path.join(os.path.dirname(
        __file__), "Flight Track Log VLG82HD 03-Apr-2022 (BIO _ LEBB-LGW _ EGKK) - FlightAware.html")
    log = FlightLog.from_html_file(path)

    row = log.by_time(time(13, 1, 0))
    assert row.LatitudeLat == '43.598743.60'  # type: ignore
    assert row.LongitudeLon == '-2.9112-2.91'  # type: ignore
