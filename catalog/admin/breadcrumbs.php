<?php
defined('AUTH') or die('Restricted access');

function breadcrumbs($arr)
{
	global $SITE;

	$out = '';
	$svg = ' <svg><use xlink:href="/administrator/template/sprite.svg#arrow_right_1"></use></svg>';
	$svg_home = '<a href="/admin"><svg class="home"><use xlink:href="/administrator/template/sprite.svg#home"></use></svg></a>';
	foreach ($arr as $key => $value) {
		if($key == 'none')
			$out .= $svg.'<span>'.$value.'</span>';
		else
			$out .= $svg.'<a href="'.$key.'">'.$value.'</a>';
	}

	return '<div class="breadcrumbs">'.$svg_home.$out.'</div>';
}

?>