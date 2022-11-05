from airium import Airium

from flight_log import LatLon
from maps import maps


def build_page(img_latlon: list[tuple[str, LatLon]], maps_api_key: str = "") -> str:
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html():
        with a.head():
            a.meta(charset="utf-8")
            a.title(_t="Flight SNAP!")
        with a.body():
            for src, latlon in img_latlon:
                with a.div():
                    a.p(_t=src)
                    a.img(src=src, style="width: 49%")
                    a.iframe(style="width: 49%; height: 40em",
                             src=maps.embed_url_by_latlon(latlon, maps_api_key))
    return str(a)
