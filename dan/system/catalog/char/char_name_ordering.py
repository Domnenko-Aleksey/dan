from classes.Char import Char
import sys
import json
sys.path.append('system/catalog/classes')


def char_name_ordering(SITE):
    print('FUNCTION -> system-> calalog -> char -> ordering')
    CHAR = Char(SITE)

    catalog_id = SITE.post['catalog_id']
    char_id_list = SITE.post['char_id_list'].split(',')

    print('char_id_list', char_id_list)

    ordering = 1
    for char_id in char_id_list:
        data = {
            'id': char_id,
            'catalog_id': catalog_id,
            'ordering': ordering
        }
        CHAR.updateNameOrdering(data)
        ordering += 1

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}