<?php
defined('AUTH') or die('Restricted access');
include_once $_SERVER['DOCUMENT_ROOT'].'/components/catalog/admin/classes/AdminAbstract.php';

class AdminCatalogCat extends AdminAbstract
{
	public function insertData($data) 
	{
		global $db;
		$settings = serialize($data['settings']);
		$stmt = $db->prepare("
			INSERT INTO components SET 
				components = :components,
				type = 'catalog',
				title = :title,
				settings = :settings,
				ordering = :ordering,
				enabled = 1
		");
		$stmt->execute(array(
			'components' => $data['url'],
			'title' => $data['title'],
			'settings' => $settings,
			'ordering' => $data['ordering']
		));
	}

	
	public function getItem($id, $settings = false)
	{
		global $db;
		if($settings){
			$sql_select = 'settings,';
		} else {
			$sql_select = '';			
		}
		$stmt = $db->prepare("SELECT id, components, title, ".$sql_select." ordering, enabled FROM components WHERE id = :id AND type = 'catalog'");
		$stmt->execute(array('id' => $id));
		if ($stmt->rowCount() > 0)
			return $stmt->fetch();
		else
			return false;
	}

	
	public function getItems($settings = false)
	{
		global $db;
		$sql_settings = $settings ? 'settings,' : '';
		$sql = "SELECT id, components, title, ".$sql_settings." enabled FROM components WHERE type = 'catalog' ORDER BY ordering";
		$query = $db->query($sql);
		if ($query->rowCount() > 0)
			return $query->fetchAll();
		return false;
	}


	public function delete($id)
	{
		global $db;
		$stmt_select = $db->prepare("SELECT components FROM components WHERE id = :id");
		$stmt_select->execute(array('id' => $id));
		$component = $stmt_select->fetchColumn();
		$stmt_delete = $db->prepare("DELETE FROM components WHERE id = :id");
		$stmt_delete->execute(array('id' => $id));
		$dir = $_SERVER['DOCUMENT_ROOT'].'/files/'.$component;
		$this->remove_directory($dir);
	}


	public function maxOrdering()
	{
		global $db;
		$query = $db->query("SELECT MAX(ordering) FROM components");
		return $query->fetchColumn();
	}


	public function ordering($act, $id)
	{    
		# АЛГОРИТМ РАБОТЫ
	    # 1. Создаём массив list_id c id и находим порядковый индекс нашего элемента - n
	    # 2. Если тип UP - ставим - меняем местами с предыдущим id
	    # 3. Если тип DOWN - меняем местами с последующим id
	    # Записываем id в БД
	    global $db;

	    $rows = $this->getItems();
	    $list_id = [];
	    $i = $n = 0;

	    # 1. Создаём новый список list_id
	    foreach ($rows as $row) {
	    	$list_id[] = $row['id'];
	    	if ($row['id'] == $id)
	    		$n = $i;
	    	$i++;
	    }

        # 2. Если тип UP
        if ($act == 'up') {
            if ($n > 0) {
                $prev = $list_id[$n-1];
                $list_id[$n-1] = $id;
                $list_id[$n] = $prev;
            }
        }

        # 3. Если тип DOWN
        if ($act == 'down') {
            if ($n < count($list_id) - 1) {
                $next = $list_id[$n + 1];
                $list_id[$n + 1] = $id;
                $list_id[$n] = $next;
            }
        }

        for ($i = 0; $i < count($list_id); $i++) {
        	$stmt = $db->prepare("UPDATE components SET ordering = :ordering WHERE id = :id AND type = 'catalog'");
        	$stmt->execute(array('ordering' => $i, 'id' => $list_id[$i]));
        }
	}


	public function setEnabled($id, $enable)
	{
		global $db;
		$stmt = $db->prepare('UPDATE components SET enabled = :enable WHERE id = :id');
		$stmt->execute(array('id' => $id, 'enable' => intval($enable)));
	}

	
	public function updateData($data) 
	{
		global $db;
		$stmt = $db->prepare("
			UPDATE components SET 
				components = :components,
				title = :title,
				ordering = :ordering
				WHERE id = :id AND type = 'catalog'
		");
		$stmt->execute(array(
			'components' => $data['url'],
			'title' => $data['title'],
			'ordering' => $data['ordering'],
			'id' => $data['id']
		));
	}


	public function updateSettings($id, $settings, $enabled) 
	{
		global $db;
		$stmt = $db->prepare("
			UPDATE components SET 
				settings = :settings,
				enabled = :enabled
				WHERE id = :id
		");
		$stmt->execute(array(
			'settings' => $settings,
			'enabled' => $enabled,
			'id' => $id
		));
	}
}

?>