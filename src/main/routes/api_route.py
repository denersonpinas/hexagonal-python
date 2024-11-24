from flask import Blueprint, jsonify, request

from src.main.adapter.api_adapter import flask_adapter
from src.main.composer import register_counterpart_composer

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api", methods=["Get"])
def something():
    """Welcome"""

    return jsonify({"message": "Hello World"})


@api_routes_bp.route("/api/counterpart", methods=["Post"])
def register_counterpart():
    """Register counterpart route"""

    message = {}
    response = flask_adapter(request=request, api_route=register_counterpart_composer())

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
