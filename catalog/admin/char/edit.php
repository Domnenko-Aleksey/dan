<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogChar.php';

include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/breadcrumbs.php';

$CATALOG = new AdminCatalogCat();
$CHAR = new AdminCatalogChar();

$char_type_select = array('string' => '', 'number' => '', 'date' => '', 'color' => '');

// Добавить характеристику
if ($SITE->d[4] == 'add') {
	$act = 'insert';
	$title = 'Добавить';
	$button_text = 'Добавить';

	$char['id'] = '';
	$char['catalog_id'] = $SITE->d[5];
	$char['name'] = $char['unit'] = $char['identifier'] = '';
	$char['ordering'] = $CHAR->getMaxOrdering($char['catalog_id']) + 1;

	$catalog = $CATALOG->getItem($char['catalog_id']);

	$char_type_select['string'] = 'selected';
}

// Редактировать характеристику
if ($SITE->d[4] == 'edit') {
	$item_id = $SITE->d[5];
	$act = 'update/'.$item_id;
	$title = 'Редактировать';
	$button_text = 'Сохранить';

	$char = $CHAR->getCharName($item_id);
	$catalog = $CATALOG->getItem($char['catalog_id']);

	$char_type_select[$char['type']] = 'selected';
}

$breadcrumbs_arr['/admin/com/catalog'] = 'Каталоги';
$breadcrumbs_arr['/admin/com/catalog/cat/'.$catalog['id']] = $catalog['title'];

$breadcrumbs_arr['none'] = 'Характеристики';
$breadcrumbs = breadcrumbs($breadcrumbs_arr);

$SITE->content = 
'<div class="bg_gray">'.
	$breadcrumbs.
	'<h1>'.$title.' характеристику</h1>'.
	'<form enctype="multipart/form-data" method="post" action="/admin/com/catalog/char/'.$act.'">'.
		'<div class="tc_container">'.
			'<div class="flex_row">'.
				'<div class="tc_item_l">Наименование</div>'.
				'<div class="tc_item_r flex_grow">'.
					'<input class="input" name="name" required value="'.$char['name'].'">'.
				'</div>'.
			'</div>'.
			'<div class="flex_row">'.
				'<div class="tc_item_l">Единица измерения</div>'.
				'<div class="tc_item_r flex_grow">'.
					'<input class="input" name="unit" value="'.$char['unit'].'">'.
				'</div>'.
			'</div>'.
			'<div class="flex_row">'.
				'<div class="tc_item_l">Тип</div>'.
				'<div class="tc_item_r flex_grow">'.
					'<select class="input" name="type">'.
						'<option value="string" '.$char_type_select['string'].'>Строка</option>'.
						'<option value="number" '.$char_type_select['number'].'>Число</option>'.
						'<option value="date" '.$char_type_select['date'].'>Дата</option>'.
						'<option value="color" '.$char_type_select['color'].'>Цвет</option>'.
					'</select>'.
				'</div>'.
			'</div>'.
			'<div class="flex_row">'.
				'<div class="tc_item_l">Порядок следования</div>'.
				'<div class="tc_item_r flex_grow">'.
					'<input class="input" name="ordering" type="number" value="'.$char['ordering'].'">'.
				'</div>'.
			'</div>'.
			'<div class="flex_row">'.
				'<div class="tc_item_l">Идентификатор</div>'.
				'<div class="tc_item_r flex_grow">'.
					'<input class="input" name="identifier" value="'.$char['identifier'].'">'.
				'</div>'.
			'</div>'.
			'<input type="hidden" name="catalog_id" value="'.$char['catalog_id'].'">'.
			'<div class="flex_row p_40_20">'.
				'<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="'.$button_text.'"></div>'.
				'<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>'.
			'</div>'.
		'</div>'.
	'</form>'.
'</div>';	


?>
