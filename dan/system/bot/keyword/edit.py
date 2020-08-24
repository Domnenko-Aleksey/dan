import sys
sys.path.append('system/bot/classes')
from system.bot.classes.Keyword import Keyword


def edit(SITE):
    print('PATH -> system/bot/keyword/edit')

    KW = Keyword(SITE)

    if SITE.p[2] == 'edit':
        kw_id = SITE.p[3]
        kw = KW.get(kw_id)
        title = 'Редактировать keyword'
        action = 'update/' + kw_id
    else:
        title = 'Добавить keyword'
        action = 'insert'
        kw = {'id': 0, 'keyword': ''}

    SITE.content += '''<div class="bg_gray">
        <h1>''' + title + '''</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/cat">Бот</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>''' + title + '''</span>
        </div>
        <form method="post" action="/system/bot/keyword/''' + action + '''">
			<div class="tc_container">
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Keyword</div>
					<div class="tc_item_r flex_grow">
						<input class="input input_long" name="keyword" required value="''' + kw['keyword'] + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="Сохранить"></div>
					<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>
				</div>
			</div>
		</form>
    </div>
    '''
