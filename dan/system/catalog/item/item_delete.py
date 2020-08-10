from classes.Item import Item
import sys
sys.path.append('system/catalog/classes')


def item_delete(SITE):
    print('FUNCTION -> system-> calalog -> item -> delete')

    id = SITE.p[3]

    ITEM = Item(SITE)
    section_id = ITEM.delete(id)

    return {'redirect': '/system/catalog/section/' + str(section_id)}