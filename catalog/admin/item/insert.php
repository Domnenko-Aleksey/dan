<?php
defined('AUTH') or die('Restricted access');
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogSection.php';
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogItem.php';

$CATALOG = new AdminCatalogCat();
$SECTION = new AdminCatalogSection();
$ITEM = new AdminCatalogItem();

set_time_limit(60);
ini_set('memory_limit', '1024M');
$memory_limit = get_cfg_var('memory_limit');
$memory_limit = (real)$memory_limit;

$item['section_id'] = intval($_POST['section_id']);
$item['name'] = f_input('name');
$item['text'] = $_POST['editor1'];
$item['settings'] = '';
$item['ordering'] = intval($_POST['ordering']);
$item['pub'] = intval($_POST['pub']);


$image = $_FILES['image'];

if (isset($_POST['cancel'])) 
	header('location: /admin/com/catalog/section/'.$item['section_id']);


// --- ПРОВЕРКА ---
if (!$item['name']) {
	$SITE->content = 
	'<div class="bg_gray">'.
		'<h1>Ошибка!</h1>'.
		'<div class="tc_container">Не заполнено наименование каталога</div>'.
	'</div>';		
}

if ($image['size'] >= 5000000) { // Проверка размера файла
	die ('
	<html>
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<title>Файл слишком большой!</title>
		</head>
		<body>
			<h3 align="center">Файл слишком большой! Максимальный размер файла не более 5 мб</h3>
		</body>
	</html>
	');
}

$section = $SECTION->getSection($item['section_id']);
$catalog = $CATALOG->getItem($section['catalog_id'], true);

$settings = unserialize($catalog['settings']);

if (!array_key_exists('catalog_image_small_resize_method', $settings)) {
	echo json_encode(array('answer' => 'error', 'message' => 'В настройках каталога не указан метод создания малого изображения'));
	exit;
}

if (!array_key_exists('catalog_image_small_w', $settings)) {
	echo json_encode(array('answer' => 'error', 'message' => 'В настройках каталога не указана ширина малого изображения'));
	exit;
}

if (!array_key_exists('catalog_image_small_h', $settings)) {
	echo json_encode(array('answer' => 'error', 'message' => 'В настройках каталога не указана высота малого изображения'));
	exit;
}


// --- ИЗОБРАЖЕНИЕ ---
$dir = $_SERVER['DOCUMENT_ROOT'].'/files/catalog/'.$catalog['id'].'/items';
if(!is_dir($dir))
	mkdir($dir, 0755, true);

if ($image['name'] != '') {
	$item['images'] = date('ymdHis').'.jpg';
	$path = $dir.'/'.$item['images'];

	switch ($settings['catalog_image_small_resize_method']) {
		case '1': // Умный ресайз
			include_once($_SERVER['DOCUMENT_ROOT']."/classes/ImageResize/ImageResizeSmart.php");
			$img_small = new ImageResizeSmart ($image['tmp_name'], $path, $settings['catalog_image_small_w'], $settings['catalog_image_small_h']);
			break;

		case '2': // Подрезка
			include_once($_SERVER['DOCUMENT_ROOT']."/classes/ImageResize/ImageResizeCutting.php");
			$img_small = new ImageResizeCutting ($image['tmp_name'], $path, $settings['catalog_image_small_w'], $settings['catalog_image_small_h']);
			break;

		case '3': // Скукожить
			include_once($_SERVER['DOCUMENT_ROOT']."/classes/ImageResize/ImageResizeCompression.php");
			$img_small = new ImageResizeCompression ($image['tmp_name'], $path, $settings['catalog_image_small_w'], $settings['catalog_image_small_h']);
			break;

		default: // Указанный размер
			include_once($_SERVER['DOCUMENT_ROOT']."/classes/ImageResize/ImageResize.php");
			$img_small = new ImageResize ($image['tmp_name'], $path, $settings['catalog_image_small_w'], $settings['catalog_image_small_h']);
	}

	$img_small->run();
} else 
	$item['images'] = '';


$ITEM->insert($item);

header('location: /admin/com/catalog/section/'.$item['section_id']);

function f_input($name){
	$post_data = isset($_POST[$name]) ? $_POST[$name] : '';
	return trim(htmlspecialchars(strip_tags($post_data)));
}
