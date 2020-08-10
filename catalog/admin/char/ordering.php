<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogChar.php';

$CHAR = new AdminCatalogChar();

$char['catalog_id'] = (int)$_POST['catalog_id'];
$char_id_arr = explode(',', $_POST['char_id_list']);

$ordering = 1;
foreach ($char_id_arr as $char_id) {
	$char['id'] = $char_id;
	$char['ordering'] = $ordering;
	$CHAR->updateOrdering($char);
	$ordering++;
}

echo json_encode(array('answer' => 'success'));
exit;