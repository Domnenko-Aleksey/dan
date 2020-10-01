from aiohttp import web
import sys
sys.path.append('index/page')
from index.page.classes.Page import Page

def page(SITE):
    print('PATH -> index/page/page.py')
    page_id = 1

    SITE.content = '<div class="w1200, p_40_20">Страница вывода PAGE</div>'
    
    if not page_id:
        raise web.HTTPNotFound()
