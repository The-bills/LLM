from flask import Flask
from router import cv_router, position_router

app = Flask("app")
app.config['UPLOAD_FOLDER'] = 'uploads'

app.register_blueprint(position_router.api, url_prefix='/positions')
app.register_blueprint(cv_router.api, url_prefix='/cv')