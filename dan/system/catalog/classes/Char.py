class Char:
    def __init__(self, SITE):
        self.db = SITE.db

    def deleteName(self, id):
        c = self.getName(id)

        sql = "DELETE FROM com_catalog_char_name WHERE id = %s"
        self.db.execute(sql, id)

        # sql = "DELETE FROM com_catalog_char_value WHERE name_id = %s"
        # self.db.execute(sql, data['id'])

        return c['catalog_id']

    def getName(self, item_id):
        sql = "SELECT * FROM com_catalog_char_name WHERE id = %s"
        self.db.execute(sql, item_id)
        return self.db.fetchone()

    def getNameList(self, catalog_id):
        sql = "SELECT * FROM com_catalog_char_name WHERE catalog_id = %s ORDER BY ordering"
        self.db.execute(sql, catalog_id)
        rows = self.db.fetchall()
        return rows if rows is not None else False

    def getNameMaxOrdering(self, catalog_id):
        sql = "SELECT MAX(ordering) max_ordering FROM com_catalog_char_name WHERE catalog_id = %s"
        self.db.execute(sql, catalog_id)
        mo = self.db.fetchone()
        return mo['max_ordering'] if mo['max_ordering'] is not None else 0

    def insertName(self, data):
        sql = "INSERT INTO com_catalog_char_name SET catalog_id = %s, name = %s, unit = %s, type = %s, settings = '', ordering = %s"

        return self.db.execute(sql, (
			data['catalog_id'],
			data['name'],
			data['unit'],
			data['type'],
			data['ordering']
        ))

    def updateName(self, data):
        sql = "UPDATE com_catalog_char_name SET name = %s, unit = %s, type = %s, ordering = %s WHERE id = %s"

        return self.db.execute(sql, (
			data['name'],
			data['unit'],
			data['type'],
			data['ordering'],
            data['id']
        ))

    def updateNameOrdering(self, data):
        sql = "UPDATE com_catalog_char_name SET ordering = %s WHERE id = %s AND catalog_id = %s"
        print('--DATA--', data)
        return self.db.execute(sql, (
			data['ordering'],
            data['id'],
            data['catalog_id']
        ))