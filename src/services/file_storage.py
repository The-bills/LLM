from werkzeug.datastructures import FileStorage as FileStorageStruct
from uuid import uuid4
from flask import current_app as app
from os import path

class FileStorage:
    @staticmethod
    def save(file: FileStorageStruct):
        name = uuid4().hex
        filepath = path.join(app.config['UPLOAD_FOLDER'], name + '.pdf')
        file.save(filepath)
        return filepath
        