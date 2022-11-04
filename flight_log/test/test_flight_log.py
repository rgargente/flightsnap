import os

from flight_log.flight_log import FlightLog
from datetime import time

file_name = "Flight Track Log VLG82HD 03-Apr-2022 (BIO _ LEBB-LGW _ EGKK) - FlightAware.html"


def test_from_folder():
    path = os.path.dirname(__file__)
    log = FlightLog.from_folder(path)
    assert len(log.data) > 0


def test_get_lat_lon_by_time():
    path = os.path.join(os.path.dirname(__file__), file_name)
    log = FlightLog.from_html_file(path)
    row = log.by_time(time(13, 45, 59))
    assert row.lat == 48.5757  # type: ignore
    assert row.lon == -1.9022  # type: ignore
    # TODO Test extremes (first, last)
    # TODO Test rows with no values

