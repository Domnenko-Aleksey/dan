import sys
sys.path.append('system/catalog/classes')
from Catalog import Catalog
from system.catalog.classes.Section import Section
from system.catalog.classes.Filter import Filter


def edit(SITE):
    print('PATH -> system/catalog/section/edit')
    SITE.addHeadFile('/plugins/ckeditor/ckeditor.js')
    SITE.addHeadFile('/lib/DAN/tooltip/tooltip.css')

    CATALOG = Catalog(SITE)
    SECTION = Section(SITE)
    FILTER = Filter(SITE)

    if SITE.p[2] == 'edit':
        SITE.addHeadFile('/lib/DRAG_N_DROP/DRAG_DROP.css')
        SITE.addHeadFile('/lib/DRAG_N_DROP/DRAG_DROP.js')
        SITE.addHeadFile('/templates/system/catalog/section/edit.js')
        SITE.addHeadFile('/templates/system/catalog/section/edit.css')
        section = SECTION.getSection(SITE.p[3])
        catalog_id = section['catalog_id']
        catalog = CATALOG.getItem(catalog_id)
        title = 'Редактировать раздел'
        action = 'update/' + SITE.p[3]
        filters = FILTER.getFiltersBySectionId(section['id'])
    else:
        catalog_id = SITE.p[3]
        catalog = CATALOG.getItem(catalog_id)
        title = 'Добавить  раздел'
        action = 'insert'
        # ordering = SECTION.getMaxOrdering() + 1
        ordering = 1
        section = {'id': 0, 'parent_id': 0, 'name': '', 'text': '', 'data': '', 'status': 1, 'ordering': ordering}
        filters = ''

    rows = SECTION.tree(catalog_id)
    sec_options = ''
    tabu_level = 1000  # Уровень, ниже которого опускаться нельзя для дочерних пунктов нашего раздела
    if (rows):
        for row in rows:

            if row['id'] == section['id']:
                # Если это текущий раздел, не отображать его и дочерние разделы
                tabu_level = row['level']
                continue
            
            if row['level'] <= tabu_level:
                # Вышли из дочерних разделов текущего раздела - всё сбрасываем
                tabu_level = 1000
                level = '&nbsp;-&nbsp;' * row['level']
                selected = 'selected' if row['id'] == section['parent_id'] else ''
                sec_options += f'''<option { selected } value="{ row['id'] }">{ level }{ row['name'] }</option>'''

    filters_out = ''

    if filters:
        for filter in filters:
            if filter['type'] == 'number':
                type_out =  '<td class="section_filter_tab_type">число</td>'
                type_out += '<td class="section_filter_tab_value">'
                type_out +=     '<input draggable="false" class="input section_filter_input_number" type="text" name="filter_value_1[]" value="' + filter['value_1'] + '">'
                type_out +=     '<input draggable="false" class="input section_filter_input_number" type="text" name="filter_value_2[]" value="' + filter['value_2'] + '">'
                type_out += '</td>'       

            if filter['type'] == 'string':
                type_out =  '<td class="section_filter_tab_type">строка</td>'
                type_out += '<td class="section_filter_tab_value">'
                type_out +=     '<input draggable="false" class="input section_filter_input_string" type="text" name="filter_value_1[]" value="' + filter['value_1'] + '">'
                type_out +=     '<input class="input section_filter_input_string" type="hidden" name="filter_value_2[]" value="">'
                type_out += '</td>'

            filters_out +=   '<table class="section_filter_tab" draggable="true" data-id="' + str(filter['id']) + '" data-char_name_id="' + str(filter['name_id']) + '">'
            filters_out +=      '<tr>'
            filters_out +=          '<td class="section_filter_tab_ico_dnd">'
            filters_out +=              '<div class="flex_row contextmenu_wrap">'
            filters_out +=                  '<svg class="drag_drop_ico" title="Перетащить" data-id="' + str(filter['name_id']) + '" data-target-id="section_filter_list" data-class="section_filter_tab" data-direction="y" data-f="SYSTEM.catalog.section.filter_ordering">'
            filters_out +=                  '<use xlink:href="/templates/system/svg/sprite.svg#cursor24"></use></svg>'
            filters_out +=              '</div>'
            filters_out +=          '</td>'
            filters_out +=          '<td class="section_filter_tab_name">'
            filters_out +=              filter['name'] + ' (' + filter['name'] + ')'
            filters_out +=              '<input type="hidden" name="filter_id[]" value="' + str(filter['id']) + '">'
            filters_out +=              '<input type="hidden" name="filter_char_id[]" value="' + str(filter['name_id']) + '">'
            filters_out +=          '</td>'
            filters_out +=          type_out
            filters_out +=          '<td class="section_filter_tab_delete">'
            filters_out +=              '<svg class="section_filter_delete" data-id="' + str(filter['id']) + '"><use xlink:href="/templates/system/svg/sprite.svg#delete"></use></svg>'
            filters_out +=          '</td>'
            filters_out +=      '</tr>'
            filters_out +=  '</table>'


    SITE.content += '''<div class="bg_gray">
        <h1>''' + title + '''</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/cat">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
			<a href="/system/catalog/cat/''' + str(catalog_id) + '''">''' + catalog['name'] + '''</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>''' + title + '''</span>
        </div>
		<form method="post" action="/system/catalog/section/''' + action + '''">
			<div class="tc_container">
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Наименование</div>
					<div class="tc_item_r flex_grow">
						<input class="input input_long" name="name" placeholder="Раздел 1" required value="''' + section['name'] + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Родительский раздел</div>
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
					    <textarea id="editor1" name="text">''' + section['text'] + '''</textarea>
                    </div>
				</div>
                <div class="flex_row p_5_20">
      				<div class="tc_item_l">Данные</div>
					<div class="tc_item_r flex_grow">          
					    <textarea class="input" name="data" style="width:100%;height:100px;">''' + section['data'] + '''</textarea>
                    </div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Статус</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="status" type="number" value="''' + str(section['status']) + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Порядок следования</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="ordering" type="number" value="''' + str(section['ordering']) + '''">
					</div>
				</div>
                <div class="flex_row accordion_container">
                    <div class="dan_accordion_container">
                        <input class="dan_accordion_checkbox" type="checkbox">
                        <div class="dan_accordion_head">
                            <svg class="icon"><use xlink:href="/templates/system/svg/sprite.svg#filter"></use></svg>
                            <div class="dan_accordion_head_indicator"></div>
                            <div class="dan_accordion_head_title">ФИЛЬТРЫ ПО ХАРАКТЕРИСТИКАМ</div>
                        </div>
                        <div class="dan_accordion_content">
                            <div class="section_filter_button_wrap">
                                <div id="section_filter_add" class="section_filter_add_button" data-catalog_id="''' + str(catalog_id) + '''">Добавить фильтр</div>
                            </div>
                            <div>
                                <table class="section_filter_title_tab">
                                    <tr>
                                        <td class="section_filter_tab_ico_dnd">&nbsp;</td>
                                        <td class="section_filter_tab_name">
                                            <div class="section_filter_column_title"><b>Фильтр по хар-ке</b></div>
                                            <div class="tooltip">
                                                <em>Фильтры</em>
                                                <p>Позволяют фильтровать товары по характеристикам, примеры:</p>
                                                <b>Цвет: </b>
                                                <select class="input" size="1" name="D1">
                                                    <option value="Характеристика 1">белый</option>
                                                    <option value="Характеристика 2">синий</option>
                                                    <option value="Характеристика 3">красный</option>
                                                </select>
                                                <br>
                                                <b>Длина: </b><input class="input" type="text" name="T1" size="5" value="80">см.&nbsp;
                                                до <input class="input" type="text" name="T2" size="5" value="120">см.
                                                <br>
                                            </div>
                                        </td>
                                        <td class="section_filter_tab_type"><b>Тип</b></td>
                                        <td class="section_filter_tab_value">
                                            <div class="section_filter_column_title"><b>Значения полей фильтра</b></div>
                                            <div class="tooltip">
                                                <em>Значение полей фильтра</em>
                                                <p>Для типа данных <i>строка</i> вводите значения фильтра  через точку с запятой, например: <b>белый;синий;красный</b></p>
                                                <p>&nbsp;</p>
                                                <p>Для типа данных <i>число</i> введите значения фильтра  <b>от</b> <i>число</i> <b>до</b> <i>число</i></p>
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                            <div id="section_filter_list" data-id="">''' + filters_out + '''.</div>
                        </div>
                    </div>
                </div>
				<div class="flex_row p_40_20">
					<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="Сохранить"></div>
					<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>
				</div>
			</div>
            <input class="input" name="catalog_id" type="hidden" value="''' + str(catalog_id) + '''">
            <script type="text/javascript">
                CKEDITOR.replace( 'editor1', {
                    height: '400px',
                    filebrowserBrowseUrl : '/system/plugins/filemanager'
                });
            </script>
		</form>
    </div>
    '''
