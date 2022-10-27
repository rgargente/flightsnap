import os

from flight_log.flight_log import FlightLog


def test_flight_log():
    path = os.path.join(os.path.dirname(__file__), "Flight Track Log VLG82HD 03-Apr-2022 (BIO _ LEBB-LGW _ EGKK) - FlightAware.html")
    log = FlightLog.from_html_file(path)
    time = None # DateTime(2022,1,1,22,00)
    assert log.by_time(time).latlon == (1,2)
    