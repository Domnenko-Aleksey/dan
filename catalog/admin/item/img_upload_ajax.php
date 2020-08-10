<?php
defined('AUTH') or die('Restricted access');
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogItem.php';
$ITEM = new AdminCatalogItem();

$id = intval($_POST['id']);
$img_src = $_POST['img_src'];

set_time_limit(60);
ini_set('memory_limit', '1024M');
$memory_limit = get_cfg_var('memory_limit');
$memory_limit = (real)$memory_limit;

$catalog = $ITEM->getCatalogByItemId($id);

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


$dir = $_SERVER['DOCUMENT_ROOT'].'/files/catalog/'.$catalog['id'].'/items';
if(!is_dir($dir))
	mkdir($dir, 0755, true);

$img_name = date('ymdHis').'.jpg';
$path = $dir.'/'.$img_name;


switch ($settings['catalog_image_small_resize_method']) {
	case '1': // Умный ресайз
		include_once($_SERVER['DOCUMENT_ROOT']."/classes/ImageResize/ImageResizeSmart.php");
		$img_small = new ImageResizeSmart ($img_src, $path, $settings['catalog_image_small_w'], $settings['catalog_image_small_h']);
		break;

	case '2': // Подрезка
		include_once($_SERVER['DOCUMENT_ROOT']."/classes/ImageResize/ImageResizeCutting.php");
		$img_small = new ImageResizeCutting ($img_src, $path, $settings['catalog_image_small_w'], $settings['catalog_image_small_h']);
		break;

	case '3': // Скукожить
		include_once($_SERVER['DOCUMENT_ROOT']."/classes/ImageResize/ImageResizeCompression.php");
		$img_small = new ImageResizeCompression ($img_src, $path, $settings['catalog_image_small_w'], $settings['catalog_image_small_h']);
		break;

	default: // Указанный размер
		include_once($_SERVER['DOCUMENT_ROOT']."/classes/ImageResize/ImageResize.php");
		$img_small = new ImageResize ($img_src, $path, $settings['catalog_image_small_w'], $settings['catalog_image_small_h']);
}

$img_small->run();

$item['id'] = $id;
$item['images'] = $img_name;
$ITEM->addImage($item);

echo json_encode(array(
	'answer' => 'success', 
	'img_name' => $img_name, 
	'img_path' => '/files/catalog/'.$catalog['id'].'/items/'.$img_name
));
exit;