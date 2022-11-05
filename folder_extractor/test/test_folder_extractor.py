import os

from .. import FolderExtractor
from flight_log import LatLon


def test_extract_map_urls():
    path = os.path.join(os.path.dirname(__file__), 'data')
    # time_zone_offset=1, pictures taken flying from Spain
    urls = FolderExtractor.from_path(path, time_zone_offset=1).map_urls()

    assert urls == [('folder_extractor/test/data/IMG_20220403_143448518.jpg',
                     LatLon(47.3518, -2.1758)),
                    ('folder_extractor/test/data/IMG_20220403_144428618.jpg',
                     LatLon(48.4035, -1.9491))]
