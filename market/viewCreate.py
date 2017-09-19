from flask.views import MethodView
from flask import request
from .sqlite import MarketModel


class MarketCreate(MethodView):

    def post(self):
        jsony = request.get_json()
        
        model = MarketModel()
        data = model.insertMarket(self.parse(jsony))
        return ""

    def parse(self, jsony):

        columns = ', '.join([key for key, value in jsony.items()])
        values = "', '".join([value for key, value in jsony.items()])

        return columns, values

        '''
        return (jsony['FMID'],
        jsony['MarketName'],
        jsony['Website'],
        jsony['Facebook'],
        jsony['Twitter'],
        jsony['Youtube'],
        jsony['OtherMedia'],
        jsony['street'],
        jsony['city'],
        jsony['County'],
        jsony['State'],
        jsony['zip'],
        jsony['Season1Date'],
        jsony['Season1Time'],
        jsony['Season2Date'],
        jsony['Season2Time'],
        jsony['Season3Date'],
        jsony['Season3Time'],
        jsony['Season4Date'],
        jsony['Season4Time'],
        jsony['x'],
        jsony['y'],
        jsony['Location'],
        jsony['Credit'],
        jsony['WIC'],
        jsony['WICcash'],
        jsony['SFMNP'],
        jsony['SNAP'],
        jsony['Organic'],
        jsony['Bakedgoods'],
        jsony['Cheese'],
        jsony['Crafts'],
        jsony['Flowers'],
        jsony['Eggs'],
        jsony['Seafood'],
        jsony['Herbs'],
        jsony['Vegetables'],
        jsony['Honey'],
        jsony['Jams'],
        jsony['Maple'],
        jsony['Meat'],
        jsony['Nursery'],
        jsony['Nuts'],
        jsony['Plants'],
        jsony['Poultry'],
        jsony['Prepared'],
        jsony['Soap'],
        jsony['Trees'],
        jsony['Wine'],
        jsony['Coffee'],
        jsony['Beans'],
        jsony['Fruits'],
        jsony['Grains'],
        jsony['Juices'],
        jsony['Mushrooms'],
        jsony['PetFood'],
        jsony['Tofu'],
        jsony['WildHarvested'],
        jsony['updateTime'])
        '''

