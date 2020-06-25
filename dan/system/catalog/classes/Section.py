class Section:
    def __init__(self, SITE):
        self.db = SITE.db
        self._tree_result = []
        self._breadcrumbs_path = []

    def getSection(self, id):
        sql = "SELECT `id`, `catalog_id`, `parent_id`, `name`, `text`, `data`, `status`, `ordering` FROM sections WHERE id = %s"
        self.db.execute(sql, id)
        return self.db.fetchone()

    def getSectionsByCatalogId(self, catalog_id, parent_id = False):
        if parent_id:
            sql = "SELECT `id`, `parent_id`, `name`, `text`, `data`, `status` FROM sections WHERE catalog_id = %s AND parent_id = %s ORDER BY ordering"
            self.db.execute(sql, catalog_id, parent_id)
        else:
            sql = "SELECT `id`, `parent_id`, `name`, `text`, `data`, `status` FROM sections WHERE catalog_id = %s ORDER BY ordering"
            self.db.execute(sql, catalog_id)
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False

    def getItems(self, section_id):
        sql = "SELECT * FROM items WHERE section_id = %s ORDER BY ordering"
        self.db.execute(sql, section_id)
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False

    def insert(self, data):
        sql = "INSERT INTO sections SET `catalog_id` = %s, `parent_id` = %s, `name` = %s, `image` = '', `text` = %s, `data` = %s, `date` = NOW(), `status` = %s, `ordering` = %s"
        return self.db.execute(sql, (
            data['catalog_id'],
            data['parent_id'],
            data['name'],
            data['text'],
            data['data'],
            data['status'],
            data['ordering']
        ))

    def update(self, data):
        sql = "UPDATE sections SET `parent_id` = %s, `name` = %s, `image` = '', `text` = %s, `data` = %s, `date` = NOW(), `status` = %s, `ordering` = %s WHERE id = %s"
        return self.db.execute(sql, (
            data['parent_id'],
            data['name'],
            data['text'],
            data['data'],
            data['status'],
            data['ordering'],
            data['id']
        ))

    def ordering(self, type, id):
        # АЛГОРИТМ РАБОТЫ
        # 1. Находим id каталога по id раздела
        # 2. Создаём список list_id c id и находим порядковый индекс нашего элемента - n
        # 3. Если тип UP - ставим - меняем местами с предыдущим id
        # 4. Если тип DOWN - меняем местами с последующим id
        # Записываем id в БД

        # 1. Находим id каталога по id раздела
        section = self.getSection(id)

        # Получаем список id каталогов
        rows = self.getSectionsByCatalogId(section['catalog_id'], section['parent_id'])
        list_id = []
        i = n = 0

        # 2. Создаём новый список list_1
        for row in rows:
            list_id.append(row['id'])
            if (int(row['id']) == int(id)):
                n = i
            i += 1

        # 3. Если тип UP
        if type == 'up':
            if (n) > 0:
                prev = list_id[n-1]
                list_id[n-1] = int(id)
                list_id[n] = prev

        # 4. Если тип DOWN
        if type == 'down':
            if (n < len(list_id) - 1):
                next = list_id[n+1]
                list_id[n+1] = int(id)
                list_id[n] = next

        for ordering in range(len(list_id)):
            sql = "UPDATE sections SET ordering = %s WHERE id = %s"
            self.db.execute(sql, (ordering + 1, list_id[ordering]))

        return section['catalog_id']
    
    def pub(self, type, id):
        status_dict = {
            'pub': 1, 
            'unpub': 0
        }

        status = status_dict[type]

        sql = "UPDATE sections SET `status` = %s WHERE id = %s"
        self.db.execute(sql, (status, id))

        return self.getSection(id)['catalog_id']
    
    def delete(self, id):
        cat_id = self.getSection(id)['catalog_id']
        rows_all = self.tree(cat_id)

        curent_level = 1000
        rows_delete = []
        for row in rows_all:
            if int(row['id']) == int(id):
                # Если это текущий раздел, запоминаем уровень
                curent_level = row['level']
                rows_delete.append(row['id'])
                continue
            
            if row['level'] > curent_level:
                 # Если опустились ниже на дочерние пункты
                rows_delete.append(row['id'])
            else:
                # Если поднялись до текущего уровня - это означает, что мы прошли все дочерние пункты, сбрасываем curent_level
                curent_level = 1000

        for delete_id in rows_delete:
            sql = "DELETE FROM sections WHERE id = %s"
            self.db.execute(sql, delete_id)
    
        return cat_id


    def tree(self, catalog_id):
        rows = self.getSectionsByCatalogId(catalog_id)
        if rows:
            self._tree_recursion(rows)
        return self._tree_result


    def _tree_recursion(self, rows, parent=0, level=-1):
        level += 1
        for row in rows:
            if int(row['parent_id']) == parent:
                self._tree_result.append({
                    'id': row['id'],
                    'parent_id': row['parent_id'],
                    'name': row['name'],
                    'status': row['status'],
                    'level': level
                })
                self._tree_recursion(rows, row['id'], level)
        return


    def breadcrumbsPath(self, data):
        r = self.getSectionsByCatalogId(data['catalog_id'])
        self._breadcrumbs_recursion(parent_id = data['parent_id'], rows = r)
        return self._breadcrumbs_path


    def _breadcrumbs_recursion(self, parent_id, rows):
        print('parent_id', parent_id)
        for row in rows:
            if int(row['id']) == parent_id:
                self._breadcrumbs_path.append({
                    'id': row['id'],
                    'name': row['name'],
                })
                print('RECURSION')
                self._breadcrumbs_recursion(row['parent_id'], rows)
        return
