import sys
import json
sys.path.append('system/catalog/classes')
from system.catalog.classes.Section import Section


def delete(SITE):
    print('FUNCTION -> system-> calalog -> section -> delete')

    id = SITE.post['id']

    SECTION = Section(SITE)

    if 'agree' in SITE.post and SITE.post['agree'] == 'yes':
        cat_id = SECTION.delete(id)
    else:
        cat_id = SECTION.getSection(id)['catalog_id']
    
    answer = {'answer': 'success', 'cat_id': cat_id}
    return {'ajax': json.dumps(answer)}