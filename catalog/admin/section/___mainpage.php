<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogSection.php';
$SITE->headAddFile('/lib/contextmenu/contextmenu.css');
$SITE->headAddFile('/lib/contextmenu/contextmenu.js');
// $SITE->headAddFile('/components/catalog/admin/section/section.js');

$catalog_id = $SITE->d[5];

$code =
	'<script>window.addEventListener("DOMContentLoaded", function(){'.
		'var contextmenu_catalog = ['.
			'["admin/com/catalog/section/settings_edit", "contextmenu_tools", "Настройки"],'.
			'["admin/com/catalog/section/edit", "contextmenu_edit", "Редактировать раздел"],'.			
			'["admin/com/catalog/section/up", "contextmenu_up", "Вверх"],'.
			'["admin/com/catalog/section/down", "contextmenu_down", "Вниз"],'.
			'["admin/com/catalog/section/pub", "contextmenu_pub", "Опубликовать"],'.
			'["admin/com/catalog/section/unpub", "contextmenu_unpub", "Скрыть"],'.
			'["#ADMIN.catalog.section.delete_modal", "contextmenu_delete", "Удалить раздел"]'.
		'];'.
		'CONTEXTMENU.add("contextmenu_ico", contextmenu_catalog, "left");'.
	'})</script>';
$SITE->headAddCode($code);
$CATALOG = new AdminCatalogCat();
$SECTION = new AdminCatalogSection();
$catalog = $CATALOG->getItem($catalog_id);
$sections_arr = $SECTION->getSections($catalog_id);

if(count($sections_arr) > 0){
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
				'<td>'.$item['components'].'</td>'.
				'<td>'.$item['title'].'</td>'.
			'</tr>';
		$n++;
	}

	$table = 
		'<div class="flex_row_start">'.
			'<table class="admin_table even_odd">'.
				'<tr>'.
					'<th style="width:50px;">№</td>'.
					'<th style="width:50px;">&nbsp;</td>'.
					'<th>URL</td>'.
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
		'<div class="flex_row_start">'.
			'<a href="/admin/com/catalog/section/add/'.$catalog_id.'" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#folder_add"></use></svg>'.
				'<div class="ico_rectangle_text">Добавить раздел</div>'.
			'</a>'.
			'<a href="/admin/com/catalog/item/add" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#paper_add"></use></svg>'.
				'<div class="ico_rectangle_text">Добавить элемент</div>'.
			'</a>'.
			'<a href="/admin/viewsite" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#help"></use></svg>'.
				'<div class="ico_rectangle_text">Помощь</div>'.
			'</a>'.
		'</div>'.
		'<h1>'.$catalog['title'].'<h1>'.
		$table.
	'</div>';
