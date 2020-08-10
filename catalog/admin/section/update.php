<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogSection.php';
$SECTION = new AdminCatalogSection();

$section['id'] = intval($SITE->d[5]);
$section['name'] = f_input('name');
$section['parent_id'] = intval($_POST['parent_id']);
$section['ordering'] = intval($_POST['ordering']);
$section['pub'] = intval($_POST['pub']);

if(isset($_POST['cancel']))
	header('location: /admin/com/catalog/section/'.$section['id']);

if(!$section['id'])
	header('location: /admin/com/catalog');

if (!$section['name']) {
	$SITE->content = 
	'<div class="bg_gray">'.
		'<h1>Ошибка!</h1>'.
		'<div class="tc_container">Не заполнено наименование каталога</div>'.
	'</div>';		
} else {
	$SECTION->updateSection($section);
	$catalog_id = $SECTION->getSection($section['id'])['catalog_id'];

	header('location: /admin/com/catalog/cat/'.$catalog_id);
}


function f_input($name){
	$post_data = isset($_POST[$name]) ? $_POST[$name] : '';
	return trim(htmlspecialchars(strip_tags($post_data)));
}
