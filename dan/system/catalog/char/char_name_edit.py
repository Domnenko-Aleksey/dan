from classes.Catalog import Catalog
from classes.Char import Char
import sys
sys.path.append('system/catalog/classes')


def char_name_edit(SITE):
    print('PATH -> system/catalog/char/edit')

    CATALOG = Catalog(SITE)
    CHAR = Char(SITE)

    if SITE.p[2] == 'edit':
        char_id = SITE.p[3]
        char = CHAR.getName(char_id)
        catalog_id = char['catalog_id']
        title = 'Редактировать характеристику'
        action = 'update/' + char_id
    else:
        catalog_id = SITE.p[3]
        title = 'Добавить  характеристику'
        action = 'insert'
        ordering = CHAR.getNameMaxOrdering(catalog_id) + 1
        char = {'id': 0, 'name': '', 'unit': '', 'type': 'string', 'ordering': ordering}


    catalog = CATALOG.getItem(catalog_id)
    char_type_select = {'string': '', 'number': '', 'date': '', 'color': ''}
    char_type_select[char['type']] = 'selected';

    SITE.content += '''<div class="bg_gray">
        <h1>''' + title + '''</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/cat">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>''' + title + '''</span>
        </div>
        <form method="post" action="/system/catalog/char/''' + action + '''">
			<div class="tc_container">
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Наименование</div>
					<div class="tc_item_r flex_grow">
						<input class="input input_long" name="name" required value="''' + char['name'] + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
                    <div class="tc_item_l">Единица измерения</div>
                    <div class="tc_item_r flex_grow"> 
					    <input class="input" name="unit" value="''' + char['unit'] + '''">
                    </div>
				</div>
                <div class="flex_row p_5_20">
      				<div class="tc_item_l">Тип</div>
					<div class="tc_item_r flex_grow">          
					    <select class="input" name="type">
                            <option value="string" ''' + char_type_select['string'] + '''>Строка</option>
                            <option value="number" ''' + char_type_select['number'] + '''>Число</option>
                            <option value="date" ''' + char_type_select['date'] + '''>Дата</option>
                            <option value="color" ''' + char_type_select['color'] + '''>Цвет</option>
                        </select>
                    </div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Порядок следования</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="ordering" type="number" value="''' + str(char['ordering']) + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="Сохранить"></div>
					<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>
				</div>
			</div>
            <input class="input" name="catalog_id" type="hidden" value="''' + str(catalog_id) + '''">
		</form>
    </div>
    '''
