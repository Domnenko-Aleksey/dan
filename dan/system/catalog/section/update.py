import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Section import Section
from system.catalog.classes.Filter import Filter


def update(SITE):
    print('FILE -> system/calalog/section/update.py')

    section_id = SITE.p[3]
    SECTION = Section(SITE)
    FILTER = Filter(SITE)
    section = SECTION.getSection(section_id)  # Получаем текущий элемент
    catalog_id = section['catalog_id']

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/cat/' + str(catalog_id)}

    filters = []
    i = 1
    for key, value in SITE.post.items():
        # Формируем список словарей характеристик
        if key.startswith('filter_'):
            if key == 'filter_id[]':
                filter_dict = {}
                filter_dict['id'] = value
                filter_dict['section_id'] = section_id

            if key == 'filter_char_id[]':
                filter_dict['char_id'] = value

            if key == 'filter_value_1[]':
                filter_dict['value_1'] = value

            if key == 'filter_value_2[]':
                filter_dict['value_2'] = value
                filter_dict['ordering'] = i
                filters.append(filter_dict)
                i += 1

    # Перебираем фильтры
    for filter in filters:
        if filter['id'] == '':
            FILTER.insert(filter);
        else:
            FILTER.update(filter);

    SECTION.update({
        'id': section_id,
        'parent_id': SITE.post['parent_id'],
        'name': SITE.post['name'],
        'text': SITE.post['text'],
        'data': SITE.post['data'],
        'status': SITE.post['status'],
        'ordering': SITE.post['ordering']
    })

    return {'redirect': '/system/catalog/cat/' + str(catalog_id)}
