import fire

import htmlbuilder
import keys
from folder_extractor import FolderExtractor


def run(input_folder, time_zone_offset=0, name='flightsnap'):
    imgs_latlon = FolderExtractor.from_path(input_folder, time_zone_offset).images_latlon()
    html = htmlbuilder.build_page(imgs_latlon, maps_api_key=keys.MAPS_API_KEY)
    with open(f'{name}.html', 'wb') as f:
        f.write(bytes(html, encoding='UTF-8'))


if __name__ == "__main__":
    fire.Fire(run)
