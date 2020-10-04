import sys
sys.path.append('classes')
from classes import Catalog

def catalog_section_items(SITE, section_id):
    print('PATH -> /index/modules/catalog_section_items.py')
    SITE.addHeadFile('/templates/index/modules/catalog_section_items/catalog_section_items.css')

    # Выводить n характеристик || False
    n_chars =3

    CATALOG = Catalog.Catalog(SITE)
    section_id = 1
    items = CATALOG.getSectionItems(section_id, chars=n_chars)
    catalog_id = CATALOG.getCatalogIdBySectionId(section_id)

    out = ''
    for item in items:
        # Изображения
        if item['image'] != '':
            img_list = item['image'].split(';')
            image = '<img src="/media/catalog/' + str(catalog_id) + '/items/' + img_list[0] + '">'
        else:
            image = ''

        # Обрезаем текст
        if len(item['text']) > 100:
            text_100 = item['text'][0:100]
            space_position = text_100.rfind(' ')
            text = text_100[0:space_position] + '...'
        else:
            text = item['text']

        # Характеристики
        if 'chars' in item:
            c_out = ''
            chars = item['chars']
            for char_name in chars:  # char_name = ключ словаря chars
                value_str = ', '.join(chars[char_name]['values'])
                c_out += '<div>' + char_name + ': ' + value_str + ' ' + chars[char_name]['unit'] + '</div>'
            char_out = '<div class="mod_catalog_section_items_chars">' + c_out + '</div>'
        else:
            char_out = ''

        out +=  '<a href="/catalog/item/' + str(item['id']) + '" class="mod_catalog_section_items_container">'
        out +=      image
        out +=      '<div class="mod_catalog_section_items_title">' + item['name'] + '</div>'
        out +=      '<div class="mod_catalog_section_items_text">' + text + '</div>'
        out +=      char_out
        out +=  '</a>'

    return out