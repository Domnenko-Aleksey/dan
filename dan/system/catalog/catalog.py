from aiohttp import web
import sys
sys.path.append('system/catalog/cat')
sys.path.append('system/catalog/section')
sys.path.append('system/catalog/item')
sys.path.append('system/catalog/char')
sys.path.append('system/catalog/settings')
from cat import cat
from section import section
from item import item
from char import char
from settings import settings



def catalog(SITE):
    print('PATH -> system/catalog')
    # Вызов функций по ключу
    functions = {
        '': cat,  # Управление каталогами
        'cat': cat,
        'section': section,
        'item': item,
        'char': char,
        'settings': settings
    }

    if (SITE.p[1] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[SITE.p[1]](SITE)
