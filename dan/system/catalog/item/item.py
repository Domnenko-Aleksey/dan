from aiohttp import web
import sys
sys.path.append('system/catalog/item')
from system.catalog.item.edit import edit
from system.catalog.item.insert import insert
from system.catalog.item.update import update
from system.catalog.item.ordering import ordering
from system.catalog.item.pub import pub
from system.catalog.item.delete import delete


def item(SITE):
    print('PATH -> system/catalog/item')
    # Вызов функций по ключу
    functions = {
        'add': edit,
        'edit': edit,
        'insert': insert,
        'update': update,
        'up': ordering,
        'down': ordering,
        'pub': pub,
        'unpub': pub,
        'delete': delete,
    }

    if (SITE.p[2] in functions):
        return functions[SITE.p[2]](SITE)

    # Если функция не существует и это не номер раздела - 404
    raise web.HTTPNotFound()
