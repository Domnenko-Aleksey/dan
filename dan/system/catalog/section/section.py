from aiohttp import web
import re
import sys
sys.path.append('system/catalog/section')
from system.catalog.section.edit import edit
from system.catalog.section.insert import insert
from system.catalog.section.update import update
from system.catalog.section.ordering import ordering
from system.catalog.section.pub import pub
from system.catalog.section.delete import delete
from system.catalog.section.section_list import section_list
from system.catalog.section.filter_add_ajax import filter_add_ajax
from system.catalog.section.filter_delete_ajax import filter_delete_ajax


def section(SITE):
    print('PATH -> system/catalog/section')

    # Вызов функций по ключу
    functions = {
        'add': edit,
        'edit': edit,
        'insert': insert,
        'update': update,
        'up': ordering,
        'down': ordering,
        'pub': pub,
        'unpub': pub,
        'delete': delete,
        'filter_add_ajax': filter_add_ajax,
        'filter_delete_ajax': filter_delete_ajax
    }

    if (SITE.p[2] in functions):
        return functions[SITE.p[2]](SITE)
    
    if re.search('^\d+$', SITE.p[2]):
        return section_list(SITE)

    # Если функция не существует и это не номер раздела - 404
    raise web.HTTPNotFound()
