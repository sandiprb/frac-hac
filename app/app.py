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
#
# if __name__ == '__main__':
#     import argparse
#
#     parser = argparse.ArgumentParser(description='Development Server Help')
#     parser.add_argument("-d", "--debug", action="store_true", dest="debug_mode",
#                         help="run in debug mode (for use with PyCharm)", default=True)
#     parser.add_argument("-p", "--port", dest="port",
#                         help="port of server (default:%(default)s)", type=int, default=5000)
#
#     cmd_args = parser.parse_args()
#     app_options = {"port": cmd_args.port}
#
#     if cmd_args.debug_mode:
#         app_options["debug"] = True
#         app_options["use_debugger"] = False
#         app_options["use_reloader"] = False
#
#     app.run(**app_options)
