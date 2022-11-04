from flight_log.flight_log import LatLon

def url_by_lat_lon(latlon: LatLon):
    alt = 20000
    # data=!3m1!1e3 displays sat mode
    return f"https://www.google.com/maps/@{latlon.lat},{latlon.lon},{alt}m/data=!3m1!1e3"