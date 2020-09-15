from aiohttp import web
import sys
sys.path.append('index/image_predict')
from form import form
from file_upload_ajax import file_upload_ajax

def image_predict(SITE):
    print('PATH -> index/image_predict/image_predict.py')
    print(SITE.p[1])
    functions = {
        '': form,
        'file_upload_ajax': file_upload_ajax
    }

    if (SITE.p[1] not in functions):
        raise web.HTTPNotFound()

    return functions[SITE.p[1]](SITE)