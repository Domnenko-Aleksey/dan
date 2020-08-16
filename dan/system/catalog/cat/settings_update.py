import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Catalog import Catalog


def settings_update(SITE):
    print('FUNCTION -> system-> calalog -> cat -> settings_update')
    
    CATALOG = Catalog(SITE)
    catalog = CATALOG.settingsUpdate(SITE.p[3], SITE.post['settings'])  # Удаляем текущий элемент

    return {'redirect': '/system/catalog/cat'}