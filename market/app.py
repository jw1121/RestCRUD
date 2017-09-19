from flask import Flask
from .viewRead import MarketRead
from .viewCreate import MarketCreate
from .viewUpdate import MarketUpdate
from .viewDelete import MarketDelete

app = Flask(__name__)

app.debug = True

read = MarketRead.as_view('read')
create = MarketCreate.as_view('create')
update = MarketUpdate.as_view('update')
delete = MarketDelete.as_view('delete')

app.add_url_rule('/market/',
                 view_func=read, methods=['GET', ])
app.add_url_rule('/market/<int:id>',
                 view_func=read, methods=['GET', ])
app.add_url_rule('/market/create',
                 view_func=create, methods=['POST', ])
app.add_url_rule('/market/',
                 view_func=update, methods=['PUT', ])
app.add_url_rule('/market/<int:id>',
                 view_func=delete, methods=['DELETE', ])

