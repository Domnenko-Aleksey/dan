from classes.Section import Section
from classes.Catalog import Catalog
import sys
sys.path.append('system/catalog/classes')


def section_edit(SITE):
    print('PATH -> system/catalog/section/edit')
    SITE.addHeadFile('/plugins/ckeditor/ckeditor.js')

    CATALOG = Catalog(SITE)
    SECTION = Section(SITE)

    if SITE.p[2] == 'edit':
        section = SECTION.getSection(SITE.p[3])
        catalog_id = section['catalog_id']
        catalog = CATALOG.getItem(catalog_id)
        title = 'Редактировать раздел'
        action = 'update/' + SITE.p[3]
    else:
        catalog_id = SITE.p[3]
        catalog = CATALOG.getItem(catalog_id)
        title = 'Добавить  раздел'
        action = 'insert'
        # ordering = SECTION.getMaxOrdering() + 1
        ordering = 1
        section = {'id': 0, 'parent_id': 0, 'name': '', 'text': '', 'data': '', 'status': 1, 'ordering': ordering}

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
						<input class="input" name="name" placeholder="Раздел 1" required value="''' + section['name'] + '''">
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
				<div class="flex_row p_5_20">
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
