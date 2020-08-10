<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
$SITE->headAddFile('/components/catalog/admin/cat/js/settings.js');
$SITE->headAddFile('/components/catalog/admin/cat/css/style.css');

$id = $SITE->d[5];
$cat = new AdminCatalogCat();
$catalog = $cat->getItem($id, true);

$settings = unserialize($catalog['settings']);

// Каталог
$catalog_pub_checked = $catalog['enabled'] == 1 ? 'checked' : '';
$catalog_image_small_resize_method = array_fill(1, 3, '');
$catalog_image_small_resize_method[$settings['catalog_image_small_resize_method']] = 'checked';
$catalog_3d_model_checked = $settings['catalog_3d_model'] == 1 ? 'checked' : '';
$catalog_3d_sprite_checked = $settings['catalog_3d_sprite'] == 1 ? 'checked' : '';
$catalog_360_checked = $settings['catalog_360'] == 1 ? 'checked' : '';

// Раздел
$section_display_type['image'] = $section_display_type['text'] = '';
$section_display_type[$settings['section_display_type']] = 'checked';
$section_sorting = array_fill(0, 7, '');
$section_sorting[$settings['section_sorting']] = 'selected';
$section_sub_display_checked = $settings['section_sub_display'] == 1 ? 'checked' : '';
$section_sub_items_display_checked = $settings['section_sub_items_display'] == 1 ? 'checked' : '';
$section_grouping_checked = $settings['section_grouping'] == 1 ? 'checked' : '';

// Элементы
$item_question_checked = $settings['item_question'] == 1 ? 'checked' : '';

if (isset($settings['shop'])) {
	$shop_on_checked = 'checked';
	$shop_display_style = '';
} else {
	$shop_on_checked = '';
	$shop_display_style = 'style="display:none;"';
}

$shop_buy_1_click_checked = $settings['shop_buy_1_click'] == 1 ? 'checked' : '';
$shop_quantity_accounting_checked = $settings['shop_quantity_accounting'] == 1 ? 'checked' : '';
$shop_packaging_checked = $settings['shop_packaging'] == 1 ? 'checked' : '';
$shop_basket_type['fly'] = $shop_basket_type['normal'] = '';
$shop_basket_type[$settings['shop_basket_type']] = 'selected';
$shop_1c_db_reset_checked = $settings['shop_1c_db_reset'] == 1 ? 'checked' : '';
$shop_1с_quantity_only_checked = $settings['shop_1с_quantity_only'] == 1 ? 'checked' : '';

