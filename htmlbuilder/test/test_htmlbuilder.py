from .. import build_page
from flight_log import LatLon


def test_htmlbuilder():
    img_latlon = [('folder_extractor/test/data/IMG_20220403_150556779.jpg',
                   LatLon(50.5204, -0.9538)),
                  ('folder_extractor/test/data/IMG_20220403_144455184.jpg',
                   LatLon(48.4646, -1.9325))]
    html = build_page(img_latlon)
    # TODO Test html content
    assert len(html) > 0
