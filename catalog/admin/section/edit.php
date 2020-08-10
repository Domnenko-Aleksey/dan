<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogSection.php';
include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/breadcrumbs.php';
$SITE->headAddFile('/components/catalog/admin/section/style.css');
$SITE->headAddFile('/components/catalog/admin/section/section.js');

$options_list = '';
$CATALOG = new AdminCatalogCat();
$SECTION = new AdminCatalogSection();
$catalog_arr = $CATALOG->getItems();

// Добавить раздел
if($SITE->d[4] == 'add'){
	$section['id'] = 0;
	$section['catalog_id'] = $SITE->d[5];
	$section['name'] = $section['parent_id'] = '';
	$section['ordering'] = $SECTION->getMaxOrdering($section['catalog_id']) + 1;
	$act = 'insert';
	$title = 'Создать';
	$button_text = 'Создать';
	$section['pub'] = 1;
	$section_parent_arr = false;
}

// Редактировать раздел
if($SITE->d[4] == 'edit'){
	$id = $SITE->d[5];
	$section = $SECTION->getSection($id);
	$act = 'update/'.$SITE->d[5];
	$title = 'Редактировать';
	$button_text = 'Сохранить';
	$parent_arr = $SECTION->getParentsArr($id);
	$section_parent_arr = false;
	if ($parent_arr) {
		$arr = array_reverse($parent_arr);
		if (count($arr) > 0)
			$section_parent_arr = array_reverse($arr);		
	}
}

$catalog = $CATALOG->getItem($section['catalog_id']);
$section_catalog = '<b>'.$catalog['title'].'</b>';

$breadcrumbs_arr['/admin/com/catalog'] = 'Каталоги';
$breadcrumbs_arr['/admin/com/catalog/cat/'.$catalog['id']] = $catalog['title'];
if ($section_parent_arr) {
	foreach ($section_parent_arr as $key => $parent) {
		$breadcrumbs_arr['/admin/com/catalog/section/'.$parent['id']] = $parent['name'];
	}	
}
$breadcrumbs_arr['none'] = $title.' раздел';
$breadcrumbs = breadcrumbs($breadcrumbs_arr);


// Вывод родительских пунктов меню
$tree = $SECTION->getSectionTree($section['catalog_id']);
$tree_out = '';
$show = true;  // Признак редактируемого элемента и элементов, для которых он является родителем. Их не показывать
$this_level = 0;  // Уровень редактируемого элемента

foreach($tree as $s) {
	$lvl = str_repeat('&nbsp;-&nbsp', $s['level']);

	if ($s['id'] == $section['parent_id'])
		$selected = 'selected';
	else
		$selected = '';

	// Ставим флаг - не выводить в родительском дереве наш пункт и ниже
	if ($s['id'] == $section['id']) {
		$this_level = $s['level'];
		$show = false;
		continue;
	}

	// Если прошли редактируемый элемент и его дочерние пункты
	if (!$show && $s['level'] <= $this_level)
		$show = true;

	if ($show)  // выводим все разделы кроме текущего и его дочерних пунктов
		$tree_out .= '<option value="'.$s['id'].'" '.$selected.'>'.$lvl.$s['name'].'</option>';
}

$tree_out = '<select name="parent_id" class="input"><option value="0">Корневой каталог</option>'.$tree_out.'</select>';


if (!$catalog_arr) {
	$SITE->content = 
		'<div class="bg_gray">'.
			$breadcrumbs.
			'<h1>Раздел не может быть создан, т.к. не созданы каталоги</h1>'.
		'</div>';	
} else {
	$pub = array_fill(0, 3, '');
	$pub[$section['pub']] = 'selected';

	$SITE->content = 
		'<div class="bg_gray">'.
			$breadcrumbs.
			'<h1>'.$title.' раздел</h1>'.
			'<form method="post" action="/admin/com/catalog/section/'.$act.'">'.
				'<div class="flex_row">'.
					'<div class="tc_item_l" style="height:40px;">Каталог</div>'.
					'<div id="catalogs_list" class="tc_item_r flex_grow">'.
						$section_catalog.
					'</div>'.
				'</div>'.
				'<div class="tc_container">'.
					'<div class="flex_row">'.
						'<div class="tc_item_l">Наименование</div>'.
						'<div class="tc_item_r flex_grow">'.
							'<input class="input" name="name" placeholder="Интернет магазин" required value="'.$section['name'].'">'.
						'</div>'.
					'</div>'.
					'<div class="flex_row">'.
						'<div class="tc_item_l">Родительский раздел</div>'.
						'<div id="catalogs_list" class="tc_item_r flex_grow">'.
							$tree_out.
						'</div>'.
					'</div>'.
					'<div class="flex_row">'.
						'<div class="tc_item_l">Порядок следования</div>'.
						'<div class="tc_item_r flex_grow">'.
							'<input class="input" name="ordering" type="number" value="'.$section['ordering'].'">'.
						'</div>'.
					'</div>'.
					'<div class="flex_row">'.
						'<div class="tc_item_l">Видимость раздела</div>'.
						'<div id="catalogs_list" class="tc_item_r flex_grow">'.
							'<select class="input" name="pub">'.
								'<option value="1" '.$pub[1].'>Опубликован</option>'.
								'<option value="0" '.$pub[0].'>Скрыт</option>'.
								'<option value="2" '.$pub[2].'>Доступен определённой группе</option>'.
							'</select>'.
						'</div>'.
					'</div>'.
					'<input type="hidden" name="catalog_id" value="'.$section['catalog_id'].'">'.
					'<div class="flex_row p_40_20">'.
						'<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="'.$button_text.'"></div>'.
						'<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>'.
					'</div>'.
				'</div>'.
			'</form>'.
		'</div>';	
}

?>
