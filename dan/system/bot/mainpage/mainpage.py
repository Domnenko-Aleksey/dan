import sys


def mainpage(SITE):
    print('FUNCTION -> system/mainpage')

    SITE.content += f'''<div class="bg_gray">
        <h1>Бот</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>Бот</span>
        </div>
        <div class="flex_row_start">
            <a href="/system/bot/keyword/add" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#folder_add"></use></svg>
                <div class="ico_rectangle_text">Добавить keyword</div>
            </a>
            <a href="/system/bot/answer/add" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#folder_add"></use></svg>
                <div class="ico_rectangle_text">Добавить ответ</div>
            </a>
            <a href="/system/catalod/help" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#help"></use></svg>
                <div class="ico_rectangle_text">Помощь</div>
            </a>
        </div>
        <div class="flex_row_start">
            <a href="/system/bot/keyword" class="ico_square_container">
                <div><svg><use xlink:href="/templates/system/svg/sprite.svg#question"></use></svg></div>
                <div class="ico_square_text">Keywords</div>
            </a>
            <a href="/system/bot/answer" class="ico_square_container">
                <div><svg><use xlink:href="/templates/system/svg/sprite.svg#info"></use></svg></div>
                <div class="ico_square_text">Ответы</div>
            </a>
        </div>
    </div>
    '''
