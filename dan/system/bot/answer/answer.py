def answer(SITE):
    print('FUNCTION -> system/bot/answer')

    SITE.content += f'''<div class="bg_gray">
        <h1>BOT -> ANSWER</h1>
        <div class="breadcrumbs">
            <span><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></span> 
        </div>
        <div class="flex_row_start">
            <a href="/system/catalog/cat/add" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#folder_add"></use></svg>
                <div class="ico_rectangle_text">Добавить каталог</div>
            </a>
            <a href="/system/catalod/help" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#help"></use></svg>
                <div class="ico_rectangle_text">Помощь</div>
            </a>
        </div>
        <div class="flex_row_start">
            <a href="/system/catalog/cat" class="ico_square_container">
                <div><svg><use xlink:href="/templates/system/svg/sprite.svg#folder_add"></use></svg></div>
                <div class="ico_square_text">Каталог</div>
            </a>
            <a href="/system/bot" class="ico_square_container">
                <div><svg><use xlink:href="/templates/system/svg/sprite.svg#bot"></use></svg></div>
                <div class="ico_square_text">Бот</div>
            </a>
        </div>
    </div>
    '''
