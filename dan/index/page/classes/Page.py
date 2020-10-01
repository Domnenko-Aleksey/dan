class Page:
    def __init__(self, SITE):
        self.db = SITE.db

    def getPage(self, id):
        sql = "SELECT * FROM pages WHERE id = %s"
        self.db.execute(sql, id)
        return self.db.fetchone()

