import jinja2
import aiohttp_jinja2
from aiohttp import web
import pymysql
import pymysql.cursors
import sys
sys.path.append('classes')
sys.path.append('system')
sys.path.append('index')
from Site import Site
from index import index
from system import system


@aiohttp_jinja2.template('index/index.html')
async def index_r(request):
    # Основной режим вывода содержимого
    SITE = site(request)
    print('******* INDEX *****************************')

    # request.post() - вся полезная нагрузка считывается в память, что приводит к возможным ошибкам OOM. 
    # Чтобы избежать этого, для составных загрузок вы должны использовать Request.multipart()
    if 'file_upload_ajax' in SITE.p:
        
        reader = await request.multipart()

        # reader.next() will `yield` the fields of your form

        SITE.post = {}
        SITE.file = {}

        with await reader.next() as field:
            print('FIELD NAME', field.name)


        '''
        field = await reader.next()
        assert field.name == 'id'
        SITE.post[field.name] = await field.read(decode=True)

        field = await reader.next()
        assert field.name == 'image'
        filename = field.filename

        SITE.file[field.name] = {'filename': filename, 'field': field}

        # You cannot rely on Content-Length if transfer is chunked.
        size = 0
        with open('tmp/file.tmp', 'wb') as f:
            while True:
                chunk = await field.read_chunk()  # 8192 bytes by default.
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)
        '''







    else:
        SITE.post = await request.post()  # Ждём получение данных методом POST
















        

    r = index.router(SITE)

    # Обработка редиректа
    if r and 'redirect' in r:
        return web.HTTPFound(r['redirect'])

    # Обработка ajax
    if r and 'ajax' in r:
        return web.HTTPOk(text=r['ajax'])

    auth = 1
    return {'AUTH': auth, 'content': SITE.content, 'head': SITE.getHead(), 'test_1': 'TEST 1', 'test_2': 'TEST 2'}

async def ws(request):
    # Веб-сокеты
    pass


@aiohttp_jinja2.template('system/main.html')
async def system_r(request):
    # Админка
    SITE = site(request)
    print('******* SYSTEM *****************************')

    SITE.post = await request.post()  # Ждём получение файлов методом POST
    r = system.router(SITE)

    # Обработка редиректа
    if r and 'redirect' in r:
        return web.HTTPFound(r['redirect'])
    
    # Обработка ajax
    if r and 'ajax' in r:
        return web.HTTPOk(text=r['ajax'])

    auth = 1
    return {'AUTH': auth, 'content': SITE.content, 'head': SITE.getHead()}


async def edit(request):
    # Режим визуального редактирования
    path = request.match_info.get('url', "Anonymous")
    print(request)
    text = 'EDIT - Путь: ' + REQ['path'] + ' Метод:' + REQ['method']
    return web.Response(text=text)


def site(request):
    con = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='dan_py',
        charset='utf8mb4',
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )
    SITE = Site()
    SITE.db = con.cursor()
    path = request.match_info.get('url', '')
    SITE.path = path
    SITE.p = path.split('/')
    i = len(SITE.p)
    while i < 7:
        SITE.p.append('')
        i += 1
    SITE.request = request

    return SITE




app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
app.add_routes([web.static('/plugins', 'plugins'),
                web.static('/lib', 'lib'),
                web.static('/templates', 'templates'),
                web.static('/media', 'media'),
                web.get('/ws', ws),  # Веб-сокеты
                web.get('/edit/{url:.*}', edit),  # Режим визуального редактирования
                web.get('/system/{url:.*}', system_r),  # Админка
                web.post('/system/{url:.*}', system_r),  # Админка
                web.get('/{url:.*}', index_r),
                web.post('/{url:.*}', index_r)])

if __name__ == '__main__':
    web.run_app(app)