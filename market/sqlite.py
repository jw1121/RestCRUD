import sqlite3


class MarketModel(object):

    def __init__(self, database="../docs/market.db"):
        self.database = database

        conn = sqlite3.connect(self.database)
        self.cursor = conn.cursor()

    def insertMarket(self):
        pass

    def getMarket(self):
        self.cursor.execute("select * from market")
        data = self.cursor.fetchone()
        return data.__str__()

    def updateMarket(self):
        pass

    def deleteMarket(self):
        pass
