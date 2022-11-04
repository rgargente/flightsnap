from folder_extractor.folder_extractor import FolderExtractor
from htmlbuilder.htmlbuilder import build_page
import keys

if __name__ == "__main__":
    urls = FolderExtractor.from_path(
        "./test/data/", time_zone_offset=1).map_urls()
    html = build_page(urls, maps_api_key=keys.MAPS_API_KEY)
    with open('sample.html', 'wb') as f:
        f.write(bytes(html, encoding='UTF-8'))
