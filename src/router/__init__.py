from flask import Flask
from router import cv_router, position_router, tokens_router

app = Flask("app")
app.config['UPLOAD_FOLDER'] = 'uploads'

from flask_cors import CORS, cross_origin
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(position_router.api, url_prefix='/positions')
app.register_blueprint(cv_router.api, url_prefix='/cv')
app.register_blueprint(tokens_router.api, url_prefix='/tokens')

from flask import send_from_directory
from os import path

@app.route('/uploads/<fileName>')
def send_report(fileName):
    return send_from_directory(
            path.join('..', app.config['UPLOAD_FOLDER']), fileName, as_attachment=False
        )