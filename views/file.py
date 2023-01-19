from flask_restful import Resource
from flask_uploads import UploadNotAllowed
from flask import send_file, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import traceback
import os

from libs import file_helper
from libs.strings import gettext
from schemas.file import FileSchema

file_schema = FileSchema()


class FileUpload(Resource):
    @jwt_required()
    def put(self):
        filename = f"user_{get_jwt_identity()}"
        data = file_schema.load(request.files)
        folder = "files"
        file_path = file_helper.find_file_any_format(filename, folder)

        if file_path:
            try:
                os.remove(file_path)
            except:
                return {"message": gettext("file_delete_failed")}, 500
        try:
            ext = file_helper.get_extension(data["file"].filename)
            file = filename + ext  # use our naming format + true extension
            file_path = file_helper.save_file(
                data["file"], folder=folder, name=file
            )
            basename = file_helper.get_basename(file_path)
            return {"message": gettext("file_uploaded").format(basename)}, 200
        except UploadNotAllowed:  # forbidden file type
            extension = file_helper.get_extension(data["file"])
            return {"message": gettext("file_illegal_extension").format(extension)}, 400


class File(Resource):
    @classmethod
    def get(cls, user_id: int):
        folder = "files"
        filename = f"user_{user_id}"
        file = file_helper.find_file_any_format(filename, folder)
        if file:
            return send_file(file)
        return {"message": gettext("files_not_found")}, 404
