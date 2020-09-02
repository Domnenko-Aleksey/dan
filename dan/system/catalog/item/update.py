import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Item import Item
from system.catalog.classes.Char import Char


def update(SITE):
    print('FUNCTION -> system-> calalog -> item -> update')

    id = SITE.p[3]

    ITEM = Item(SITE)
    CHAR = Char(SITE)
    item = ITEM.getItem(id)  # Получаем текущий элемент
    section_id = item['section_id']

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/section/' + str(section_id)}

    chars = []
    i = 1
    for key, value in SITE.post.items():
        # Формируем список словарей характеристик
        if key.startswith('char_'):
            if key == 'char_id[]':
                char_dict = {}
                char_dict['id'] = value
                char_dict['item_id'] = id

            if key == 'char_name_id[]':
                char_dict['name_id'] = value
                char_dict['ordering'] = i

            if key == 'char_value[]':
                char_dict['value'] = value
                chars.append(char_dict)
                i += 1

    # Перебираем список
    for char in chars:
        if char['id'] == '':
            CHAR.insertValue(char);
        else:
            CHAR.updateValue(char);
    ITEM.update({
        'id': id,
        'name': SITE.post['name'],
        'text': SITE.post['text'],
        'data': SITE.post['data'],
        'status': SITE.post['status'],
        'ordering': SITE.post['ordering']
    })

    return {'redirect': '/system/catalog/section/' + str(section_id)}
