from system.catalog.classes.Filter import Filter
import sys
import json
sys.path.append('system/catalog/classes')

def filter_delete_ajax(SITE):
    print('FILE -> /system/catalog/section/filter_delete_ajax.py')
    FILTER = Filter(SITE)
    FILTER.delete(SITE.post['id'])
    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}
