<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogChar.php';
include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/breadcrumbs.php';
$SITE->headAddFile('/components/catalog/admin/char/list.css');
$SITE->headAddFile('/lib/DRAG_N_DROP/DRAG_DROP.css');
$SITE->headAddFile('/lib/DRAG_N_DROP/DRAG_DROP.js');
$SITE->headAddFile('/components/catalog/admin/char/list.js');

$catalog_id = (int)$SITE->d[4];

$CATALOG = new AdminCatalogCat();
$CHAR = new AdminCatalogChar();
$catalog = $CATALOG->getItem($catalog_id);
$chars = $CHAR->getCharNameList($catalog_id);

$breadcrumbs_arr['/admin/com/catalog'] = 'Каталоги';
$breadcrumbs_arr['/admin/com/catalog/cat/'.$catalog_id] = $catalog['title'];
$breadcrumbs_arr['none'] = 'Характеристики';
$breadcrumbs = breadcrumbs($breadcrumbs_arr);

$type = array('string' => 'строка', 'number' => 'число', 'date' => 'дата', 'color' => 'цвет');

$tables = '';
if ($chars) {
	foreach ($chars as $char) {
		$unit = $char['unit'] != '' ? '('.$char['unit'].')' : '';
		$tables .= 
			'<table class="drag_drop" data-id="'.$char['id'].'">'.
				'<tr>'.
					'<td>'.$char['id'].'</td>'.
					'<td>'.
						'<div class="flex_row contextmenu_wrap"><svg class="drag_drop_ico" title="Перетащить" data-id="'.$char['id'].'" data-target-id="drag_target" data-class="drag_drop" data-f="ADMIN.chars.drag_drop"><use xlink:href="/administrator/template/sprite.svg#cursor24"></use></svg></div>'.
					'</td>'.
					'<td><a href="/admin/com/catalog/char/edit/'.$char['id'].'">'.$char['name'].' '.$unit.'</a></td>'.
					'<td>'.$type[$char['type']].'</td>'.
					'<td>'.
						'<svg class="catalog_char_delete" data-id="'.$char['id'].'"><use xlink:href="/administrator/template/sprite.svg#delete"></use></svg>'.
					'</td>'.
				'</tr>'.
			'</table>';
	}

} 


$SITE->content = 
	'<div class="bg_gray">'.
		$breadcrumbs.
		'<div class="flex_row_start">'.
			'<a href="/admin/com/catalog/char/add/'.$catalog_id.'" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#paper_add"></use></svg>'.
				'<div class="ico_rectangle_text">Добавить характеристику</div>'.
			'</a>'.
			'<a href="/admin/com/catalog/char/help" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#help"></use></svg>'.
				'<div class="ico_rectangle_text">Помощь</div>'.
			'</a>'.
		'</div>'.
		'<h1>Характеристики</h1>'.
		'<div class="flex_row_start">'.
			'<table class="admin_table even_odd">'.
				'<tr>'.
					'<th>Id</th>'.
					'<th></th>'.
					'<th>Наменование</th>'.
					'<th>Тип</th>'.
					'<th></th>'.
				'</tr>'.
			'</table>'.
		'</div>'.
		'<div id="drag_target" data-catalog_id="'.$catalog_id.'">'.$tables.'</div>'.
	'</div>';
