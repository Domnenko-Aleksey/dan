<?php
defined('AUTH') or die('Restricted access');
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminAbstract.php';

class AdminCatalogItem extends AdminAbstract
{
	public function addImage($item)
	{
		global $db;

		$item_select = $this->getItem($item['id']);
		$images = $item_select['images'] == '' ? $item['images'] : $item_select['images'].';'.$item['images'];

		$stmt_update = $db->prepare("UPDATE com_catalog_items SET images = :images WHERE id = :id");
		$stmt_update->execute(array('images' => $images, 'id' => $item['id']));
	}

	public function getCatalogByItemId($id)
	{
		global $db;
		$stmt = $db->prepare("
			SELECT id, settings FROM components WHERE id IN (
				SELECT catalog_id FROM com_catalog_sections WHERE id IN (
					SELECT section_id FROM com_catalog_items WHERE id = :id
				)
			)
		");
		$stmt->execute(array('id' => $id));
		return $stmt->fetch();
	}

	public function getItem($id)
	{
		global $db;
		$stmt = $db->prepare("SELECT * FROM com_catalog_items WHERE id = :id");
		$stmt->execute(array('id' => $id));
		if ($stmt->rowCount() > 0)
			return $stmt->fetch();
		return false;
	}

	public function getMaxOrdering($section_id)
	{
		global $db;
		$stmt = $db->prepare("SELECT MAX(ordering) FROM com_catalog_items WHERE section_id = :section_id");
		$stmt->execute(array('section_id' => $section_id));
		return $stmt->fetchColumn();
	}

	public function delete($id)
	{
		global $db;

		$stmt = $db->prepare("DELETE FROM com_catalog_items WHERE id = :id");
		$stmt->execute(array('id' => $id));

		// $dir = $_SERVER['DOCUMENT_ROOT'].'/files/'.$component.'/sections/'.$id;
		// $this->remove_directory($dir);
	}


	public function insert($item)
	{
		global $db;

		$stmt = $db->prepare("
			INSERT INTO com_catalog_items SET
			section_id = :section_id,
			name = :name,
			images = :images,
			`text` = :txt,
			settings = :settings,
			`date` = NOW(),
			ordering = :ordering,
			pub = :pub
		");

		$stmt->execute(array(
			'section_id' => $item['section_id'],
			'name' => $item['name'],
			'images' => $item['images'],
			'txt' => $item['text'],
			'settings' => $item['settings'],
			'ordering' => $item['ordering'],
			'pub' => $item['pub']
		));
	}


	public function ordering($arr)
	{
		global $db;

		$stmt = $db->prepare("
			SELECT id FROM com_catalog_items 
			WHERE section_id = (
				SELECT section_id 
				FROM com_catalog_items
				WHERE id = :id
				LIMIT 1
			)
			ORDER BY  ordering
		");
		$stmt->execute(array('id' => $arr['id']));
		$count = $stmt->rowCount();
		$items_arr = $stmt->fetchAll();

		// Создаём массив с ключём $i (порядок следовани) и значением $section['id']
		// Находим порядковый уровень нашего раздела
		$arr_order = [];
		$i = 0;
		foreach ($items_arr as $section) {
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
		$stmt_update = $db->prepare("UPDATE com_catalog_items SET ordering = :ordering WHERE id = :id");

		foreach ($arr_order as $key => $value) {
			$stmt_update->execute(array('id' => $value, 'ordering' => $key));
		}
	}


	public function pub_unpub($arr)
	{
		global $db;
		$stmt = $db->prepare("UPDATE com_catalog_items SET pub = :pub WHERE id = :id");
		$stmt->execute(array('id' => $arr['id'], 'pub' => $arr['pub']));
	}


	public function update($item)
	{
		global $db;

		$stmt = $db->prepare("
			UPDATE com_catalog_items SET 
			section_id = :section_id,
			name = :name,
			images = :images,
			`text` = :txt,
			`date` = NOW(),
			ordering = :ordering,
			pub = :pub
			WHERE id = :id
		");

		$stmt->execute(array(
			'section_id' => $item['section_id'],
			'name' => $item['name'],
			'images' => $item['images'],
			'txt' => $item['text'],
			'ordering' => $item['ordering'],
			'pub' => $item['pub'],
			'id' => $item['id']
		));
	}

	public function updateImages($item)
	{
		global $db;

		$stmt_update = $db->prepare("UPDATE com_catalog_items SET images = :images WHERE id = :id");
		$stmt_update->execute(array('images' => $item['images'], 'id' => $item['id']));
	}
}