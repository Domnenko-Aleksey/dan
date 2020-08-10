<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogSection.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogItem.php';
include $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/breadcrumbs.php';
$SITE->headAddFile('/components/catalog/admin/item/style.css');
$SITE->headAddFile('/administrator/plugins/ckeditor_textarea/ckeditor.js');

$CATALOG = new AdminCatalogCat();
$SECTION = new AdminCatalogSection();
$ITEM = new AdminCatalogItem();

// Добавить элемент
if ($SITE->d[4] == 'add') {
	$act = 'insert';
	$title = 'Добавить';
	$button_text = 'Создать';
	$section['pub'] = 1;
	$section_parent_arr = false;

	$item['id'] = '';
	$item['section_id'] = $SITE->d[5];
	$item['name'] = $item['text'] = $item['images'] = '';
	$item['ordering'] = $ITEM->getMaxOrdering($item['section_id']) + 1;
	$item['pub'] = 1;
	$section = $SECTION->getSection($item['section_id']);
	$catalog = $CATALOG->getItem($section['catalog_id']);

	$images_out_tr = '';
	$images_out = '';
}

// Редактировать элемент
if ($SITE->d[4] == 'edit') {
	$SITE->headAddFile('/lib/DRAG_N_DROP/DRAG_DROP.css');
	$SITE->headAddFile('/lib/DRAG_N_DROP/DRAG_DROP.js');
	$SITE->headAddFile('/lib/contextmenu/contextmenu.css');
	$SITE->headAddFile('/lib/contextmenu/contextmenu.js');
	$SITE->headAddFile('/components/catalog/admin/item/edit.js');
	$item_id = $SITE->d[5];
	$act = 'update/'.$item_id;
	$title = 'Редактировать';
	$button_text = 'Сохранить';

	$item = $ITEM->getItem($item_id);
	$section = $SECTION->getSection($item['section_id']);
	$catalog = $CATALOG->getItem($section['catalog_id']);
	$section_parent_arr = $SECTION->getParentsArr($item['section_id']);

	$arr = $SECTION->getParentsArr($section['id']);
	if (count($arr) > 0)
		$section_parent_arr = array_reverse($arr);
	else
		$section_parent_arr = false;

	$breadcrumbs_text = $item['name'];

	// Выводим изображения
	$images_out = '';
	$dir = '/files/catalog/'.$catalog['id'].'/items/';
	if ($item['images'] != '') {
	$images = explode(';', $item['images']);
		foreach ($images as $image) {
			$images_out .= '<img class="drag_drop_ico" src="'.$dir.$image.'" data-target-id="drag_trg" data-class="drag_drop_ico" data-f="ADMIN.catalog.item.images_ordering">';
		}
	}

	$images_out_tr =
		'<div class="flex_row">'.
			'<div class="tc_item_l">Изображения</div>'.
			'<div id="drag_trg" class="tc_item_r flex_grow">'.$images_out.'</div>'.
		'</div>';
}

// $section_catalog = '<b>'.$CATALOG->getItem($section['catalog_id'])['title'].'</b>';

$breadcrumbs_arr['/admin/com/catalog'] = 'Каталоги';
$breadcrumbs_arr['/admin/com/catalog/cat/'.$catalog['id']] = $catalog['title'];
if ($section_parent_arr) {
	foreach ($section_parent_arr as $key => $parent) {
		$breadcrumbs_arr['/admin/com/catalog/section/'.$parent['id']] = $parent['name'];
	}	
}
$breadcrumbs_arr['none'] = $title.' элемент';
$breadcrumbs = breadcrumbs($breadcrumbs_arr);


// Вывод пунктов меню

$tree = $SECTION->getSectionTree($section['catalog_id']);
$tree_out = '';
$show = true;  // Признак редактируемого элемента и элементов, для которых он является родителем. Их не показывать
$this_level = 0;  // Уровень редактируемого элемента

foreach ($tree as $s) {
	$lvl = str_repeat('&nbsp;-&nbsp', $s['level']);

	// Ставим флаг - не выводить в родительском дереве наш пункт и ниже
	$selected = $s['id'] == $section['id'] ? 'selected' : '';
	$tree_out .= '<option value="'.$s['id'].'" '.$selected.'>'.$lvl.$s['name'].'</option>';
}

$tree_out = '<select name="section_id" class="input">'.$tree_out.'</select>';
$pub_checked = $item['pub'] == 1 ? 'checked' : '';



$SITE->content = 
'<div class="bg_gray">'.
	$breadcrumbs.
	'<h1>'.$title.' элемент</h1>'.
	'<form enctype="multipart/form-data" method="post" action="/admin/com/catalog/item/'.$act.'">'.
		'<div class="tc_container">'.
			'<div class="flex_row">'.
				'<div class="tc_item_l">Наименование</div>'.
				'<div class="tc_item_r flex_grow">'.
					'<input class="input" name="name" placeholder="Интернет магазин" required value="'.$item['name'].'">'.
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
					'<input class="input" name="ordering" type="number" value="'.$item['ordering'].'">'.
				'</div>'.
			'</div>'.
			'<div class="flex_row">'.
				'<div class="tc_item_l">Видимость элемента</div>'.
				'<div id="catalogs_list" class="tc_item_r flex_grow">'.
					'<input id="pub" name="pub" class="input" type="checkbox" '.$pub_checked.' value="1"><label for="pub"></label>'.
				'</div>'.
			'</div>'.
				$images_out_tr.
			'<div class="flex_row">'.
				'<div class="tc_item_l">Загрузить новое изображение</div>'.
				'<div id="catalogs_list" class="tc_item_r flex_grow">'.
					'<input id="image_file" type="file" name="image" data-id="'.$item['id'].'">'.
					'<span id="img_status"></span>'.
					'<span class="img_warn">Загружаемый размер изображения - не более 2 мегабайт.</span>'.
				'</div>'.
			'</div>'.
			'<div class="flex_row">'.
				'<div class="tc_item_l">Текст</div>'.
				'<div id="catalogs_list" class="tc_item_r flex_grow">'.
					'<textarea name="editor1">'.$item['text'].'</textarea>'.
				'</div>'.
			'</div>'.
			'<div class="flex_row p_40_20">'.
				'<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="'.$button_text.'"></div>'.
				'<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>'.
			'</div>'.
			'<input id="images_order" name="images_order" type="hidden" value="'.$item['images'].'">'.
		'</div>'.
	'</form>'.
	'<script type="text/javascript">'.
		'e_editor_1 = CKEDITOR.replace("editor1", {'.
			'height: "400px",'.
			'filebrowserBrowseUrl : "/administrator/plugins/browser/dan_browser.php",'.
		'});'.
	'</script>'.
'</div>';	


?>
