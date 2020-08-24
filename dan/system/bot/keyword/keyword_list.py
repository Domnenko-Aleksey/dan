from system.bot.classes.Keyword import Keyword

def keyword_list(SITE):
    print('FUNCTION -> system/bot/keyword/keyword_list')
    SITE.addHeadFile('/templates/system/bot/keyword_list.css')

    KW = Keyword(SITE)
    keywords = KW.keywordList()

    tr = ''
    if (keywords):
        i = 1
        for keyword in keywords:
            tr +=  f'''<tr>
                <td>{ i }</td>
                <td><a href="/system/bot/keyword/edit/{ keyword['id'] }">{ keyword['name'] }</a></td>
                <td>
                    <a href="/system/bot/keyword/delete/{ keyword['id'] }">
                        <svg class="catalog_char_delete"><use xlink:href="/templates/system/svg/sprite.svg#delete"></use></svg>
                    </a>
                </td>
            </tr>'''


    SITE.content += f'''<div class="bg_gray">
        <h1>Keyword list</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/cat">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>Keyword</span>
        </div>
        <div class="flex_row_start">
            <a href="/system/bot/keyword/add" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#paper_add"></use></svg>
                <div class="ico_rectangle_text">Добавить keyword</div>
            </a>
            <a href="/system/section/help" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#help"></use></svg>
                <div class="ico_rectangle_text">Помощь</div>
            </a>
        </div>
        <div>
            <table class="admin_table">{ tr }</table>
        </div>
    </div>
    '''
