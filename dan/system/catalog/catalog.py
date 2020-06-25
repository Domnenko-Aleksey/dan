from aiohttp import web
import sys
sys.path.append('system/catalog/cat')
sys.path.append('system/catalog/section')
sys.path.append('system/catalog/item')
from cat import cat
from section import section
from item import item


def catalog(SITE):
    print('PATH -> system/catalog')
    # Вызов функций по ключу
    functions = {
        '': cat,  # Управление каталогами
        'cat': cat,
        'section': section,
        'item': item
        # 'settings': settings,
        # 'char': char
    }

    if (SITE.p[1] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[SITE.p[1]](SITE)
