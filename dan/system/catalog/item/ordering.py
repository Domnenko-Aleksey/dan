import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Item import Item


def ordering(SITE):
    print('FUNCTION -> system-> calalog -> item -> ordering')
    type = SITE.p[2]
    id = SITE.p[3]

    ITEM = Item(SITE)
    section_id = ITEM.ordering(type, id)

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/section/' + str(section_id)}
    return {'redirect': '/system/catalog/section/' + str(section_id)}
