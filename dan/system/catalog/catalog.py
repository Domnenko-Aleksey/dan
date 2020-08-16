from aiohttp import web
import sys
sys.path.append('system/catalog/cat')
sys.path.append('system/catalog/section')
sys.path.append('system/catalog/item')
sys.path.append('system/catalog/char')
sys.path.append('system/catalog/settings')
from system.catalog.cat import cat
from system.catalog.section import section
from system.catalog.item import item
from system.catalog.char import char
from system.catalog.settings import settings



def catalog(SITE):
    print('PATH -> system/catalog')
    # Вызов функций по ключу
    functions = {
        '': cat.cat,  # Управление каталогами
        'cat': cat.cat,
        'section': section.section,
        'item': item.item,
        'char': char.char,
        'settings': settings.settings
    }

    if (SITE.p[1] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[SITE.p[1]](SITE)
