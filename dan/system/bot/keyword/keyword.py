from aiohttp import web
import sys
from system.bot.keyword.keyword_list import keyword_list
from system.bot.keyword.edit import edit


def keyword(SITE):
    print('PATH -> system/bot/keyword')

    if SITE.p[2].isdigit():
        return keyword_list(SITE)

    functions = {
        'add': edit,
        'edit': edit,
        #'delete': delete,
        #'insert': insert,
        #'update': update,
    }

    if (SITE.p[2] not in functions):
        # raise web.HTTPNotFound()
        return keyword_list(SITE)

    return functions[SITE.p[2]](SITE)
