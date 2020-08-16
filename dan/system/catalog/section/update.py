import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Section import Section


def update(SITE):
    print('FUNCTION -> system-> calalog -> section -> update')

    section_id = SITE.p[3]
    SECTION = Section(SITE)
    section = SECTION.getSection(section_id)  # Получаем текущий элемент
    catalog_id = section['catalog_id']

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/cat/' + str(catalog_id)}

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
