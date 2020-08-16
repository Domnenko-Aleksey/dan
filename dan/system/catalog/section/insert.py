import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Section import Section


def insert(SITE):
    print('FUNCTION -> system-> calalog -> section -> insert')

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/cat/' + SITE.post['catalog_id']}

    SECTION = Section(SITE)
    SECTION.insert({
        'catalog_id': SITE.post['catalog_id'],
        'parent_id': SITE.post['parent_id'],
        'name': SITE.post['name'],
        'text': SITE.post['text'],
        'data': SITE.post['data'],
        'status': SITE.post['status'],
        'ordering': SITE.post['ordering']
    })

    return {'redirect': '/system/catalog/cat/' + SITE.post['catalog_id']}
