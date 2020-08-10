<?php
defined('AUTH') or die('Restricted access');

$SITE->headAddFile('/components/catalog/admin/cat/css/style.css');
$SITE->headAddFile('/components/catalog/admin/cat/js/catalog.js');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
$cat = new AdminCatalogCat();

$id = $SITE->d[5];

if($SITE->d[4] == 'add'){
	$catalog['title'] = '';
	$catalog['components'] = '';
	$catalog['ordering'] = $cat->maxOrdering() + 1;
	$act = 'insert';
	$url = '';
	$title = 'Создать';
	$button_text = 'Создать';
}

if($SITE->d[4] == 'edit'){
	$catalog = $cat->getItem($id);
	$act = 'update/'.$SITE->d[5];
	$url = '<input type="hidden" name="url" value="'.$catalog['components'].'">';
	$title = 'Редактировать';
	$button_text = 'Сохранить';
}


$SITE->content = 
	'<div class="bg_gray">'.
		'<h1>'.$title.' каталог</h1>'.
		'<form method="post" action="/admin/com/catalog/cat/'.$act.'">'.
			'<div class="tc_container">'.
				'<div class="flex_row p_5_20">'.
					'<div class="tc_item_l">Наименование</div>'.
					'<div class="tc_item_r flex_grow">'.
						'<input class="input" name="name" placeholder="Интернет магазин" required value="'.$catalog['title'].'">'.
					'</div>'.
				'</div>'.
				'<div class="flex_row p_5_20">'.
					'<div class="tc_item_l">URL адрес каталога</div>'.
					'<div class="tc_item_r flex_grow">'.
						'<input id="sef" class="input" name="sef" placeholder="catalog" required value="'.$catalog['components'].'">'.
						'<div id="url_status"></div>'.
					'</div>'.
				'</div>'.
				'<div class="flex_row p_5_20">'.
					'<div class="tc_item_l">Порядок следования</div>'.
					'<div class="tc_item_r flex_grow">'.
						'<input class="input" name="ordering" type="number" value="'.$catalog['ordering'].'">'.
						'<div id="url_status"></div>'.
					'</div>'.
				'</div>'.
				'<div class="flex_row p_5_20">'.
					'<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="'.$button_text.'"></div>'.
					'<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>'.
				'</div>'.
			'</div>'.
			$url.
		'</form>'.
	'</div>';

?>
