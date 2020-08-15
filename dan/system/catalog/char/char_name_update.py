from classes.Char import Char
import sys
sys.path.append('system/catalog/classes')


def char_name_update(SITE):
    print('FUNCTION -> system-> calalog -> char -> update')

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/char/' + SITE.post['catalog_id']}

    CHAR = Char(SITE)
    CHAR.updateName({
        'name': SITE.post['name'],
        'unit': SITE.post['unit'],
        'type': SITE.post['type'],
        'ordering': SITE.post['ordering'],
        'id': SITE.p[3]
    })

    return {'redirect': '/system/catalog/char/' + SITE.post['catalog_id']}
