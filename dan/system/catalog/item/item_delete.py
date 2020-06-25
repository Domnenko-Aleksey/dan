from classes.Item import Item
import sys
sys.path.append('system/catalog/classes')


def item_delete(SITE):
    print('FUNCTION -> system-> calalog -> item -> delete')

    id = SITE.post['id']

    ITEM = item(SITE)

    if 'agree' in SITE.post and SITE.post['agree'] == 'yes':
        cat_id = itITEMem.delete(id)
    else:
        cat_id = ITEM.getitem(id)['section_id']

    return {'redirect': '/system/catalog/section/' + str(section_id)}