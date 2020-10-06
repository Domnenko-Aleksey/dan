from aiohttp import web
import sys
sys.path.append('index/page')
sys.path.append('index/modules')
from index.modules import catalog_section_items
from index.modules import catalog_item

def page(SITE):
    print('PATH -> index/page/page.py')

    # ЧПУ URL
    print(SITE.p[1])
    if SITE.p[1] == 'section':
        cat_sections(SITE)
    elif SITE.p[1] == 'item':
        cat_item(SITE, int(SITE.p[2]))
    else:
        raise web.HTTPNotFound()

        
# Вывод содержимого раздела
def cat_sections(SITE):
    section_id = 1
    SITE.content =  '<div class="bg_gray">'
    SITE.content +=     '<div class="w1200 p_40_20">'
    SITE.content +=         '<h1>Разделы каталога 1</h1>'
    SITE.content +=         '<div class="flex_row">' + catalog_section_items.catalog_section_items(SITE, section_id) + '</div>'
    SITE.content +=     '</div>'
    SITE.content += '</div>'


# Вывод элемента
def cat_item(SITE, id):
    SITE.content =  '<div class="w1200 p_40_20">'
    SITE.content +=     catalog_item.catalog_item(SITE, id)
    SITE.content += '</div>'