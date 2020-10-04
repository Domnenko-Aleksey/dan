from aiohttp import web
import sys
sys.path.append('index/mainpage')
sys.path.append('index/graph')
sys.path.append('index/image_predict')
sys.path.append('index/page')
sys.path.append('index/mod')
from index.mainpage import mainpage
from index.page import page

# from index.graph import graph
# from index.image_predict import image_predict


def router(SITE):
    # Вызов функций по ключу
    functions = {
        '': mainpage.mainpage,
        'page': page.page,
        'catalog': page.page,
        # 'graph': graph.graph,
        # 'image_predict': image_predict.image_predict
        # 'users': users,
        # 'help': help
    }

    if (SITE.p[0] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[SITE.p[0]](SITE)

