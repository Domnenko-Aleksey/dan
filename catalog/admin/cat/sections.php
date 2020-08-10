<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogSection.php';
include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/breadcrumbs.php';
$SITE->headAddFile('/lib/contextmenu/contextmenu.css');
$SITE->headAddFile('/lib/contextmenu/contextmenu.js');
$SITE->headAddFile('/components/catalog/admin/cat/js/sections.js');

$catalog_id = (int)$SITE->d[4];

if (!$catalog_id) {
	include_once $_SERVER['DOCUMENT_ROOT'].'/404.php';
	exit;
}

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
$section_items = $SECTION->getSectionTree($catalog_id);

$breadcrumbs_arr['/admin/com/catalog'] = 'Каталоги';
$breadcrumbs_arr['none'] = $catalog['title'];
$breadcrumbs = breadcrumbs($breadcrumbs_arr);

if(count($section_items) > 0){
	$n = 1;
	$tr = '';
	foreach($section_items as $section){
		if($section['pub'] == 1)
			$tr_class = '';
		else
			$tr_class = 'admin_table_tr_unpub';

		$lvl = str_repeat('&nbsp;-&nbsp', $section['level']);

		$tr .= 
			'<tr class="'.$tr_class.'">'.
				'<td>'.$n.'</td>'.
				'<td>'.
					'<div class="flex_row contextmenu_wrap"><svg class="contextmenu_ico" title="Действия" data-id="'.$section['id'].'"><use xlink:href="/administrator/template/sprite.svg#menu_3"></use></svg></div>'.
				'</td>'.
				'<td><a href="/admin/com/catalog/section/'.$section['id'].'">'.$lvl.$section['name'].'</a></td>'.
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
			'<a href="/admin/com/catalog/section/add/'.$catalog_id.'" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#folder_add"></use></svg>'.
				'<div class="ico_rectangle_text">Добавить раздел</div>'.
			'</a>'.
			'<a href="/admin/com/catalog/item/add/'.$section['id'].'" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#paper_add"></use></svg>'.
				'<div class="ico_rectangle_text">Добавить элемент</div>'.
			'</a>'.
			'<a href="/admin/com/catalog/cat/settings_edit/'.$catalog['id'].'" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#gear"></use></svg>'.
				'<div class="ico_rectangle_text">Настройки</div>'.
			'</a>'.
			'<a href="/admin/com/catalog/char/'.$catalog['id'].'" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#chars"></use></svg>'.
				'<div class="ico_rectangle_text">Характеристики</div>'.
			'</a>'.
			'<a href="/admin/viewsite" target="blank" class="ico_rectangle_container">'.
				'<svg><use xlink:href="/administrator/template/sprite.svg#help"></use></svg>'.
				'<div class="ico_rectangle_text">Помощь</div>'.
			'</a>'.
		'</div>'.
		'<h1>'.$catalog['title'].' <span class="hint">(каталог)</span></h1>'.
		$table.
	'</div>';
