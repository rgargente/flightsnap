import os

from .. import FolderExtractor
from flight_log import LatLon


def test_extract_map_urls():
    path = os.path.join(os.path.dirname(__file__), 'data')
    # time_zone_offset=1, pictures taken flying from Spain
    imgs_latlon = FolderExtractor.from_path(
        path, time_zone_offset=1).images_latlon()

    assert imgs_latlon == [('folder_extractor/test/data/IMG_20220403_144428618.jpg', LatLon(lat=48.4035, lon=-1.9491)),
                           ('folder_extractor/test/data/IMG_20220403_143448518.jpg', LatLon(lat=47.3518, lon=-2.1758))]
