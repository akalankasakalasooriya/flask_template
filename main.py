import os
import uuid
import logging
from config import config_app
from flask import Flask, session
from werkzeug.middleware.proxy_fix import ProxyFix
logging.basicConfig(filename='logs/server.log', level=logging.DEBUG)

app = Flask("Flask template")
app.wsgi_app = ProxyFix(app.wsgi_app)
app.secret_key = 'IGzUojlAX5FeY8bEcQeM'
app.config['SESSION_TYPE'] = 'filesystem'
app.config.from_object("config.Config")
config_app(app)


@app.before_request
def before_request():
    session["request_id"] = str(uuid.uuid4())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

else:
    logging.info("Starting flask server")
