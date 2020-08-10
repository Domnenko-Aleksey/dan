<?php
defined('AUTH') or die('Restricted access');

// Общие настройки
$settings_array['catalog_image_small_resize_method'] = 1;  // Метод ресайза для малых изображений
$settings_array['catalog_image_small_w'] = '240';  // Ширина малого изображения 
$settings_array['catalog_image_small_h'] = '180';  // Высота малого изображения
$settings_array['catalog_image_big_w'] = '1000';  // Максимальная ширина большого изображения 
$settings_array['catalog_image_big_h'] = '800';  // Максимальная высота большого изображения
$settings_array['catalog_3d_model'] = '0';  // Отображать интерфейс для 3D моделей
$settings_array['catalog_3d_sprite'] = '0';  // Отображать интерфейс для 3D спрайта
$settings_array['catalog_360'] = '0';  // Отображать интерфейс для панорамы 360 градусов

// Раздел
$settings_array['section_display_type'] = 'image';  // image / text - тип отображения раздела - изображение и текст / только текст
$settings_array['section_preview_w'] = '200';  // Ширина превьюшки раздела
$settings_array['section_preview_h'] = '200';  // Высота превьюшки раздела
$settings_array['section_quantity_item'] = '100';  // Количество элементов на странице
$settings_array['section_product_card'] = '1';  // Тип карточки элемента в разделе
$settings_array['section_sorting'] = 0;  // Сортировка элементов в разделе
$settings_array['section_sub_display'] = '1';  // 1 / 0 - отображать подразделы
$settings_array['section_sub_items_display'] = '1';  // 1 / 0 - отображать товары из вложенных разделов
$settings_array['section_grouping'] = '0';  // 0 / 1 - товары группируются по одинаковому идентификатору группы.

// Элементы
$settings_array['item_product_card'] = '';  // Тип карточки элемента
$settings_array['item_question'] = '';  // Задать вопрос по товару

// Для интернет - магазина
$settings_array['shop_name'] = '';  // Название каталога (название магазина для Яндекс-Маркета)
$settings_array['shop_company_name'] = '';  // Название компании (используется для Яндекс-Маркета)
$settings_array['shop_delivery'] = '';  // Условия доставки (для интернет магазина, для Яндекс-Маркета)
$settings_array['shop_currency'] = 'руб.';  // Валюта
$settings_array['shop_inner_course_ue'] = '';  // Внутренний курс у.е.
$settings_array['shop_buy_1_click'] = '';  // Купить в 1 клик
$settings_array['shop_quantity_accounting'] = '1';  // 1 - учитывать / 0 - не учитывать - учёт количества
$settings_array['shop_packaging'] = '1';  // 1 - включено / 0 - выключено - включить единицу учёта товара (количество в упаковке)
$settings_array['shop_basket_type'] = 'fly';  // fly - летающая / normal - обычная
$settings_array['shop_price_type'] = '1';  // Тип цен поумолчанию 
$settings_array['shop_1c_psw'] = 'testtest';  // Тип цен поумолчанию
$settings_array['shop_1c_db_reset'] = '1';  // Стирать базу данных
$settings_array['shop_1с_quantity_only'] = '1';  // При загрузки из 1С - обновляется только количество товаров.



?>