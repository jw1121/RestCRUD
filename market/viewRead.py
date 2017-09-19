from flask import jsonify
from flask.views import MethodView
from .sqlite import MarketModel


class MarketRead(MethodView):

    def get(self, id):
       m = MarketModel()
       data = m.getMarket(id)
       return jsonify({"market" : data})