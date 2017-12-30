from flask import Flask, render_template

import settings
from api.controllers import api
from services.mongo import mongo

app = Flask(
    __name__,
    template_folder=settings.TEMPLATES_DIR,
    static_folder='static')

app.config['MONGO_DBNAME'] = settings.DB_NAME
app.config['MONGO_URI'] = settings.DB_URI

mongo.init_app(app)


@app.route('/')
def index():
    context = {}
    context['message'] = 'Hello!'
    return render_template('index.html', data=context)


app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=settings.DEBUG)
