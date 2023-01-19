import traceback
from flask_jwt_extended import create_access_token, create_refresh_token
from libs.strings import gettext

from flask import request, session
from flask_restful import Resource
from flask_bcrypt import Bcrypt

from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()
bcrypt = Bcrypt()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_json['password'] = bcrypt.generate_password_hash(user_json.get('password'))
        user = user_schema.load(user_json)

        if UserModel.find_by_username(user.username):
            return {"message": gettext("user_username_exists")}, 400

        try:
            user.save_to_db()
            return {"message": gettext("user_registered")}, 201
        except:  # failed to save user to db
            traceback.print_exc()
            user.delete_from_db()  # rollback
            return {"message": gettext("user_error_creating")}, 500


class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": gettext("user_not_found")}, 404

        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": gettext("user_not_found")}, 404

        user.delete_from_db()
        return {"message": gettext("user_deleted")}, 200


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = user_schema.load(user_json)
        session['username'] = user_data.username
        user = UserModel.find_by_username(user_data.username)

        if user and bcrypt.check_password_hash(user.password, user_data.password):
            access_token = create_access_token(user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            session['access_token'] = access_token

            return (
                {"access_token": access_token, "refresh_token": refresh_token},
                200,
            )

        return {"message": gettext("user_invalid_credentials")}, 401