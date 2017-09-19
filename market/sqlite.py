import sqlite3


class MarketModel(object):

    def __init__(self, database="market.db"):
        self.database = database

        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

    def insertMarket(self):
        pass

    def getMarket(self):
        pass

    def updateMarket(self):
        pass

    def deleteMarket(self):
        pass

