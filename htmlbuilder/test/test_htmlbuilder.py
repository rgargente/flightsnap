from htmlbuilder.htmlbuilder import build_page

def test_htmlbuilder():
    urls = [('folder_extractor/test/data/IMG_20220403_150556779.jpg',
             'https://www.google.com/maps/@50.5204,-0.9538,20000m/data=!3m1!1e3'),
            ('folder_extractor/test/data/IMG_20220403_144455184.jpg',
             'https://www.google.com/maps/@48.4646,-1.9325,20000m/data=!3m1!1e3')]
    html = build_page(urls)
    assert len(html) > 0