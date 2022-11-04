import os

from folder_extractor.folder_extractor import FolderExtractor


def test_extract_map_urls():
    path = os.path.join(os.path.dirname(__file__), 'data')
    # time_zone_offset=1, pictures taken flying from Spain
    urls = FolderExtractor.from_path(path, time_zone_offset=1).map_urls()

    assert urls == [('folder_extractor/test/data/IMG_20220403_143448518.jpg',
                    'https://www.google.com/maps/@47.3518,-2.1758,20000m/data=!3m1!1e3'),
                    ('folder_extractor/test/data/IMG_20220403_144428618.jpg',
                     'https://www.google.com/maps/@48.4035,-1.9491,20000m/data=!3m1!1e3')]
