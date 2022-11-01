def url_by_lat_lon(lat, lon):
    alt = 20000
    # data=!3m1!1e3 displays sat mode
    return f"https://www.google.com/maps/@{lat},{lon},{alt}m/data=!3m1!1e3"