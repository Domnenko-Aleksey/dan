from classes.Item import Item
import sys
sys.path.append('system/catalog/classes')


def item_insert(SITE):
    print('FUNCTION -> system-> calalog -> item -> insert')

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/section/' + SITE.post['section_id']}

    ITEM = Item(SITE)
    ITEM.insert({
        'section_id': SITE.post['section_id'],
        'name': SITE.post['name'],
        'text': SITE.post['text'],
        'data': SITE.post['data'],
        'status': SITE.post['status'],
        'ordering': SITE.post['ordering']
    })

    return {'redirect': '/system/catalog/section/' + SITE.post['section_id']}
