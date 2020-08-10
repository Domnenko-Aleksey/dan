<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';
$id = $SITE->d[5];
$catalog = new AdminCatalogCat();

if(isset($_POST['cancel'])){
	header('location: /admin/com/catalog/cat/');
	exit;
}

$cat = $catalog->getItem($id, true);
$settings = unserialize($cat['settings']);

// Catalog
$enabled = input_str('enabled');
$settings['catalog_image_small_resize_method'] = input_int('catalog_image_small_resize_method');
if(!$settings['catalog_image_small_resize_method'])
	$settings['catalog_image_small_resize_method'] = 1;
$settings['catalog_image_small_w'] = input_int('catalog_image_small_w');
if($settings['catalog_image_small_w'] < 100)
	$settings['catalog_image_small_w'] = 100;
if($settings['catalog_image_small_w'] > 500)
	$settings['catalog_image_small_w'] = 500;
$settings['catalog_image_small_h'] = input_int('catalog_image_small_h');
if($settings['catalog_image_small_h'] < 100)
	$settings['catalog_image_small_h'] = 100;
if($settings['catalog_image_small_h'] > 500)
	$settings['catalog_image_small_h'] = 500;
$settings['catalog_image_big_w'] = input_int('catalog_image_big_w');
if($settings['catalog_image_big_w'] < 100)
	$settings['catalog_image_big_w'] = 100;
if($settings['catalog_image_big_w'] > 500)
	$settings['catalog_image_big_w'] = 500;
$settings['catalog_image_big_h'] = input_int('catalog_image_big_h');
if($settings['catalog_image_big_h'] < 100)
	$settings['catalog_image_big_h'] = 100;
if($settings['catalog_image_big_h'] > 500)
	$settings['catalog_image_big_h'] = 500;
$settings['catalog_3d_model'] = input_int('catalog_3d_model');
$settings['catalog_3d_sprite'] = input_int('catalog_3d_sprite');
$settings['catalog_360'] = input_int('catalog_360');

// Section
$settings['section_display_type'] = input_int('section_display_type');
$settings['section_preview_w'] = input_int('section_preview_w');
$settings['section_preview_h'] = input_int('section_preview_h');
$settings['section_quantity_item'] = input_int('section_quantity_item');
$settings['section_product_card'] = input_int('section_product_card');
$settings['section_sorting'] = input_int('section_sorting');
$settings['section_sub_display'] = input_int('section_sub_display');
$settings['section_sub_items_display'] = input_int('section_sub_items_display');
$settings['section_grouping'] = input_int('section_grouping');

// Elements
$settings['item_product_card'] = input_int('item_product_card');
$settings['item_question'] = input_int('item_question');

// Shop
if (input_str('shop_on') != '') {
	$settings['shop'] = array();
} else {
	unset($settings['shop']);
}

$settings['shop_name'] = input_str('shop_name');
$settings['shop_company_name'] = input_str('shop_company_name');
$settings['shop_delivery'] = input_str('shop_delivery');
$settings['shop_currency'] = input_str('shop_currency');
$settings['shop_inner_course_ue'] = input_str('shop_inner_course_ue');
$settings['shop_buy_1_click'] = input_int('shop_buy_1_click');
$settings['shop_quantity_accounting'] = input_int('shop_quantity_accounting');
$settings['shop_packaging'] = input_int('shop_packaging');
$settings['shop_basket_type'] = input_str('shop_basket_type');
$settings['shop_price_type'] = input_int('shop_price_type');
$settings['shop_1c_psw'] = input_str('shop_1c_psw');
$settings['shop_1c_db_reset'] = input_int('shop_1c_db_reset');
$settings['shop_1с_quantity_only'] = input_int('shop_1с_quantity_only');

$s = serialize($settings);
$catalog->updateSettings($id, $s, $enabled);

header('location: /admin/com/catalog/cat/settings_edit/'.$id);


function input_str($name){
	$post_data = isset($_POST[$name]) ? $_POST[$name] : '';
	return trim(htmlspecialchars(strip_tags($post_data)));
}

function input_int($name){
	$post_data = isset($_POST[$name]) ? $_POST[$name] : 0;
	return trim(htmlspecialchars(strip_tags($post_data)));
}