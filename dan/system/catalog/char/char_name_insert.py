from classes.Char import Char
import sys
sys.path.append('system/catalog/classes')


def char_name_insert(SITE):
    print('FUNCTION -> system-> calalog -> char -> insert')

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/char/' + SITE.post['catalog_id']}

    CHAR = Char(SITE)
    CHAR.insertName({
        'catalog_id': SITE.post['catalog_id'],
        'name': SITE.post['name'],
        'unit': SITE.post['unit'],
        'type': SITE.post['type'],
        'ordering': SITE.post['ordering']
    })

    return {'redirect': '/system/catalog/char/' + SITE.post['catalog_id']}
