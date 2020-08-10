<?php
defined('AUTH') or die('Restricted access');

include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminCatalogCat.php';

if($SITE->d[4] == 'pub')
	$enabled = 1;
else
	$enabled = 0;

$catalog = new AdminCatalogCat();
$catalog->setEnabled($SITE->d[5], $enabled);

header('location: /admin/com/catalog');
