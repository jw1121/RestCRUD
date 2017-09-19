from flask.views import MethodView
from flask import request
from .sqlite import MarketModel


class MarketUpdate(MethodView):

    def put(self,id):
        jsony = request.get_json()

        print(jsony)
        model = MarketModel()
        data = model.updateMarket(id, self.parse(jsony))
        return ""

    def parse(self, data):
        sets = ', '.join([key + "='" + value + "'" for key, value in data.items()])
        return sets
