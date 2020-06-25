class Item:
    def __init__(self, SITE):
        self.db = SITE.db


    def getItem(self, item_id):
        sql = "SELECT * FROM items WHERE id = %s"
        self.db.execute(sql, item_id)
        return self.db.fetchone()


    def insert(self, data):
        sql = "INSERT INTO items SET `section_id` = %s, `name` = %s, `image` = '', `text` = %s, `data` = %s, `date` = NOW(), `status` = %s, `ordering` = %s"
        return self.db.execute(sql, (
            data['section_id'],
            data['name'],
            data['text'],
            data['data'],
            data['status'],
            data['ordering']
        ))


    def update(self, data):
        sql = "UPDATE items SET `name` = %s, `text` = %s, `data` = %s, `date` = NOW(), `status` = %s, `ordering` = %s WHERE id = %s"
        return self.db.execute(sql, (
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

        # Получаем список id раздела


        sql = "SELECT section_id FROM items WHERE id = %s"
        self.db.execute(sql, id)
        row = self.db.fetchone()
        section_id = row['section_id']

        sql_s = "SELECT id FROM items WHERE section_id = %s"
        self.db.execute(sql_s, section_id)
        rows = self.db.fetchall()

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
            sql = "UPDATE items SET ordering = %s WHERE id = %s"
            self.db.execute(sql, (ordering + 1, list_id[ordering]))

        return section_id

    def getMaxOrdering(self, section_id):
        sql = "SELECT MAX(ordering) ord FROM items WHERE section_id = %s"
        self.db.execute(sql, section_id)
        row = self.db.fetchone()
        return row['ord'] if len(row) > 0 else 1

    
    def pub(self, type, id):
        status_dict = {
            'pub': 1, 
            'unpub': 0
        }

        status = status_dict[type]

        sql = "UPDATE items SET `status` = %s WHERE id = %s"
        self.db.execute(sql, (status, id))

        return self.getItem(id)['section_id']
    
    def delete(self, id):
        item = self.getItem(['id', 'section_id'])
        sql = "DELETE FROM items WHERE id = %s"
        self.db.execute(sql, item['section_id'])
    
        return cat_id
