import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Catalog import Catalog


def update(SITE):
    print('FUNCTION -> system-> calalog -> cat -> update')

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/cat'}

    CATALOG = Catalog(SITE)
    catalog = CATALOG.getItem(SITE.p[3])  # Получаем текущий элемент

    if CATALOG.checkUrl(SITE.post['url'], catalog['url']) is not None:
        SITE.content += '<div class="bg_gray"><h1>Ошибка</h1><div>url <b>' + \
            SITE.post['url'] + '</b> - занят!</div></div>'
        return

    CATALOG.update({
        'url': SITE.post['url'],
        'name': SITE.post['name'],
        'ordering': SITE.post['ordering'],
        'id': SITE.p[3]
    })

    return {'redirect': '/system/catalog/cat'}
