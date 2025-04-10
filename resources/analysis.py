import asyncio

from flask import request
from flask_restful import Resource, abort

from misc import generate_analysis


class AnalysisResource(Resource):
    @staticmethod
    def post():
        if not request.is_json:
            abort(400, message="Request must be in JSON format.")
        try:
            data = request.get_json()
            required_fields = ["model", "prompt", "stream"]
            for field in required_fields:
                if field not in data:
                    abort(400, message=f"Missing required field: {field}")
            model = data["model"]
            prompt = data["prompt"]
            stream = data["stream"]
            analysis_result = asyncio.run(generate_analysis(model=model, prompt=prompt, stream=stream))
            return {
                "status": "success",
                "data": analysis_result
            }
        except Exception as e:
            abort(500, message=f"An error occurred: {str(e)}")
