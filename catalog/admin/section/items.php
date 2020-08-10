<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogSection.php';
include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/breadcrumbs.php';
$SITE->headAddFile('/lib/contextmenu/contextmenu.css');
$SITE->headAddFile('/lib/contextmenu/contextmenu.js');
$SITE->headAddFile('/components/catalog/admin/cat/sections.js');

$section_id = (int)$SITE->d[4];

if (!$section_id) {
	include_once $_SERVER['DOCUMENT_ROOT'].'/404.php';
	exit;
}

$code =
	'<script>window.addEventListener("DOMContentLoaded", function(){'.
		'var contextmenu_catalog = ['.
			'["admin/com/catalog/item/edit", "contextmenu_edit", "Редактировать элемент"],'.			
			'["admin/com/catalog/item/up", "contextmenu_up", "Вверх"],'.
			'["admin/com/catalog/item/down", "contextmenu_down", "Вниз"],'.
			'["admin/com/catalog/item/pub", "contextmenu_pub", "Опубликовать"],'.
			'["admin/com/catalog/item/unpub", "contextmenu_unpub", "Скрыть"],'.
			'["#ADMIN.catalog.item.delete_modal", "contextmenu_delete", "Удалить элемент"]'.
		'];'.
		'CONTEXTMENU.add("contextmenu_ico", contextmenu_catalog, "left");'.
	'})</script>';
$SITE->headAddCode($code);


$CATALOG = new AdminCatalogCat();
$SECTION = new AdminCatalogSection();
$section = $SECTION->getSection($section_id);
$catalog = $CATALOG->getItem($section['catalog_id']);
$items = $SECTION->getItems($section_id);

$breadcrumbs_arr['/admin/com/catalog'] = 'Каталоги';
$breadcrumbs_arr['/admin/com/catalog/cat/'.$section['catalog_id']] = $catalog['title'];
$breadcrumbs_arr['none'] = $section['name'];
$breadcrumbs = breadcrumbs($breadcrumbs_arr);

if ($items) {
	$n = 1;
	$tr = '';

	foreach ($items as $item) {
		if ($item['pub'] == 1)
			$tr_class = '';
		else
			$tr_class = 'admin_table_tr_unpub';

		$tr .= 
			'<tr class="'.$tr_class.'">'.
				'<td>'.$n.'</td>'.
				'<td>'.
					'<div class="flex_row contextmenu_wrap"><svg class="contextmenu_ico" title="Действия" data-id="'.$item['id'].'"><use xlink:href="/administrator/template/sprite.svg#menu_3"></use></svg></div>'.
				'</td>'.
				'<td><a href="/admin/com/catalog/item/edit/'.$item['id'].'">'.$item['name'].'</a></td>'.
			'</tr>';
		$n++;
	}

	$table = 
		'<div class="flex_row_start">'.
			'<table class="admin_table even_odd">'.
				'<tr>'.
					'<th style="width:50px;">№</td>'.
					'<th style="width:50px;">&nbsp;</td>'.
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
			'<a href="/admin/com/catalog/item/add/'.$section_id.'" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#paper_add"></use></svg>'.
				'<div class="ico_rectangle_text">Добавить элемент</div>'.
			'</a>'.
			'<a href="/admin/viewsite" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#help"></use></svg>'.
				'<div class="ico_rectangle_text">Помощь</div>'.
			'</a>'.
		'</div>'.
		// '<h1>'.$catalog['title'].' <span class="hint">(каталог)</span></h1>'.
		$table.
	'</div>';
