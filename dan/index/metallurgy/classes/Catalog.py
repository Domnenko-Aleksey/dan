class Catalog:
    def __init__(self, SITE):
        self.db = SITE.db

    def getSection(self, id):
        sql = "SELECT `id`, `catalog_id`, `parent_id`, `name`, `text`, `data`, `status`, `ordering` FROM com_catalog_sections WHERE id = %s"
        self.db.execute(sql, id)
        return self.db.fetchone()

    def getSectionsByCatalogId(self, data):
        if data['parent_id']:
            sql = "SELECT `id`, `parent_id`, `name`, `text`, `data`, `status` FROM com_catalog_sections WHERE catalog_id = %s AND parent_id = %s ORDER BY ordering"
            self.db.execute(sql, (data['catalog_id'], data['parent_id']))
        else:
            sql = "SELECT `id`, `parent_id`, `name`, `text`, `data`, `status` FROM com_catalog_sections WHERE catalog_id = %s ORDER BY ordering"
            self.db.execute(sql, data['catalog_id'])
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False

    def getItems(self, section_id):
        sql = "SELECT * FROM com_catalog_items WHERE section_id = %s ORDER BY ordering"
        self.db.execute(sql, section_id)
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False