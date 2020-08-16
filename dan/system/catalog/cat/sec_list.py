import sys
sys.path.append('system/catalog/classes')
from system.catalog.classes.Catalog import Catalog
from system.catalog.classes.Section import Section

def sec_list(SITE):
    print('FUNCTION -> system_> calalog -> cat -> sec_list')
    catalog_id = SITE.p[2]

    SITE.addHeadFile('/templates/system/catalog/cat/sec.js')
    CATALOG = Catalog(SITE)
    catalog = CATALOG.getItem(catalog_id)
    SECTION = Section(SITE)

    rows = SECTION.tree(catalog_id)
    row_out = ''
    i = 1
    if (rows):
        for row in rows:
            level = '&nbsp;-&nbsp;' * row['level']
            status_tr_class = ''
            if row['status'] == 0:
                status_tr_class = 'class="admin_table_tr_unpub"' 

            row_out += f'''<tr { status_tr_class }>
                <td>{ i }</td>
                <td>
                    <div class="flex_row contextmenu_wrap">
                        <svg class="contextmenu_ico" title="Действия" data-id="{ row['id'] }">
                            <use xlink:href="/templates/system/svg/sprite.svg#menu_3"></use>
                        </svg>
                    </div>
                </td>
                <td>
                    <a href="/system/catalog/section/{ row['id'] }">{ level }{ row['name'] }</a>
                </td>
            </tr>
            '''
            i += 1

    SITE.content += f'''<div class="bg_gray">
        <script>window.addEventListener("DOMContentLoaded", function(){{
        var contextmenu_catalog = [
            ["system/catalog/section/edit", "contextmenu_edit", "Редактировать раздел"],
            ["system/catalog/section/up", "contextmenu_up", "Вверх"],
            ["system/catalog/section/down", "contextmenu_down", "Вниз"],
            ["system/catalog/section/pub", "contextmenu_pub", "Опубликовать"],
            ["system/catalog/section/unpub", "contextmenu_unpub", "Скрыть"],
            ["#SYSTEM.section.delete_modal", "contextmenu_delete", "Удалить раздел"]
        ];
        CONTEXTMENU.add("contextmenu_ico", contextmenu_catalog, "left");
        }})</script>
        <h1>Разделы каталога { catalog['name'] }</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>{ catalog_id }</span>
        </div>
        <div class="flex_row_start">
            <a href="/system/catalog/section/add/{ catalog_id }" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#folder_add"></use></svg>
                <div class="ico_rectangle_text">Добавить раздел</div>
            </a>
            <a href="/system/catalog/item/add/{ catalog_id }" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#paper_add"></use></svg>
                <div class="ico_rectangle_text">Добавить элемент</div>
            </a>
			<a href="/system/catalog/settings/edit/{ catalog_id }" target="blank" class="ico_rectangle_container">
				<svg><use xlink:href="/templates/system/svg/sprite.svg#gear"></use></svg>
				<div class="ico_rectangle_text">Настройки</div>
			</a>
			<a href="/system/catalog/char/{ catalog_id }" target="blank" class="ico_rectangle_container">
				<svg><use xlink:href="/templates/system/svg/sprite.svg#chars"></use></svg>
				<div class="ico_rectangle_text">Характеристики</div>
			</a>
            <a href="/system/catalog/help" target="blank" class="ico_rectangle_container">
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
            { row_out }
        </table>
    </div>
    '''
