from aiohttp import web
import re
import sys
sys.path.append('system/catalog/item')
from item_edit import item_edit
from item_insert import item_insert
from item_update import item_update
from item_ordering import item_ordering
from item_pub import item_pub
from item_delete import item_delete


def item(SITE):
    print('PATH -> system/catalog/item')
    # Вызов функций по ключу
    functions = {
        'add': item_edit,
        'edit': item_edit,
        'insert': item_insert,
        'update': item_update,
        'up': item_ordering,
        'down': item_ordering,
        'pub': item_pub,
        'unpub': item_pub,
        'delete': item_delete,
    }

    if (SITE.p[2] in functions):
        return functions[SITE.p[2]](SITE)

    # Если функция не существует и это не номер раздела - 404
    raise web.HTTPNotFound()
