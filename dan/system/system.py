from aiohttp import web
import sys
sys.path.append('system/mainpage')
sys.path.append('system/catalog')
sys.path.append('system/bot')
from system.mainpage import mainpage
from system.catalog import catalog
from system.bot import bot

def router(SITE):
    print('SYSTEM - router')
    auth = 0

    if (auth != 1):
        # Если нет авторизации
        # if (SITE.request.method == 'POST' and SITE == 'login'):
            # print ('Проверка логина / пароля')
        # else:
            # print ('Редирект на страницу SYSTEM')

        # Вызов функций по ключу
        functions = {
            '': mainpage.mainpage,
            'catalog': catalog.catalog,
            'bot': bot.bot,
            # 'users': users,
            # 'help': help
        }

        if (SITE.p[0] not in functions):
            # Если функция не существует - 404
            raise web.HTTPNotFound()

        # Вызов функции
        return functions[SITE.p[0]](SITE)
