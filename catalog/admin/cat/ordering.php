<?php
defined('AUTH') or die('Restricted access');

if(isset($_POST['cancel']))
	header('location: /admin/com/catalog');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';

$catalog = new AdminCatalogCat();

$act = $SITE->p[4];
$id = $SITE->p[5];

$catalog->ordering($act, $id);

header('location: /admin/com/catalog');
