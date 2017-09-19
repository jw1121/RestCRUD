from flask import Flask
from .viewRead import MarketRead
from .viewCreate import MarketCreate
from .viewUpdate import MarketUpdate
from .viewDelete import MarketDelete


app = Flask(__name__)

read = MarketRead.as_view('read')
create = MarketCreate.as_view('create')
update = MarketUpdate.as_view('update')
delete = MarketDelete.as_view('delete')

app.add_url_rule('/markets/',
                 view_func=read, methods=['GET', ])