class Keyword:
    def __init__(self, SITE):
        self.db = SITE.db

    def keywordList(self):
        sql = "SELECT * FROM com_bot_keyword WHERE id > %s ORDER BY keyword"
        self.db.execute(sql, 0)
        rows = self.db.fetchall()
        return rows if rows is not None else False