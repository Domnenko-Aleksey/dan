from aiohttp import web
import re
import sys

sys.path.append('system/catalog/char')
from system.catalog.char.name_list import name_list
from system.catalog.char.edit import edit
from system.catalog.char.insert import insert
from system.catalog.char.update import update
from system.catalog.char.ordering import ordering
from system.catalog.char.delete import delete


def char(SITE):
    print('PATH -> system/catalog/char')

    if SITE.p[2].isdigit() > 0:
        return name_list(SITE)

    # Вызов функций по ключу
    functions = {
        'add': edit,
        'edit': edit,
        'insert': insert,
        'update': update,
        'ordering': ordering,
        'delete': delete,
    }

    if SITE.p[2] in functions:
        return functions[SITE.p[2]](SITE)
    
    # Если функция не существует и это не номер раздела - 404
    raise web.HTTPNotFound()