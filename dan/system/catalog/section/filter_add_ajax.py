from system.catalog.classes.Char import Char
import sys
import json
sys.path.append('system/catalog/classes')


def filter_add_ajax(SITE):
    print('FILE -> /system/calalog/section/filter_add_ajax.py')
    CHAR = Char(SITE)
    catalog_id = SITE.post['catalog_id']
    char_dict = CHAR.getNameList(catalog_id)

    options = ''
    if char_dict:
        for char in char_dict:
            options +=  '<option value=' + str(char['id']) + ' data-type="' + char['type'] + '" data-unit="' + char['unit'] + '">'
            options +=   char['name']
            options += '</option>'
        content = '<select id="char_name_select" onChange="SYSTEM.catalog.section.char_insert();" class="input"><option value=""></option>' + options + '</select>'
    else:
        content = '<div>Нет характеристик!</div><div style="margin:10px 0px;"><a href="/admin/com/catalog/char/' + catalog_id + '">Добавить характеристику</a></div>'

    answer = {'answer': 'success', 'content': content}
    return {'ajax': json.dumps(answer)}
