<?php
defined('AUTH') or die('Restricted access');
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminAbstract.php';

class AdminCatalogSection extends AdminAbstract
{
	public function insertData($section) 
	{
		global $db;
		$stmt = $db->prepare("
			INSERT INTO com_catalog_sections SET 
				catalog_id = :catalog_id,
				parent_id = :parent_id,
				name = :name,
				settings = '',
				ordering = :ordering,
				pub = :pub
		");
		$stmt->execute(array(
			'catalog_id' => $section['catalog_id'],
			'name' => $section['name'],
			'parent_id' => $section['parent_id'],
			'ordering' => $section['ordering'],
			'pub' => $section['pub']
		));
	}


	public function getItems($section_id)
	{
		global $db;
		$stmt = $db->prepare("SELECT * FROM com_catalog_items WHERE section_id = :section_id ORDER BY ordering");
		$stmt->execute(array('section_id' => $section_id));
		if ($stmt->rowCount() > 0)
			return $stmt->fetchAll();
		return false;
	}


	public function getMaxOrdering($catalog_id)
	{
		global $db;
		$stmt = $db->prepare("SELECT MAX(ordering) FROM com_catalog_sections WHERE catalog_id = :catalog_id");
		$stmt->execute(array('catalog_id' => $catalog_id));
		return $stmt->fetchColumn();
	}


	public function getParentsArr($id)
	{
		global $db, $admin_catalog_section_parent_arr;
		$stmt = $db->prepare("SELECT id, name, parent_id FROM com_catalog_sections WHERE id = :id LIMIT 1");
		$stmt->execute(array('id' => $id));
		if ($stmt->rowCount() > 0) {
			$parent = $stmt->fetch();
			if ($parent['parent_id'] != 0) {
				$admin_catalog_section_parent_arr[] = $parent;
				$this->getParentsArr($parent['parent_id']);
			}	
		}
		return $admin_catalog_section_parent_arr;
	}


	public function getSection($section_id)
	{
		global $db;
		$stmt = $db->prepare("SELECT id, catalog_id, parent_id, name, ordering, pub FROM com_catalog_sections WHERE id = :section_id LIMIT 1");
		$stmt->execute(array('section_id' => $section_id));
		if($stmt->rowCount() > 0)
			return $stmt->fetch();
		return false;
	}


	public function getSectionTree($catalog_id, $parent_id=0, $level=-1)
	{
		global $db, $admin_catalog_section_arr;
		if(!isset($admin_catalog_section_arr))
				$admin_catalog_section_arr = array();

		$stmt = $db->prepare("SELECT id, catalog_id, parent_id, name, ordering, pub FROM com_catalog_sections WHERE catalog_id = :catalog_id AND parent_id = :parent_id ORDER BY ordering");
		$stmt->execute(array('catalog_id' => $catalog_id, 'parent_id' => $parent_id));
		if($stmt->rowCount() > 0) {
			$level++;
			$sections = $stmt->fetchAll();
			foreach ($sections as $section) {
				$section['level'] = $level;
				$admin_catalog_section_arr[] = $section;
				$this->getSectionTree($catalog_id, $section['id'], $level);	
			}
		}
		return $admin_catalog_section_arr;
	}


	public function delete($id)
	{
		global $db;

		$stmt_select = $db->prepare("
				SELECT c.components FROM components c 
				JOIN com_catalog_sections s
				ON c.id = s.catalog_id
				WHERE s.id = :id
			");
		$stmt_select->execute(array('id' => $id));
		$component = $stmt_select->fetchColumn();

		$stmt_delete = $db->prepare("DELETE FROM com_catalog_sections WHERE id = :id");
		$stmt_delete->execute(array('id' => $id));

		$dir = $_SERVER['DOCUMENT_ROOT'].'/files/'.$component.'/sections/'.$id;
		$this->remove_directory($dir);
	}


	public function pub_unpub($arr)
	{
		global $db;
		$stmt = $db->prepare("UPDATE com_catalog_sections SET pub = :pub WHERE id = :id");
		$stmt->execute(array('id' => $arr['id'], 'pub' => $arr['pub']));
	}


	public function ordering($arr)
	{
		global $db;

		// Находим все разделы (братские) с аналогичным родительским разделом
		$stmt = $db->prepare("
			SELECT id FROM com_catalog_sections 
			WHERE parent_id = (
				SELECT parent_id 
				FROM com_catalog_sections
				WHERE id = :id
				LIMIT 1
			)
			ORDER BY  ordering
		");
		$stmt->execute(array('id' => $arr['id']));
		$count = $stmt->rowCount();
		$sections_arr = $stmt->fetchAll();

		// Создаём массив с ключём $i (порядок следовани) и значением $section['id']
		// Находим порядковый уровень нашего раздела
		$arr_order = [];
		$i = 0;
		foreach ($sections_arr as $section) {
			$arr_order[$i] = $section['id'];
			if ($section['id'] == $arr['id'])
				$num = $i;
			$i++;
		}

		// Проверяем допустимость дейсвия
		// Выше поднимать некуда  или ниже опускать некуда - наш элемент первый или последний
		if (($arr['type'] == 'up' && $num <= 0) || ($arr['type'] == 'down' && $num >= $count-1))
			return;

		// Меняем пункты меню в зависимости от действия up / down
		if ($arr['type'] == 'up') {
			$prev = $arr_order[$num - 1];
			$arr_order[$num - 1] = $arr_order[$num];
			$arr_order[$num] = $prev;
		}

		if ($arr['type'] == 'down') {
			$next = $arr_order[$num + 1];
			$arr_order[$num + 1] = $arr_order[$num];
			$arr_order[$num] = $next;
		}
	
		// Записываем новые значения в БД
		$stmt_update = $db->prepare("UPDATE com_catalog_sections SET ordering = :ordering WHERE id = :id");

		foreach ($arr_order as $key => $value) {
			$stmt_update->execute(array('id' => $value, 'ordering' => $key));
		}
	}


	public function updateSection($section)
	{
		global $db;
		$stmt = $db->prepare("
			UPDATE com_catalog_sections SET 
			name = :name,
			parent_id = :parent_id,
			ordering = :ordering,
			pub = :pub
			WHERE id = :id
		");
		$stmt->execute(array(
			'name' => $section['name'],
			'parent_id' => $section['parent_id'],
			'ordering' => $section['ordering'],
			'pub' => $section['pub'],
			'id' => $section['id']
		));
	}
}

?>