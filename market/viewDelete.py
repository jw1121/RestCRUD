from flask.views import MethodView
from flask import request
from .sqlite import MarketModel

class MarketDelete(MethodView):

    def delete(self, id):
        model = MarketModel()
        data = 'FMID', id
        rdata = model.deleteMarket(data)
        return ""

