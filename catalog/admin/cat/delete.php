<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';

$id = intval($_POST['id']);
if($id == 0 || $_POST['agree'] != 'yes')
	header('location: /admin/com/catalog');

$catalog = new AdminCatalogCat();
$catalog->delete($id);

header('location: /admin/com/catalog');
exit;