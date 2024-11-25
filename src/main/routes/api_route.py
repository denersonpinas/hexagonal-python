from flask import Blueprint, jsonify, request

from src.main.adapter.api_adapter import flask_adapter_get, flask_adapter_post
from src.main.composer import register_counterpart_composer, find_counterpart_composer

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api", methods=["Get"])
def something():
    """Welcome"""

    return jsonify({"message": "Hello World"})


@api_routes_bp.route("/api/counterpart", methods=["Post"])
def register_counterpart():
    """Register counterpart route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_counterpart_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "Counterpart",
            "id": response.body.id,
            "attibutes": {"description": response.body.descricao},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/counterpart", methods=["GET"])
def finder_counterpart():
    """Find counterpart route"""

    message = []
    response = flask_adapter_get(request=request, api_route=find_counterpart_composer())

    if response.status_code < 300:
        for counterpart in response.body:
            message.append(
                {
                    "Type": "Counterpart",
                    "id": counterpart.id,
                    "attibutes": {
                        "description": counterpart.descricao,
                        "example_aplicability": counterpart.exemplo_aplicabilidade,
                        "required": counterpart.obrigatoria,
                        "default": counterpart.padrao,
                    },
                }
            )

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )
