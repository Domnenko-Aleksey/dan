class MetallurgyData:
    def __init__(self, SITE):
        self.db = SITE.db
    
    def getAll(self):
        sql = "SELECT * FROM com_metallurgy_data"
        self.db.execute(sql)
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False

    def getRow(self, id):
        sql = "SELECT * FROM com_metallurgy_data WHERE id = %s"
        self.db.execute(sql, row_id)
        rows = self.db.fetchone()
        return rows if len(rows) > 0 else False

    def getDataByItemId(self, item_id):
        self.db.execute("SELECT * FROM com_metallurgy_data WHERE item_id = %s")
        rows = self.db.execute(sql, item_id)
        return rows if len(rows) > 0 else False

    def insert(self, data):
        sql =   "INSERT INTO com_metallurgy_data SET " 
        sql +=  "item_id = %s, p_1 = %s, p_2 = %s, p_3 = %s, p_4 = %s, p_5 = %s, p_6 = %s, p_7 = %s, p_8 = %s, p_9 = %s, p_10 = %s, date=NOW()"
        return self.db.execute(sql, (data['item_id'], data['p_1'], data['p_2'], data['p_3'], data['p_4'], 
            data['p_5'], data['p_6'], data['p_7'], data['p_8'], data['p_9'], data['p_10']
        ))

    def update(self, data):
        sql = "UPDATE com_metallurgy_data SET "
        sql +=  "item_id = %s, p_1 = %s, p_2 = %s, p_3 = %s, p_4 = %s, p_5 = %s, p_6 = %s, p_7 = %s, p_8 = %s, p_9 = %s, p_10 = %s, date=NOW() " 
        return self.db.execute(sql, (data['item_id'], data['p_1'], data['p_2'], data['p_3'], data['p_4'], 
            data['p_5'], data['p_6'], data['p_7'], data['p_8'], data['p_9'], data['p_10']
        ))

    def delete(self, row_id):
        sql = "DELETE FROM com_metallurgy_data WHERE id = %s"
        return self.db.execute(sql, row_id)
