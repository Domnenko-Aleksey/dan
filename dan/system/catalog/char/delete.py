import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Char import Char


def delete(SITE):
    print('FUNCTION -> system-> calalog -> char -> delete')

    CHAR = Char(SITE)
    catalog_id = CHAR.deleteName(SITE.p[3])

    return {'redirect': '/system/catalog/char/' + str(catalog_id)}

