<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogSection.php';

$id = intval($_POST['id']);
if($id == 0 || $_POST['agree'] != 'yes')
	header('location: /admin/com/catalog');

$section = new AdminCatalogSection();
$section_data = $section->getSection($id);
$section->delete($id);

echo json_encode(array('answer' => 'success', 'catalog_id' => $section_data['catalog_id']));
exit;