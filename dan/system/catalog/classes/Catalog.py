class Catalog:
    def __init__(self, SITE):
        self.db = SITE.db

    def getItem(self, id):
        sql = "SELECT * FROM component WHERE id = %s"
        self.db.execute(sql, id)
        return self.db.fetchone()

    def getItems(self):
        self.db.execute("SELECT * FROM component ORDER BY ordering")
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False

    def getMaxOrdering(self):
        self.db.execute(
            "SELECT MAX(ordering) mo FROM component ORDER BY ordering")
        return self.db.fetchone()['mo']

    def checkUrl(self, new_url, current_url=''):
        if new_url == '':
            return False
        sql = "SELECT id FROM component WHERE url = %s AND url != %s LIMIT 1"
        self.db.execute(sql, (new_url, current_url))
        return self.db.fetchone()

    def insert(self, data):
        sql = "INSERT INTO component SET component = 'catalog', `url` = %s, `name` = %s, settings = '', ordering = %s"
        return self.db.execute(sql, (data['url'], data['name'], data['ordering']))

    def update(self, data):
        sql = "UPDATE component SET `url` = %s, `name` = %s, ordering = %s WHERE id = %s"
        return self.db.execute(sql, (data['url'], data['name'], data['ordering'], data['id']))

    def ordering(self, type, id):
        # АЛГОРИТМ РАБОТЫ
        # 1. Создаём список list_id c id и находим порядковый индекс нашего элемента - n
        # 2. Если тип UP - ставим - меняем местами с предыдущим id
        # 3. Если тип DOWN - меняем местами с последующим id
        # Записываем id в БД

        rows = self.getItems()  # Получаем список id каталогов
        list_id = []
        i = n = 0

        # 1. Создаём новый список list_1
        for row in rows:
            list_id.append(row['id'])
            if (int(row['id']) == int(id)):
                n = i
            i += 1

        # 2. Если тип UP
        if type == 'up':
            if (n) > 0:
                prev = list_id[n-1]
                list_id[n-1] = int(id)
                list_id[n] = prev

        # 3. Если тип DOWN
        if type == 'down':
            if (n < len(list_id) - 1):
                next = list_id[n+1]
                list_id[n+1] = int(id)
                list_id[n] = next

        for ordering in range(len(list_id)):
            sql = "UPDATE component SET ordering = %s WHERE id = %s"
            self.db.execute(sql, (ordering + 1, list_id[ordering]))

    def delete(self, id):
        sql = "DELETE FROM component WHERE id = %s"
        return self.db.execute(sql, id)

    def settingsUpdate(self, id, settings):
        sql = "UPDATE component SET `settings` = %s WHERE id = %s"
        return self.db.execute(sql, (settings, id))

    def getSections(self, catalog_id, short=True):
        if short:
            sql = "SELECT id, parent_id, name, status FROM sections WHERE catalog_id = %s ORDER BY ordering"
        else:
            sql = "SELECT * FROM com_catalog_sections WHERE catalog_id = %s ORDER BY ordering"
        self.db.execute(sql, catalog_id)
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False