$SITE->content =
	'<div class="bg_gray">'.
		'<h1>Настройки каталога</h1>'.
		'<form method="POST" action="/admin/com/catalog/cat/settings_update/'.$id.'">'.
			'<div class="dan_accordion_container">'.
				'<input class="dan_accordion_checkbox" type="checkbox">'.
				'<div class="dan_accordion_head">'.
					'<svg class="icon"><use xlink:href="/administrator/template/sprite.svg#gear"></use></svg>'.
					'<div class="dan_accordion_head_indicator"></div>'.
					'<div>ОБЩИЕ НАСТРОЙКИ</div>'.
				'</div>'.
				'<div class="dan_accordion_content">'.
					'<table class="admin_table even_odd">'.
						'<tr>'.
							'<td class="admin_table_td_num">1</td>'.
							'<td class="admin_table_td_name">Опубликовать каталог</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="catalog_enabled" name="enabled" type="checkbox" class="input" value="1" '.$catalog_pub_checked.'>'.
								'<label for="catalog_enabled"></label>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">2</td>'.
							'<td class="admin_table_td_name">Метод ресайза для малых изображений</td>'.
							'<td class="admin_table_td_input">'.
								'<div class="lineheight30">'.
									'<input id="small_resize_method_1" class="input" type="radio" value="1" name="catalog_image_small_resize_method" '.$catalog_image_small_resize_method[1].'>'.
									'<label for="small_resize_method_1"></label><span>умный ресайз <i>(вставка по большей стороне)</i></span>'.
								'</div>'.
								'<div class="lineheight30">'.
									'<input id="small_resize_method_2" class="input" type="radio" value="2" name="catalog_image_small_resize_method" '.$catalog_image_small_resize_method[2].'>'.
									'<label for="small_resize_method_2"></label><span>подрезка <i>(подрезка большей стороны)</i></span>'.
								'</div>'.
								'<div class="lineheight30">'.
									'<input id="small_resize_method_3" class="input" type="radio" value="3" name="catalog_image_small_resize_method" '.$catalog_image_small_resize_method[3].'>'.
									'<label for="small_resize_method_3"></label><span>скукожить <i>(смять, пропорции игнорируются)</i></span>'.
								'</div>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">3</td>'.
							'<td class="admin_table_td_name">Размер малого изображения</td>'.
							'<td class="admin_table_td_input">'.
								'по ширине: <input name="catalog_image_small_w" type="number" size="3" min="50" max="500" class="input" value="'.$settings['catalog_image_small_w'].'"> px &nbsp;&nbsp; '.
								'по высоте: <input name="catalog_image_small_h" type="number" size="3" min="50" max="500" class="input" value="'.$settings['catalog_image_small_h'].'"> px'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">4</td>'.
							'<td class="admin_table_td_name">Максимальный размер большого изображения</td>'.
							'<td class="admin_table_td_input">'.
								'по ширине: <input name="catalog_image_big_w" type="number" size="3" min="400" max="2000" class="input" value="'.$settings['catalog_image_big_w'].'"> px &nbsp;&nbsp; '.
								'по высоте: <input name="catalog_image_big_h" type="number" size="3" min="400" max="2000" class="input" value="'.$settings['catalog_image_big_h'].'"> px'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">5</td>'.
							'<td class="admin_table_td_name">Отображать интерфейс для 3D моделей</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="catalog_3d_model" name="catalog_3d_model" type="checkbox" class="input" value="1" '.$catalog_3d_model_checked.'>'.
								'<label for="catalog_3d_model"></label>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">6</td>'.
							'<td class="admin_table_td_name">Отображать интерфейс для 3D спрайта</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="catalog_3d_sprite" name="catalog_3d_sprite" type="checkbox" class="input" value="1" '.$catalog_3d_sprite_checked.'>'.
								'<label for="catalog_3d_sprite"></label>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">7</td>'.
							'<td class="admin_table_td_name">Отображать интерфейс для панорамы 360 градусов</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="catalog_360" name="catalog_360" type="checkbox" class="input" value="1" '.$catalog_360_checked.'>'.
								'<label for="catalog_360"></label>'.
							'</td>'.
						'</tr>'.
					'</table>'.
				'</div>'.
			'</div>'.
			'<div class="dan_accordion_container">'.
				'<input class="dan_accordion_checkbox" type="checkbox">'.
				'<div class="dan_accordion_head">'.
					'<svg class="icon"><use xlink:href="/administrator/template/sprite.svg#section"></use></svg>'.
					'<div class="dan_accordion_head_indicator"></div>'.
					'<div>РАЗДЕЛ</div>'.
				'</div>'.
				'<div class="dan_accordion_content">'.
					'<table class="admin_table even_odd">'.
						'<tr>'.
							'<td class="admin_table_td_num">1</td>'.
							'<td class="admin_table_td_name">Тип отображения раздела</td>'.
							'<td class="admin_table_td_input">'.
								'<div class="lineheight30">'.
									'<input id="section_display_type_1" class="input" type="radio" value="image" name="section_display_type" '.$section_display_type['image'].'>'.
									'<label for="section_display_type_1"></label><span>изображение и текст</span>'.
								'</div>'.
								'<div class="lineheight30">'.
									'<input id="section_display_type_2" class="input" type="radio" value="text" name="section_display_type" '.$section_display_type['text'].'>'.
									'<label for="section_display_type_2"></label><span>текст</span>'.
								'</div>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">2</td>'.
							'<td class="admin_table_td_name">Размер превью раздела</td>'.
							'<td class="admin_table_td_input">'.
								'по ширине: <input name="section_preview_w" type="number" size="3" min="50" max="500" class="input" value="'.$settings['section_preview_w'].'"> px &nbsp;&nbsp; '.
								'по высоте: <input name="section_preview_h" type="number" size="3" min="50" max="500" class="input" value="'.$settings['section_preview_h'].'"> px'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">3</td>'.
							'<td class="admin_table_td_name">Количество элементов на странице</td>'.
							'<td class="admin_table_td_input">'.
								'<input name="section_quantity_item" type="number" size="3" min="20" max="200" class="input" value="'.$settings['section_quantity_item'].'">'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">4</td>'.
							'<td class="admin_table_td_name">Тип карточки элемента в разделе</td>'.
							'<td class="admin_table_td_input">'.
								'<select class="input" name="section_product_card">'.
									'<option value="1">1</option>'.
								'</select>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">5</td>'.
							'<td class="admin_table_td_name">Сортировка элементов в разделе</td>'.
							'<td class="admin_table_td_input">'.
								'<select class="input" name="section_sorting">'.
									'<option value="0" '.$section_sorting[0].'>Ручная</option>'.
									'<option value="1" '.$section_sorting[1].'>Ручная - в обратном порядке</option>'.
									'<option value="2" '.$section_sorting[2].'>По цене (по возрастанию)</option>'.
									'<option value="3" '.$section_sorting[3].'>По цене (по убыванию)</option>'.
									'<option value="4" '.$section_sorting[4].'>По алфавиту (по возрастанию)</option>'.
									'<option value="5" '.$section_sorting[5].'>По алфавиту (по убыванию)</option>'.
									'<option value="6" '.$section_sorting[6].'>По дате (новые сверху)</option>'.
								'</select>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">6</td>'.
							'<td class="admin_table_td_name">Отображать подразделы</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="section_sub_display" name="section_sub_display" type="checkbox" class="input" value="1" '.$section_sub_display_checked.'>'.
								'<label for="section_sub_display"></label>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">7</td>'.
							'<td class="admin_table_td_name">Отображать товары из вложенных разделов</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="section_sub_items_display" name="section_sub_items_display" type="checkbox" class="input" value="1" '.$section_sub_items_display_checked.'>'.
								'<label for="section_sub_items_display"></label>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">8</td>'.
							'<td class="admin_table_td_name">Группировка (по одинаковому идентификатору группы)</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="section_grouping" name="section_grouping" type="checkbox" class="input" value="1" '.$section_grouping_checked.'>'.
								'<label for="section_grouping"></label>'.
							'</td>'.
						'</tr>'.
					'</table>'.
				'</div>'.
			'</div>'.
			'<div class="dan_accordion_container">'.
				'<input class="dan_accordion_checkbox" type="checkbox">'.
				'<div class="dan_accordion_head">'.
					'<svg class="icon"><use xlink:href="/administrator/template/sprite.svg#pages"></use></svg>'.
					'<div class="dan_accordion_head_indicator"></div>'.
					'<div>ЭЛЕМЕНТЫ</div>'.
				'</div>'.
				'<div class="dan_accordion_content">'.
					'<table class="admin_table even_odd">'.
						'<tr>'.
							'<td class="admin_table_td_num">1</td>'.
							'<td class="admin_table_td_name">Тип карточки элемента</td>'.
							'<td class="admin_table_td_input">'.
								'<select class="input" name="item_product_card">'.
									'<option value="1">1</option>'.
								'</select>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">2</td>'.
							'<td class="admin_table_td_name">Задать вопрос по товару</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="item_question" name="item_question" type="checkbox" class="input" value="1" '.$item_question_checked.'>'.
								'<label for="item_question"></label>'.
							'</td>'.
						'</tr>'.
					'</table>'.
				'</div>'.
			'</div>'.
			'<div class="dan_accordion_container">'.
				'<input class="dan_accordion_checkbox" type="checkbox">'.
				'<div class="dan_accordion_head">'.
					'<svg class="icon"><use xlink:href="/administrator/template/sprite.svg#basket"></use></svg>'.
					'<div class="dan_accordion_head_indicator"></div>'.
					'<div>ИНТЕРНЕТ-МАГАЗИН</div>'.
				'</div>'.
				'<div class="dan_accordion_content">'.
					'<div style="padding:20px">'.
						'<table>'.
							'<tr>'.
								'<td class="admin_table_td_name">Настройки Интернет-магазина</td>'.
								'<td class="admin_table_td_input">'.
									'<input id="catalog_shop_on" name="shop_on" type="checkbox" class="input" value="1" '.$shop_on_checked.'>'.
									'<label for="catalog_shop_on"></label>'.
								'</td>'.
							'</tr>'.
						'</table>'.
					'</div>'.
					'<table id="catalog_shop_settings" class="admin_table even_odd" '.$shop_display_style.'>'.
						'<tr>'.
							'<td class="admin_table_td_num">1</td>'.
							'<td class="admin_table_td_name">Название каталога (название магазина для Яндекс-Маркета)</td>'.
							'<td class="admin_table_td_input">'.
								'<input name="shop_name" type="text" class="input w_max_500" value="'.$settings['shop_name'].'">'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">2</td>'.
							'<td class="admin_table_td_name">Название компании (используется для Яндекс-Маркета)</td>'.
							'<td class="admin_table_td_input">'.
								'<input name="shop_company_name" type="text" class="input w_max_500" value="'.$settings['shop_company_name'].'">'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">3</td>'.
							'<td class="admin_table_td_name">Условия доставки (используется для Яндекс-Маркета)</td>'.
							'<td class="admin_table_td_input">'.
								'<textarea class="input w_max_500" style="height:100px;" name="shop_delivery">'.$settings['shop_delivery'].'</textarea>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">4</td>'.
							'<td class="admin_table_td_name">Валюта</td>'.
							'<td class="admin_table_td_input">'.
								'<input name="shop_currency" type="text" class="input" value="'.$settings['shop_currency'].'">'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">5</td>'.
							'<td class="admin_table_td_name">Внутренний курс у.е.</td>'.
							'<td class="admin_table_td_input">'.
								'<input name="shop_inner_course_ue" type="text" class="input" value="'.$settings['shop_inner_course_ue'].'">'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">6</td>'.
							'<td class="admin_table_td_name">Купить в 1 клик</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="shop_buy_1_click" name="shop_buy_1_click" type="checkbox" class="input" value="1" '.$shop_buy_1_click_checked.'>'.
								'<label for="shop_buy_1_click"></label>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">7</td>'.
							'<td class="admin_table_td_name">Учёт количеста</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="shop_quantity_accounting" name="shop_quantity_accounting" type="checkbox" class="input" value="1" '.$shop_quantity_accounting_checked.'>'.
								'<label for="shop_quantity_accounting"></label>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">8</td>'.
							'<td class="admin_table_td_name">Включить единицу учёта товара (количество в упаковке)</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="shop_packaging" name="shop_packaging" type="checkbox" class="input" value="1" '.$shop_packaging_checked.'>'.
								'<label for="shop_packaging"></label>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">9</td>'.
							'<td class="admin_table_td_name">Тип корзины</td>'.
							'<td class="admin_table_td_input">'.
								'<select class="input" name="shop_basket_type">'.
									'<option value="normal" '.$shop_basket_type['normal'].'>Обычная</option>'.
									'<option value="fly" '.$shop_basket_type['fly'].'>Летающая</option>'.
								'</select>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">10</td>'.
							'<td class="admin_table_td_name">Тип цен</td>'.
							'<td class="admin_table_td_input">'.
								'<select class="input" name="shop_price_type">'.
									'<option value="1">Розничная</option>'.
								'</select>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">11</td>'.
							'<td class="admin_table_td_name">Пароль для 1с</td>'.
							'<td class="admin_table_td_input">'.
								'<input name="shop_1c_psw" type="text" class="input" value="'.$settings['shop_1c_psw'].'">'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">12</td>'.
							'<td class="admin_table_td_name">Стирать базу данных</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="shop_1c_db_reset" name="shop_1c_db_reset" type="checkbox" class="input" value="1" '.$shop_1c_db_reset_checked.'>'.
								'<label for="shop_1c_db_reset"></label>'.
							'</td>'.
						'</tr>'.
						'<tr>'.
							'<td class="admin_table_td_num">13</td>'.
							'<td class="admin_table_td_name">При загрузки из 1С - обновляется только количество товаров</td>'.
							'<td class="admin_table_td_input">'.
								'<input id="shop_1с_quantity_only" name="shop_1с_quantity_only" type="checkbox" class="input" value="1" '.$shop_1с_quantity_only_checked.'>'.
								'<label for="shop_1с_quantity_only"></label>'.
							'</td>'.
						'</tr>'.
					'</table>'.
				'</div>'.
			'</div>'.
			'<div class="flex_row" style="margin-top:20px">'.
				'<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="Сохранить"></div>'.
				'<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>'.
			'</div>'.
		'</form>'.
	'</div>';
?>
