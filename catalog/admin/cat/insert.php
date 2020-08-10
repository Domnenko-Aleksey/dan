<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/classes/Translit.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/classes/SefUrl.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/cat/settings_array.php';

if(isset($_POST['cancel']))
	header('location: /admin/com/catalog');

$data['title'] = f_input('name');
$s = f_input('sef');
$data['settings'] = $settings_array;
$data['ordering'] = $_POST['ordering'];

$translit = new Translit();
$data['url'] = mb_strtolower($translit->getResult($s));

$sefUrl = new SefUrl();
if($sefUrl->checkUrl($data['url'], '')){
	$dir = $_SERVER['DOCUMENT_ROOT'].'/files/'.$data['url'];
	if(!is_dir($dir))
		mkdir($dir, 0755, true);
	$catalog = new AdminCatalogCat();
	$catalog->insertData($data);
	header('location: /admin/com/catalog');
} else{
	$SITE->content = 
	'<div class="bg_white">'.
		'<h1>Ошибка</h1>'.
		'<div>URL <b>'.$data['url'].'</b> уже занят системой</div>'.
	'</div>';
}


function f_input($name){
	$post_data = isset($_POST[$name]) ? $_POST[$name] : '';
	return trim(htmlspecialchars(strip_tags($post_data)));
}
