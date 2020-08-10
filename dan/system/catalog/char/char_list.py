from classes.Catalog import Catalog
from classes.Char import Char
import sys
sys.path.append('system/catalog/char')

def char_list(SITE):
    print('FUNCTION -> system-> calalog -> char -> list')

    SITE.addHeadFile('/templates/system/css/style.css')
    catalog_id = SITE.p[2]

    CATALOG = Catalog(SITE)
    CHAR = Char(SITE)
    catalog = CATALOG.getItem(catalog_id)
    chars = CHAR.getCharName(catalog_id)

    print(chars)

    char_type = {'string':'строка', 'number':'число', 'date':'дата', 'color':'цвет'}

    char_out = ''
    if (chars):
        i = 1
        for char in chars:
            char_out +=  f'''<table class="drag_drop" data-id="{ char['id'] }">'
				<tr>
					<td>{ char['id'] }</td>
					<td>
						<div class="flex_row contextmenu_wrap"><svg class="drag_drop_ico" title="Перетащить" data-id="{ char['id'] }" data-target-id="drag_target" data-class="drag_drop" data-f="ADMIN.chars.drag_drop"><use xlink:href="/administrator/template/sprite.svg#cursor24"></use></svg></div>
					</td>
					<td><a href="/admin/com/catalog/char/edit/{ char['id'] }">{ char['name'] } { char['unit'] }</a></td>
					<td>{ char_type[char['type']] }</td>
					<td>
						<svg class="catalog_char_delete" data-id="{ char['id'] }"><use xlink:href="/administrator/template/sprite.svg#delete"></use></svg>
					</td>
				</tr>
			</table>'''
    

    SITE.content += f'''<div class="bg_gray">
        <h1>Характеристики</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/cat">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>Характеристики</span>
        </div>
        <div class="flex_row_start">
            <a href="/system/catalog/char/add/{ catalog['id'] }" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#paper_add"></use></svg>
                <div class="ico_rectangle_text">Добавить характеристику</div>
            </a>
            <a href="/system/section/help" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#help"></use></svg>
                <div class="ico_rectangle_text">Помощь</div>
            </a>
        </div>
        <table class="admin_table even_odd">
            <tr>
                <th style="width:50px;">№</th>
                <th style="width:50px;">&nbsp;</th>
                <th>Наменование</th>
            </tr>
            { char_out }
        </table>
    </div>
    '''