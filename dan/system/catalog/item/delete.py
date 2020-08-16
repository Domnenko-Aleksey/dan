import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Item import Item


def delete(SITE):
    print('FUNCTION -> system-> calalog -> item -> delete')

    id = SITE.p[3]

    ITEM = Item(SITE)
    section_id = ITEM.delete(id)

    return {'redirect': '/system/catalog/section/' + str(section_id)}