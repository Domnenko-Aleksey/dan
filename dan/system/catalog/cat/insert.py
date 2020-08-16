import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Catalog import Catalog


def insert(SITE):
    print('FUNCTION -> system-> calalog -> cat -> insert')

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/cat'}

    CATALOG = Catalog(SITE)
    if CATALOG.checkUrl(SITE.post['url']) is not None:
        SITE.content += '<div class="bg_gray"><h1>Ошибка</h1><div>url <b>' + \
            SITE.post['url'] + '</b> - занят!</div></div>'
        return

    CATALOG.insert({'url': SITE.post['url'], 'name': SITE.post['name'], 'ordering': SITE.post['ordering']})

    return {'redirect': '/system/catalog/cat'}
