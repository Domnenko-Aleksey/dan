<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogSection.php';

if(isset($_POST['cancel']))
	header('location: /admin/com/catalog');

$section['name'] = f_input('name');
$section['catalog_id'] = intval($_POST['catalog_id']);
$section['parent_id'] = intval($_POST['parent_id']);
$section['ordering'] = intval($_POST['ordering']);
$section['pub'] = intval($_POST['pub']);

$CATALOG = new AdminCatalogCat();
$SECTION = new AdminCatalogSection();

if (!$CATALOG->getItem($section['catalog_id'])) {
	$SITE->content = 
	'<div class="bg_white">'.
		'<h1>Ошибка</h1>'.
		'<div>Каталог не найден.</div>'.
	'</div>';
} else {
	if (!$section['name']) {
		$SITE->content = 
		'<div class="bg_gray">'.
			'<h1>Ошибка!</h1>'.
			'<div class="tc_container">Не заполнено наименование каталога</div>'.
		'</div>';		
	} else {
		$section_id = $SECTION->insertData($section);		
	}
}

header('location: /admin/com/catalog/cat/'.$section['catalog_id']);


function f_input($name){
	$post_data = isset($_POST[$name]) ? $_POST[$name] : '';
	return trim(htmlspecialchars(strip_tags($post_data)));
}
