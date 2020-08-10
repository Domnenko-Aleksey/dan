<?php
defined('AUTH') or die('Restricted access');

class AdminCatalogChar
{
	public function delete($id) 
	{
		global $db;
		$stmt = $db->prepare("SELECT catalog_id FROM com_catalog_char_name WHERE id = :id");
		$stmt->execute(array('id' => $id));

		$catalog_id = $stmt->fetchColumn();

		$stmt = $db->prepare("DELETE FROM com_catalog_char_name WHERE id = :id");
		$stmt->execute(array('id' => $id));

		return $catalog_id;
	}

	public function getCharName($id)
	{
		global $db;
		$stmt = $db->prepare("SELECT * FROM com_catalog_char_name WHERE id = :id");
		$stmt->execute(array('id' => $id));
		if ($stmt->rowCount() > 0)
			return $stmt->fetch();
		return false;
	}

	public function getCharNameList($catalog_id)
	{
		global $db;
		$stmt = $db->prepare("SELECT * FROM com_catalog_char_name WHERE catalog_id = :catalog_id ORDER BY ordering");
		$stmt->execute(array('catalog_id' => $catalog_id));
		if ($stmt->rowCount() > 0)
			return $stmt->fetchAll();
		return false;
	}

	public function getMaxOrdering($catalog_id)
	{
		global $db;
		$stmt = $db->prepare("SELECT MAX(ordering) FROM com_catalog_char_name WHERE catalog_id = :catalog_id");
		$stmt->execute(array('catalog_id' => $catalog_id));
		return $stmt->fetchColumn();
	}

	public function insert($char)
	{
		global $db;
		$stmt = $db->prepare("
			INSERT INTO com_catalog_char_name SET
			catalog_id = :catalog_id,
			identifier = :identifier,
			name = :name,
			unit = :unit,
			type = :type,
			settings = :settings,
			ordering = :ordering
		");
		$stmt->execute(array(
			'catalog_id' => $char['catalog_id'],
			'identifier' => $char['identifier'],
			'name' => $char['name'],
			'unit' => $char['unit'],
			'type' => $char['type'],
			'settings' => $char['settings'],
			'ordering' => $char['ordering']
		));
	}

	public function update($char)
	{
		global $db;
		$stmt = $db->prepare("
			UPDATE com_catalog_char_name SET
			identifier = :identifier,
			name = :name,
			unit = :unit,
			type = :type,
			ordering = :ordering
			WHERE id = :id
		");
		$stmt->execute(array(
			'identifier' => $char['identifier'],
			'name' => $char['name'],
			'unit' => $char['unit'],
			'type' => $char['type'],
			'ordering' => $char['ordering'],
			'id' => $char['id']
		));
	}

	public function updateOrdering($char) {
		global $db;
		$stmt = $db->prepare("
			UPDATE com_catalog_char_name SET
			ordering = :ordering
			WHERE id = :id AND catalog_id = :catalog_id
		");
		$stmt->execute(array(
			'ordering' => $char['ordering'],
			'id' => $char['id'],
			'catalog_id' => $char['catalog_id']
		));		
	}
}