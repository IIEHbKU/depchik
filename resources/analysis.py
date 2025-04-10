from flask import request
from flask_restful import Resource, abort

from misc import generate_analysis


class AnalysisResource(Resource):
    @staticmethod
    def get():
        data = request.args.get("data")
        if data is None:
            abort(404, message="Данные являются объектом None")
        try:
            return generate_analysis(data)
        except Exception as e:
            abort(404, message=f"Ошибка при генерации: {e}")
            raise
