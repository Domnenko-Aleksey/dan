from system.catalog.classes.Char import Char
import sys
import json
sys.path.append('system/catalog/classes')


def char_list_add_ajax(SITE):
    print('FUNCTION -> system-> calalog -> char -> char_list_add_ajax')
    CHAR = Char(SITE)

    catalog_id = SITE.post['catalog_id']
    char_arr = CHAR.getNameList(catalog_id)

    options = ''
    for char in char_arr:
        options +=  '<option value=' + str(char['id']) + ' data-type="' + char['type'] + '" data-unit="' + char['unit'] + '">'
        options +=   char['name']
        options += '</option>'

    content =  '<select id="char_name_select" onChange="SYSTEM.catalog.item.char_insert();" class="input">'
    content +=   '<option value=""></option>' + options
    content += '</select>'

    answer = {'answer': 'success', 'content': content}
    return {'ajax': json.dumps(answer)}
