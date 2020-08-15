from aiohttp import web
import re
import sys

sys.path.append('system/catalog/char')
from char_name_list import char_name_list
from char_name_edit import char_name_edit
from char_name_insert import char_name_insert
from char_name_update import char_name_update
from char_name_ordering import char_name_ordering
from char_name_delete import char_name_delete


def char(SITE):
    print('PATH -> system/catalog/char')

    if SITE.p[2].isdigit() > 0:
        return char_name_list(SITE)

    # Вызов функций по ключу
    functions = {
        'add': char_name_edit,
        'edit': char_name_edit,
        'insert': char_name_insert,
        'update': char_name_update,
        'ordering': char_name_ordering,
        'delete': char_name_delete,
    }

    if SITE.p[2] in functions:
        return functions[SITE.p[2]](SITE)
    
    # Если функция не существует и это не номер раздела - 404
    raise web.HTTPNotFound()