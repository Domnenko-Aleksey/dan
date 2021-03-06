import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Char import Char


def update(SITE):
    print('FILE -> /system/calalog/char/update.py')

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
