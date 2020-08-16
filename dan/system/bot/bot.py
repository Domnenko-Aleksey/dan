from aiohttp import web
import sys
sys.path.append('system/bot/mainpage')
sys.path.append('system/bot/keyword')
sys.path.append('system/bot/answer')
from system.bot.mainpage import mainpage
from system.bot.keyword import keyword
from system.bot.answer import answer


def bot(SITE):
    print('PATH -> system/bot')

    functions = {
        '': mainpage.mainpage,
        'keyword': keyword.keyword,
        'answer': answer.answer,
    }

    if (SITE.p[1] not in functions):
        raise web.HTTPNotFound()

    return functions[SITE.p[1]](SITE)