from aiohttp import web
import sys
sys.path.append('system/catalog/cat')
from system.catalog.cat.edit import edit
from system.catalog.cat.insert import insert
from system.catalog.cat.cat_list import cat_list
from system.catalog.cat.update import update
from system.catalog.cat.ordering import ordering
from system.catalog.cat.delete import delete
from system.catalog.cat.settings_edit import settings_edit
from system.catalog.cat.settings_update import settings_update
from system.catalog.cat.sec_list import sec_list

print('sys.path',sys.path)


def cat(SITE):
    print('PATH -> system/catalog/cat')

    if SITE.p[2].isdigit():
        return sec_list(SITE)

    # Вызов функций по ключу
    functions = {
        '': cat_list,
        'edit': edit,
        'add': edit,
        'insert': insert,
        'update': update,
        'up': ordering,
        'down': ordering,
        'delete': delete,
        'settings_edit': settings_edit,
        'settings_update': settings_update,
    }

    if (SITE.p[2] in functions):
        return functions[SITE.p[2]](SITE)

    # Если функция не существует и это не номер раздела - 404
    raise web.HTTPNotFound()
    
