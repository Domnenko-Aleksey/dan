<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogItem.php';
$ITEM = new AdminCatalogItem();

$item['id'] = intval($SITE->d[5]);
$item['name'] = f_input('name');
$item['section_id'] = intval($_POST['section_id']);
$item['ordering'] = intval($_POST['ordering']);
$item['pub'] = isset($_POST['pub']) ? 1 : 0;
$item['text'] = $_POST['editor1'];
$item['images'] = $_POST['images_order'];


if(isset($_POST['cancel']))
	header('location: /admin/com/catalog/section/'.$item['section_id']);

if (!$item['name']) {
	$SITE->content = 
	'<div class="bg_gray">'.
		'<h1>Ошибка!</h1>'.
		'<div class="tc_container">Не заполнено наименование каталога</div>'.
	'</div>';		
} else {
	$ITEM->update($item);
	header('location: /admin/com/catalog/section/'.$item['section_id']);
}


function f_input($name){
	$post_data = isset($_POST[$name]) ? $_POST[$name] : '';
	return trim(htmlspecialchars(strip_tags($post_data)));
}
