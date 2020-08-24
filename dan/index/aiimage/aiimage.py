from aiohttp import web
import sys
sys.path.append('index/aiimage/aiimage_1')
sys.path.append('index/aiimage/aiimage_2')
from aiimage_1 import aiimage_1
# from aiimage_2 import aiimage_2


def aiimage(SITE):
    print('PATH -> index/aiimage')

    functions = {
        '': aiimage_1,  
        'aiimage_1': aiimage_1,
        # 'aiimage_2': aiimage_2,
    }

    if (SITE.p[1] not in functions):
        raise web.HTTPNotFound()

    return functions[SITE.p[1]](SITE)