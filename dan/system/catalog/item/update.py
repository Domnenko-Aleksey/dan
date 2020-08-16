import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Item import Item


def update(SITE):
    print('FUNCTION -> system-> calalog -> item -> update')

    id = SITE.p[3]

    ITEM = Item(SITE)
    item = ITEM.getItem(id)  # Получаем текущий элемент
    section_id = item['section_id']

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/section/' + str(section_id)}

    ITEM.update({
        'id': id,
        'name': SITE.post['name'],
        'text': SITE.post['text'],
        'data': SITE.post['data'],
        'status': SITE.post['status'],
        'ordering': SITE.post['ordering']
    })

    return {'redirect': '/system/catalog/section/' + str(section_id)}
