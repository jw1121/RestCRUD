from flask.views import MethodView
from .sqlite import MarketModel


class MarketRead(MethodView):

    def get(self):
       pass