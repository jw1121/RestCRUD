import sqlite3


class MarketModel(object):

    def __init__(self, database="../docs/market.db"):
        self.database = database

        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()

    def insertMarket(self, data):
        sql_str = ("INSERT INTO market({0}) VALUES('{1}')").format(data[0], data[1])
        print(sql_str)
        self.cur.execute(sql_str, "") # Parameter is not optional
        self.conn.commit()
        self.conn.close()
        return True

    def getMarket(self, id):
        self.cur.execute("select * from market where FMID = :FMID", {'FMID': id})
        data = self.cur.fetchone()
        self.conn.close()
        return data.__str__()

    def updateMarket(self, data):
        sql_str = ("UPDATE market SET {0} WHERE = {1}").format(data[0], data[1])
        print(sql_str)
        self.cur.execute(sql_str, "")  # Parameter is not optional
        self.conn.commit()
        self.conn.close()
        return True

    def deleteMarket(self, data):
        sql_str = ("DELETE FROM market WHERE {0} = {1}").format(data[0], data[1])
        print(sql_str)
        self.cur.execute(sql_str, "")  # Parameter is not optional
        self.conn.commit()
        self.conn.close()
        return True

