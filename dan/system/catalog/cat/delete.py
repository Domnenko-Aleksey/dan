import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Catalog import Catalog


def delete(SITE):
    print('FUNCTION -> system-> calalog -> cat -> delete')

    if 'agree' in SITE.post and SITE.post['agree'] == 'yes':
        CATALOG = Catalog(SITE)
        catalog = CATALOG.delete(SITE.post['id'])  # Удаляем текущий элемент

    return {'redirect': '/system/catalog/cat'}