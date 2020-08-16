import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Section import Section


def ordering(SITE):
    print('FUNCTION -> system-> calalog -> section -> ordering')
    data = {'id': SITE.p[3], 'type': SITE.p[2]}

    SECTION = Section(SITE)
    cat_id = SECTION.ordering(data)

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/cat/' + str(cat_id)}
    return {'redirect': '/system/catalog/cat/' + str(cat_id)}
