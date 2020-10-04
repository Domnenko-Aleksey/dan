class Catalog:
    def __init__(self, SITE):
        self.db = SITE.db

    def getItem(self, id):
        sql = "SELECT * FROM com_catalog_items WHERE id = %s"
        self.db.execute(sql, id)
        return self.db.fetchone()

    def getSectionItems(self, section_id, chars=False):
        if chars:
            sql = "SELECT id, name, image, text FROM com_catalog_items WHERE section_id = %s ORDER BY ordering"
            self.db.execute(sql, section_id)
            items = self.db.fetchall()
            if len(items) == 0:
                return false
            for item in items:
                chars = self.getCharsByItemId(item['id'])
                if chars:
                    chars_dict = {}
                    for char in chars:
                        if char['name'] not in chars_dict:
                            chars_dict[char['name']] = {
                                'unit': char['unit'],
                                'type': char['type'],
                                'values': [char['value']]
                            }
                        else:
                            chars_dict[char['name']]['values'].append(char['value'])
                item['chars'] = chars_dict
            return items
        else:
            sql = "SELECT id, name, image, text FROM com_catalog_items WHERE section_id = %s ORDER BY ordering"
            self.db.execute(sql, section_id)
            rows = self.db.fetchall()
            return rows if len(rows) > 0 else False

    def getMaxOrdering(self):
        self.db.execute(
            "SELECT MAX(ordering) mo FROM com_catalog_items ORDER BY ordering")
        return self.db.fetchone()['mo']

    def getCatalogIdBySectionId(self, section_id):
        sql = "SELECT catalog_id FROM com_catalog_sections WHERE id = %s"
        self.db.execute(sql, section_id)
        return self.db.fetchone()['catalog_id']
    
    def getCharsByItemId(self, item_id):
        sql =   "SELECT v.value, n.name, n.unit, n.type "
        sql +=  "FROM com_catalog_char_value v "
        sql +=  "JOIN com_catalog_char_name n ON n.id = v.name_id "
        sql +=  "WHERE v.item_id = %s ORDER BY v.ordering"
        self.db.execute(sql, item_id)
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False
