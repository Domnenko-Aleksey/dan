<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/breadcrumbs.php';
$SITE->headAddFile('/lib/contextmenu/contextmenu.css');
$SITE->headAddFile('/lib/contextmenu/contextmenu.js');
$SITE->headAddFile('/components/catalog/admin/cat/js/catalog.js');

$catalog_id = $SITE->d[4];

$code =
	'<script>window.addEventListener("DOMContentLoaded", function(){'.
		'var contextmenu_catalog = ['.
			'["admin/com/catalog/cat/settings_edit", "contextmenu_tools", "Настройки"],'.
			'["admin/com/catalog/cat/edit", "contextmenu_edit", "Редактировать каталог"],'.			
			'["admin/com/catalog/cat/up", "contextmenu_up", "Вверх"],'.
			'["admin/com/catalog/cat/down", "contextmenu_down", "Вниз"],'.
			'["admin/com/catalog/cat/pub", "contextmenu_pub", "Опубликовать"],'.
			'["admin/com/catalog/cat/unpub", "contextmenu_unpub", "Скрыть"],'.
			'["#ADMIN.catalog.delete_modal", "contextmenu_delete", "Удалить каталог"]'.
		'];'.
		'CONTEXTMENU.add("contextmenu_ico", contextmenu_catalog, "left");'.
	'})</script>';
$SITE->headAddCode($code);

$catalog = new AdminCatalogCat();
$catalog_items_arr = $catalog->getItems();
$breadcrumbs_arr['none'] = 'Каталоги';
$breadcrumbs = breadcrumbs($breadcrumbs_arr);

if(count($catalog_items_arr) > 0){
	$n = 1;
	$tr = '';
	foreach($catalog_items_arr as $item){
		if($item['enabled'] == 1)
			$tr_class = '';
		else
			$tr_class = 'admin_table_tr_unpub';
		$tr .= 
			'<tr class="'.$tr_class.'">'.
				'<td>'.$n.'</td>'.
				'<td>'.
					'<div class="flex_row contextmenu_wrap"><svg class="contextmenu_ico" title="Действия" data-id="'.$item['id'].'"><use xlink:href="/administrator/template/sprite.svg#menu_3"></use></svg></div>'.
				'</td>'.
				'<td><a href="/admin/com/catalog/cat/'.$item['id'].'">'.$item['components'].'</a></td>'.
				'<td>'.$item['title'].'</td>'.
			'</tr>';
		$n++;
	}

	$table = 
		'<h1>Каталоги</h1>'.
		'<div class="flex_row_start">'.
			'<table class="admin_table even_odd">'.
				'<tr>'.
					'<th style="width:50px;">№</td>'.
					'<th style="width:50px;">&nbsp;</td>'.
					'<th style="width:200px;">URL</td>'.
					'<th>Наменование</td>'.
				'</tr>'.
				$tr.
			'</table>'.
		'</div>';
} else{
	$table = '';
}


$SITE->content = 
	'<div class="bg_gray">'.
		$breadcrumbs.
		'<div class="flex_row_start">'.
			'<a href="/admin/com/catalog/cat/add/'.$catalog_id.'" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#add"></use></svg>'.
				'<div class="ico_rectangle_text">Добавить каталог</div>'.
			'</a>'.
			'<a href="/admin/viewsite" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#help"></use></svg>'.
				'<div class="ico_rectangle_text">Помощь</div>'.
			'</a>'.
		'</div>'.
		$table.
	'</div>';
