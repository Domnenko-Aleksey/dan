from aiohttp import web
import sys
sys.path.append('index/graph/graph_1')
# sys.path.append('index/graph/graph_2')
from graph_1 import graph_1
# from graph_2 import graph_2


def graph(SITE):
    print('PATH -> index/graph')
    # Вызов функций по ключу
    functions = {
        '': graph_1,  # Управление каталогами
        'graph_1': graph_1,
        # 'graph_2': graph_2,
    }

    if (SITE.p[1] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[SITE.p[1]](SITE)