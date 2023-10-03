from werkzeug.datastructures import FileStorage as File
from uuid import uuid4
from flask import current_app as app
from os import path

class FileStorage:
    @staticmethod
    def save(file: File):
        name = uuid4().hex
        filepath = path.join(app.config['UPLOAD_FOLDER'], name + '.pdf')
        file.save(filepath)
        return filepath
        