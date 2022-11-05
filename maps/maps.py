from flight_log import LatLon


def url_by_lat_lon(latlon: LatLon):
    alt = 20000
    # data=!3m1!1e3 displays sat mode
    return f"https://www.google.com/maps/@{latlon.lat},{latlon.lon},{alt}m/data=!3m1!1e3"


def embed_url_by_latlon(latlon: LatLon, api_key=""):
    zoom = 10
    return f"https://www.google.com/maps/embed/v1/view?key={api_key}&center={latlon.lat},{latlon.lon}&zoom={zoom}&maptype=satellite"
