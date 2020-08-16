import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Catalog import Catalog


def settings_edit(SITE):
    print('FUNCTION -> system-> calalog -> cat -> settings_edit')
    CATALOG = Catalog(SITE)
    catalog = CATALOG.getItem(SITE.p[3])

    SITE.content += '''<div class="bg_gray">
        <h1>Настройки каталога ''' + catalog['name'] + '''</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>Настройки</span>
        </div>
		<form method="post" action="/system/catalog/cat/settings_update/''' + SITE.p[3] + '''">
			<div class="tc_container">
				<div class="flex_row p_5_20">
					'<textarea class="input" name="settings" style="width:100%; height:200px;">''' + catalog['settings'] + '''</textarea>'
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="Сохранить"></div>
					<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>
				</div>
			</div>
		</form>
    </div>
    '''
