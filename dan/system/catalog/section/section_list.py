from classes.Catalog import Catalog
from classes.Section import Section
import sys
sys.path.append('system/catalog/classes')

def section_list(SITE):
    print('FUNCTION -> system-> calalog -> section -> list')

    SITE.addHeadFile('/templates/system/css/style.css')
    section_id = SITE.p[2]

    CATALOG = Catalog(SITE)
    SECTION = Section(SITE)
    section = SECTION.getSection(section_id)
    catalog = CATALOG.getItem(section['catalog_id'])

    # Breadcrumbs
    data = {}
    data['catalog_id'] = catalog['id']
    data['parent_id'] = section['parent_id']
    breadcrubmps_list = SECTION.breadcrumbsPath(data)[::-1]

    breadcrumbs = ''

    if (len(breadcrubmps_list) > 0):
        for i in breadcrubmps_list:
            breadcrumbs += '<svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>'
            breadcrumbs += '<a href="/system/catalog/section/' + str(i['id']) + '">' + i['name'] + '</a>'

    rows = SECTION.getItems(section_id)

    row_out = ''
    if (rows):
        i = 1
        for row in rows:
            status_tr_class = ''
            if row['status'] == 0:
                status_tr_class = 'class="admin_table_tr_unpub"'

            row_out +=  f'''<tr { status_tr_class }>
                <td>{ i }</td>
                <td>
                    <div class="flex_row contextmenu_wrap">
                        <svg class="contextmenu_ico" title="Действия" data-id="{ row['id'] }">
                            <use xlink:href="/templates/system/svg/sprite.svg#menu_3"></use>
                        </svg>
                    </div>
                </td>
                <td><a href="/system/catalog/item/edit/{ row['id'] }">{ row['name'] }</a></td>
            </tr>'''
            i += 1

    SITE.content += f'''<div class="bg_gray">
        <script>window.addEventListener("DOMContentLoaded", function(){{
        var contextmenu_item = [
            ["system/catalog/item/edit", "contextmenu_edit", "Редактировать элемент"],
            ["system/catalog/item/up", "contextmenu_up", "Вверх"],
            ["system/catalog/item/down", "contextmenu_down", "Вниз"],
            ["system/catalog/item/pub", "contextmenu_pub", "Опубликовать"],
            ["system/catalog/item/unpub", "contextmenu_unpub", "Скрыть"],
            ["system/catalog/item/delete", "contextmenu_delete", "Удалить элемент"]
        ];
        CONTEXTMENU.add("contextmenu_ico", contextmenu_item, "left");
        }})</script>
        <h1>Элементы раздела { section['name'] }</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/cat">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
			<a href="/system/catalog/cat/{ catalog['id'] }">{ catalog['name'] }</a>
            { breadcrumbs }
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>{ section['name'] }</span>
        </div>
        <div class="flex_row_start">
            <a href="/system/catalog/item/add/{ section_id }" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#paper_add"></use></svg>
                <div class="ico_rectangle_text">Добавить элемент</div>
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
            { row_out }
        </table>
    </div>
    '''