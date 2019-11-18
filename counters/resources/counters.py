from flask import current_app
from flask_restful import Resource


class Counter(Resource):
    def get(self):
        return {"message": "test"}
