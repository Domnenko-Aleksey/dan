import sys
sys.path.append('classes')
from classes import Catalog

def catalog_item(SITE, id):
    print('PATH -> /index/modules/catalog_item.py')
    SITE.addHeadFile('/lib/DAN/DAN.css')
    SITE.addHeadFile('/lib/DAN/DAN.js')
    SITE.addHeadFile('/templates/index/modules/catalog_item/catalog_item.css')

    item_id = SITE.p[2]

    CATALOG = Catalog.Catalog(SITE)
    item = CATALOG.getItem(item_id)
    catalog_id = CATALOG.getCatalogIdBySectionId(item['section_id'])

    # Изображения
    if item['image'] != '':
        image_list = item['image'].split(';')
        image_name = image_list[0].replace('.jpg', '_.jpg')
        image = '<img class="show" src="/media/catalog/' + str(catalog_id) + '/items/' + image_name + '">'

        images_more = ''
        i=0
        for img in image_list:
            if i > 0:
                images_more += '<img class="show" src="/media/catalog/' + str(catalog_id) + '/items/' + img + '">'
            i += 1
        if len(image_list) > 0:
            images_more_script = '<script>DAN.show("show", "mod_catalog_item_left")</script>'
        else:
            images_more_script = ''
    else:
        image = images_more = images_more_script = ''

    # Характеристики
    if 'chars' in item:
        c_out = ''
        chars = item['chars']
        for char_name in chars:  # char_name = ключ словаря chars
            value_str = ', '.join(chars[char_name]['values'])
            c_out += '<div>' + char_name + ': ' + '<b>' + value_str + '</b> ' + chars[char_name]['unit'] + '</div>'
        chars_out = '<div class="mod_catalog_item_chars">' + c_out + '</div>'
    else:
        chars_out = ''

    # Вывод
    out =   '<div class="mod_catalog_item_container flex_row">'
    out +=      '<div id="mod_catalog_item_left" class="mod_catalog_item_left">'
    out +=          '<div class="mod_catalog_item_title">' + item['name'] + '</div>'
    out +=          image
    out +=          '<div class="mod_catalog_item_images_more">' + images_more + '</div>'
    out +=          images_more_script 
    out +=          '<div class="mod_catalog_item_text">' + item['text'] + '</div>'
    out +=      '</div>'
    out +=      '<div class="mod_catalog_item_right">'
    out +=          chars_out
    out +=      '</div>'
    out +=  '</div>'

    return out