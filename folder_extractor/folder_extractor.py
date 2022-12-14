import os
from datetime import datetime
from glob import glob

from attrs import define, field
from PIL import Image

from flight_log import FlightLog, LatLon


@define
class FolderExtractor:
    path: str
    time_zone_offset: int
    _log: FlightLog = field()

    @_log.default
    def _flight_log_factory(self):
        return FlightLog.from_folder(self.path)

    @classmethod
    def from_path(cls, path: str, time_zone_offset=0):
        return cls(path, time_zone_offset)

    def images_latlon(self) -> list[tuple[str, LatLon]]:
        # TODO Support other image types
        return list(map(self._img_latlon_from_path, glob(os.path.join(self.path, '*.jpg'))))

    def _img_latlon_from_path(self, img_path) ->  tuple[str, LatLon]:
        img_time = _extract_time(img_path)

        # TODO This is a horrible hack, it will fail with midnight flights. Better to use proper datetime and timedelta
        img_time = img_time.replace(hour=img_time.hour - self.time_zone_offset)

        row = self._log.by_time(img_time)
        return (os.path.relpath(img_path), row.latlon)


def _extract_time(img_path):
    date_time_original_key = 306  # Magic value! https://exiv2.org/tags.html
    # TODO My sample images don't have 34858 (time zone offset) but it could be extracted here
    exifs = Image.open(img_path).getexif().items()
    dt_str = next(v for k, v in exifs if k == date_time_original_key)
    time_str = dt_str.split()[1]
    return datetime.strptime(time_str, '%H:%M:%S').time()
