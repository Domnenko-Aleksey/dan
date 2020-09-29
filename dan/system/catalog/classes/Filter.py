class Filter:
    def __init__(self, SITE):
        self.db = SITE.db

    def delete(self, id):
        sql = "DELETE FROM com_catalog_filter WHERE id = %s"
        self.db.execute(sql, id)

    def getFilter(self, item_id):
        sql = "SELECT * FROM com_catalog_filter WHERE id = %s"
        self.db.execute(sql, item_id)
        row = self.db.fetchone()
        return row if row is not None else False

    def getNameMaxOrdering(self, section_id):
        sql = "SELECT MAX(ordering) max_ordering FROM com_catalog_filter WHERE filter_id = %s"
        self.db.execute(sql, section_id)
        mo = self.db.fetchone()
        return mo['max_ordering'] if mo['max_ordering'] is not None else 0

    def insert(self, data):
        sql = "INSERT INTO com_catalog_filter SET section_id = %s, char_id = %s, value_1 = %s, value_2 = %s, settings = '', ordering = %s"
        return self.db.execute(sql, (
            data['section_id'],
            data['char_id'],
            data['value_1'],
            data['value_2'],
            data['ordering']
        ))

    def update(self, data):
        sql = "UPDATE com_catalog_filter SET section_id = %s, char_id = %s, value_1 = %s, value_2 = %s, settings = '', ordering = %s WHERE id = %s"
        return self.db.execute(sql, (
            data['section_id'],
            data['char_id'],
            data['value_1'],
            data['value_2'],
            data['ordering'],
            data['id']
        ))

    def getFiltersBySectionId(self, section_id):
        sql = "SELECT f.id, f.section_id, f.char_id, f.value_1, f.value_2, f.ordering, c.id name_id, c.name, c.unit, c.type "
        sql += "FROM com_catalog_filter f "
        sql += "JOIN com_catalog_char_name c "
        sql += "ON c.id = f.char_id "
        sql += "WHERE section_id = %s "
        sql += "ORDER BY f.ordering"
        self.db.execute(sql, section_id)
        rows = self.db.fetchall()
        return rows if rows is not None else False
