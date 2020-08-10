<?php
defined('AUTH') or die('Restricted access');

class AdminAbstract
{
	public function remove_directory($dir) 
	{
		if ($objs = glob($dir."/*")) {
			foreach ($objs as $obj) {
	     		is_dir($obj) ? $this->remove_directory($obj) : unlink($obj);
	   		}
		}
		if (is_dir($dir))
			rmdir($dir);
	}
}