from aiohttp import web
import sys
sys.path.append('index')
sys.path.append('index/graph')
from graph import graph
from mainpage import mainpage

def router(SITE):
    print('INDEX - router')

    # Вызов функций по ключу
    functions = {
        '': mainpage,
        'graph': graph
        # 'users': users,
        # 'help': help
    }

    if (SITE.p[0] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[SITE.p[0]](SITE)
