from .. import maps
from flight_log import LatLon

def test_url_by_lat_lon():
    assert maps.url_by_lat_lon(LatLon(48.6347,-1.8852)) == "https://www.google.com/maps/@48.6347,-1.8852,20000m/data=!3m1!1e3"


# https://www.google.co.uk/maps/@48.634748,-1.8852,14z
# https://www.google.co.uk/maps/@48.6319367,-1.9348852,24549m/data=!3m1!1e3
