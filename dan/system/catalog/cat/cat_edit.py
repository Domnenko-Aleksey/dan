from classes.Catalog import Catalog
import sys
sys.path.append('system/catalog/classes')


def cat_edit(SITE):
    print('FUNCTION -> system_> calalog -> cat -> edit')

    CATALOG = Catalog(SITE)

    if SITE.p[2] == 'edit':
        catalog = CATALOG.getItem(SITE.p[3])
        title = 'Редактировать каталог'
        action = 'update/' + SITE.p[3]
    else:
        title = 'Добавить  каталог'
        action = 'insert'
        ordering = CATALOG.getMaxOrdering() + 1
        catalog = {'name': '', 'url': '', 'ordering': ordering}

    SITE.content += '''<div class="bg_gray">
        <h1>''' + title + '''</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>''' + title + '''</span>
        </div>
		<form method="post" action="/system/catalog/cat/''' + action + '''">
			<div class="tc_container">
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Наименование</div>
					<div class="tc_item_r flex_grow">
						<input class="input input_long" name="name" placeholder="Интернет магазин" required value="''' + catalog['name'] + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">URL адрес каталога</div>
					<div class="tc_item_r flex_grow">
						<input id="url" class="input" name="url" placeholder="catalog" required value="''' + catalog['url'] + '''">
						<div id="url_status"></div>
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Порядок следования</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="ordering" type="number" value="''' + str(catalog['ordering']) + '''">
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
