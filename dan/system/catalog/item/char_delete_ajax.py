from system.catalog.classes.Char import Char
import sys
import json
sys.path.append('system/catalog/classes')

def char_delete_ajax(SITE):
    print('FUNCTION -> system-> calalog -> char -> char_delete_ajax')
    CHAR = Char(SITE)
    CHAR.deleteValue(SITE.post['id'])
    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}