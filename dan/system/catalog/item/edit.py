from system.catalog.classes.Char import Char
from system.catalog.classes.Item import Item
from system.catalog.classes.Section import Section
from system.catalog.classes.Catalog import Catalog
import sys
sys.path.append('system/catalog/classes')


def edit(SITE):
    print('PATH -> system/catalog/item/edit')
    SITE.addHeadFile('/plugins/ckeditor/ckeditor.js')
    SITE.addHeadFile('/lib/DRAG_N_DROP/DRAG_DROP.css')
    SITE.addHeadFile('/lib/DRAG_N_DROP/DRAG_DROP.js')
    SITE.addHeadFile('/templates/system/catalog/item/edit.css')
    SITE.addHeadFile('/templates/system/catalog/item/edit.js')

    CATALOG = Catalog(SITE)
    SECTION = Section(SITE)
    CHAR = Char(SITE)
    ITEM = Item(SITE)

    if SITE.p[2] == 'edit':
        item_id = SITE.p[3]
        item = ITEM.getItem(item_id)
        section_id = item['section_id']
        title = 'Редактировать элемент'
        action = 'update/' + item_id
    else:
        section_id = SITE.p[3]
        title = 'Добавить  элемент'
        action = 'insert'
        ordering = ITEM.getMaxOrdering(section_id) + 1
        item = {'id': 0, 'name': '', 'text': '',
                'data': '', 'status': 1, 'ordering': ordering}

    section = SECTION.getSection(section_id)
    catalog = CATALOG.getItem(section['catalog_id'])
    chars = CHAR.getValuesByItemId(item['id'])

    data = {}
    data['catalog_id'] = catalog['id']
    data['parent_id'] = section['parent_id']
    breadcrubmps_list = SECTION.breadcrumbsPath(data)[::-1]

    breadcrumbs = ''

    if (len(breadcrubmps_list) > 0):
        for i in breadcrubmps_list:
            breadcrumbs += '<svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>'
            breadcrumbs += '<a href="/system/catalog/section/' + str(i['id']) + '">' + i['name'] + '</a>'

    # Обработка характеристик
    chars_out = ''
    if chars:
        for char in chars:
            if char['type'] == 'number':
                type_out =  '<td class="char_tab_type">число</td>'
                type_out += '<td class="char_tab_value">'
                type_out +=     '<input draggable="false" class="input char_input_number" type="text" name="char_value[]" value="' + char['value'] + '"> '
                type_out += '</td>'

            if char['type'] == 'string':
                type_out =  '<td class="char_tab_type">строка</td>'
                type_out += '<td class="char_tab_value">'
                type_out +=     '<input draggable="false" class="input char_input_string" type="text" name="char_value[]" value="' + char['value'] + '">'
                type_out += '</td>'
            
            chars_out += '<table class="char_tab" data-id="' + str(char['id']) + '">'
            chars_out +=    '<tr>'
            chars_out +=        '<td class="char_tab_ico_dnd">'
            chars_out +=            '<div class="flex_row contextmenu_wrap">'
            chars_out +=                '<svg class="drag_drop_ico" title="Перетащить" data-id="' + str(char['name_id']) + '" data-target-id="char_list" data-class="char_tab" data-direction="y" data-f="SYSTEM.catalog.item.char_ordering">'
            chars_out +=                '<use xlink:href="/templates/system/svg/sprite.svg#cursor24"></use></svg>'
            chars_out +=            '</div>'
            chars_out +=        '</td>'
            chars_out +=        '<td class="char_tab_name">'
            chars_out +=            char['name'] + ' (' + char['unit'] + ')'
            chars_out +=            '<input type="hidden" name="char_id[]" value="' + str(char['id']) + '">'
            chars_out +=            '<input type="hidden" name="char_name_id[]" value="' + str(char['name_id']) + '">'
            chars_out +=        '</td>'
            chars_out +=        type_out
            chars_out +=        '<td class="char_tab_delete">'
            chars_out +=            '<svg class="catalog_char_delete" data-id="' + str(char['id']) + '"><use xlink:href="/templates/system/svg/sprite.svg#delete"></use></svg>'
            chars_out +=        '</td>'
            chars_out +=    '</tr>'
            chars_out += '</table>'

    rows = SECTION.tree(catalog['id'])
    sec_options = ''
    # Уровень, ниже которого опускаться нельзя для дочерних пунктов нашего раздела
    tabu_level = 1000
    if (rows):
        for row in rows:
            if row['level'] <= tabu_level:
                level = '&nbsp;-&nbsp;' * row['level']
                selected = 'selected' if row['id'] == section['id'] else ''
                sec_options += f'''<option { selected } value="{ row['id'] }">{ level }{ row['name'] }</option>'''

    SITE.content += '''<div class="bg_gray">
        <h1>''' + title + '''</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/cat">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
			<a href="/system/catalog/cat/''' + str(catalog['id']) + '''">''' + catalog['name'] + '''</a>
            ''' + breadcrumbs + '''
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/section/''' + str(section['id']) + '''">''' + section['name'] + '''</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>''' + title + '''</span>
        </div>
        <form method="post" action="/system/catalog/item/''' + action + '''">
			<div class="tc_container">
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Наименование</div>
					<div class="tc_item_r flex_grow">
						<input class="input input_long" name="name" placeholder="Элемент" required value="''' + item['name'] + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Раздел</div>
					<div class="tc_item_r flex_grow">
						<select class="input" name="parent_id">
                            <option value="0">Нет</option>
                            ''' + sec_options + '''
                        </select>
					</div>
				</div>
				<div class="flex_row p_5_20">
                    <div class="tc_item_l">Текст</div>
                    <div class="tc_item_r flex_grow"> 
					    <textarea id="editor1" name="text">''' + item['text'] + '''</textarea>
                    </div>
				</div>
                <div class="flex_row p_5_20">
      				<div class="tc_item_l">Данные</div>
					<div class="tc_item_r flex_grow">
					    <textarea class="input" name="data" style="width:100%;height:100px;">''' + item['data'] + '''</textarea>
                    </div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Статус</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="status" type="number" value="''' + str(item['status']) + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Порядок следования</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="ordering" type="number" value="''' + str(item['ordering']) + '''">
					</div>
				</div>
                <div class="flex_row accordion_container">
                    <div class="dan_accordion_container">
                        <input class="dan_accordion_checkbox" type="checkbox">
                        <div class="dan_accordion_head">
                            <div class="dan_accordion_head_indicator"></div>
                            <div class="dan_accordion_head_title">ХАРАКТЕРИСТИКИ</div>
                        </div>
                        <div class="dan_accordion_content">
                            <div class="char_button_wrap">
                                <a href="/system/catalog/char/add/''' + str(catalog['id']) + '''" target="blank" class="char_name_add_button" title="Добавить характеристику">+</a>
                                <div id="char_value_add" class="char_value_add_button" data-catalog_id="''' + str(catalog['id']) + '''">Добавить значение</div>
                            </div>
                            <div id="char_list" data-id="''' + str(item['id']) + '''">''' + chars_out + '''</div>
                        </div>
                    </div>
                </div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="Сохранить"></div>
					<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>
				</div>
			</div>
            <input class="input" name="section_id" type="hidden" value="''' + str(section_id) + '''">
            <script type="text/javascript">
                CKEDITOR.replace( 'editor1', {
                    height: '400px',
                    filebrowserBrowseUrl : '/system/plugins/filemanager'
                });
            </script>
		</form>
    </div>
    '''
