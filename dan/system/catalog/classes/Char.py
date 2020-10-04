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
        return self.db.execute(sql, (
            data['ordering'],
            data['id'],
            data['catalog_id']
        ))

    # Value
    def getValue(self, id):
        sql = "SELECT * FROM com_catalog_char_value WHERE id = %s"
        self.db.execute(sql, id)
        return self.db.fetchone()

    def getValuesByItemId(self, item_id):
        sql = "SELECT v.id, v.item_id, v.name_id, v.value, n.name, n.unit, n.type, n.settings "
        sql += "FROM com_catalog_char_value v "
        sql += "JOIN com_catalog_char_name n "
        sql += "ON n.id = v.name_id "
        sql += "WHERE item_id = %s "
        sql += "ORDER BY v.ordering"
        self.db.execute(sql, item_id)
        rows = self.db.fetchall()
        return rows if rows is not None else False

    def deleteValue(self, id):
        sql = "DELETE FROM com_catalog_char_value WHERE id = %s"
        self.db.execute(sql, id)

    def insertValue(self, data):
        sql = "INSERT INTO com_catalog_char_value SET "
        sql += "item_id = %s, "
        sql += "name_id = %s, "
        sql += "value = %s, "
        sql += "ordering = %s"

        return self.db.execute(sql, (
            data['item_id'],
            data['name_id'],
            data['value'],
            data['ordering']
        ))

    def updateValue(self, data):
        char = self.getValue(data['id'])
        if char['value'] == data['value'] and char['ordering'] == data['ordering']:
            return

        sql = "UPDATE com_catalog_char_value SET "
        sql += "item_id = %s, "
        sql += "name_id = %s, "
        sql += "value = %s, "
        sql += "ordering = %s "
        sql += "WHERE id = %s"

        return self.db.execute(sql, (
            data['item_id'],
            data['name_id'],
            data['value'],
            data['ordering'],
            data['id']
        ))
