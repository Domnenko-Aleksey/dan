from aiohttp import web
import sys
sys.path.append('index/mainpage')
sys.path.append('index/graph')
from index.mainpage import mainpage
from index.graph import graph


def router(SITE):
    print('INDEX - router')

    # Вызов функций по ключу
    functions = {
        '': mainpage.mainpage,
        'graph': graph.graph
        # 'users': users,
        # 'help': help
    }

    if (SITE.p[0] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()


    # Вызов функции
    return functions[SITE.p[0]](SITE)
