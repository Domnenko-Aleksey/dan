from classes.Char import Char
import sys
sys.path.append('system/catalog/classes')


def char_name_delete(SITE):
    print('FUNCTION -> system-> calalog -> char -> delete')

    CHAR = Char(SITE)
    catalog_id = CHAR.deleteName(SITE.p[3])

    return {'redirect': '/system/catalog/char/' + str(catalog_id)}

