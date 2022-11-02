import os

from folder_extractor.folder_extractor import FolderExtractor


def test_extract_map_urls():
    path = os.path.join(os.path.dirname(__file__), 'data')
    # time_zone_offset=1, pictures taken flying from Spain
    urls = FolderExtractor.from_path(path, time_zone_offset=1).map_urls()

    assert urls == ['https://www.google.com/maps/@50.5204,-0.9538,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@49.3242,-1.6799,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@48.4646,-1.9325,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@49.6154,-1.5548,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@49.2192,-1.7095,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@49.3783,-1.6649,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@50.8357,-0.5452,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@48.7976,-1.8359,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@48.4035,-1.9491,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@49.1171,-1.7396,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@47.3518,-2.1758,20000m/data=!3m1!1e3',
                    'https://www.google.com/maps/@49.0095,-1.7721,20000m/data=!3m1!1e3']
