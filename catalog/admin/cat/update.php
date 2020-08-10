<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/classes/Translit.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/classes/SefUrl.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
$catalog = new AdminCatalogCat();

if(isset($_POST['cancel']))
	header('location: /admin/com/catalog');

$data['id'] = $SITE->d[5];
$data['title'] = f_input('name');
$s = f_input('sef');
$url = f_input('url');
$data['ordering'] = intval($_POST['ordering']);

$translit = new Translit();
$data['url'] = mb_strtolower($translit->getResult($s));

$sefUrl = new SefUrl();
if($sefUrl->checkUrl($data['url'], $url)){
	$dir_old = $_SERVER['DOCUMENT_ROOT'].'/files/'.$url;
	$dir_new = $_SERVER['DOCUMENT_ROOT'].'/files/'.$data['url'];
	if(is_dir($dir_old))
		rename($dir_old, $dir_new);
	$catalog->updateData($data);
	header('location: /admin/com/catalog');
} else{
	$SITE->content = 
	'<div class="bg_white">'.
		'<h1>Ошибка</h1>'.
		'<div>URL <b>'.$data['url'].'</b> уже занят системой'.
	'</div>';
}


function f_input($name){
	$post_data = isset($_POST[$name]) ? $_POST[$name] : '';
	return trim(htmlspecialchars(strip_tags($post_data)));
}
