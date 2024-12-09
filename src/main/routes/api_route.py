from flask import Blueprint, jsonify, request

from src.main.adapter.api_adapter import flask_adapter_get, flask_adapter_post
from src.main.composer import (
    find_relationship_category_counterparts_composer,
    register_counterpart_composer,
    find_counterpart_composer,
    find_investmento_approacht_composer,
    find_category_counterpart_composer,
    find_type_project_composer,
    find_abginvest_tpproj_lei_composer,
    find_type_file_composer,
    find_thematic_composer,
    find_categorization_type_composer,
    find_categorization_composer,
)
from src.main.composer.find_law_composite import find_law_composer
from src.main.functions import (
    formatted_abginvest_tpproj_lei,
    formatted_categorization,
    formatted_categorization_type,
    formatted_category_counterpart,
    formatted_counterpart,
    formatted_law,
    formatted_investment_approach,
    formatted_thematic,
    formatted_type_file,
    formatted_type_project,
)
from src.presenters.helpers.http_models import HttpRequest

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


@api_routes_bp.route("/bff/cadastro_projeto", methods=["GET"])
def finder_bff_project_create():
    """Find bff project create route"""

    data = {
        "abordagens_investimento": [],
        "leis": [],
        "tipos_projetos": [],
        "contrapartidas": [],
        "categoriasContrapartida": [],
        "relacao_contrapartidas_categoria": [],
        "abginvest_tpproj_lei": [],
        "tipos_arquivos": [],
        "tematicas": [],
        "tipos_categorizacoes_beneficiarios": [],
        "categorizacoes_beneficiarios": [],
    }

    # Get Investment Approach
    response_investment_appr = flask_adapter_get(
        request=request, api_route=find_investmento_approacht_composer()
    )

    if response_investment_appr.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_investment_appr.status_code,
                        "title": response_investment_appr.body["error"],
                    }
                }
            ),
            response_investment_appr.status_code,
        )

    data["abordagens_investimento"] = formatted_investment_approach(
        response_investment_appr.body
    )

    # Get Law
    response_law = flask_adapter_get(request=request, api_route=find_law_composer())

    if response_law.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_law.status_code,
                        "title": response_law.body["error"],
                    }
                }
            ),
            response_law.status_code,
        )

    data["leis"] = formatted_law(response_law.body)

    # Get Relationship Category Counterpart
    response_relationship_catg_ctrp = flask_adapter_get(
        request=request, api_route=find_relationship_category_counterparts_composer()
    )

    if response_relationship_catg_ctrp.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_relationship_catg_ctrp.status_code,
                        "title": response_relationship_catg_ctrp.body["error"],
                    }
                }
            ),
            response_relationship_catg_ctrp.status_code,
        )

    data_relationship_ctg_ctpr = []
    for relationship in response_relationship_catg_ctrp.body:
        http_request = HttpRequest(
            query={
                "counterpart_id": relationship.contrapartida_id,
            }
        )
        find_counterpart_composite = find_counterpart_composer()
        response_relationship_counterpart = find_counterpart_composite.route(
            http_request
        )

        if response_relationship_counterpart.status_code > 300:
            # Handling Errors
            return (
                jsonify(
                    {
                        "error": {
                            "status": response_relationship_counterpart.status_code,
                            "title": response_relationship_counterpart.body["error"],
                        }
                    }
                ),
                response_relationship_counterpart.status_code,
            )

        http_request = HttpRequest(
            query={
                "category_counterpart_id": relationship.categoria_id,
            }
        )

        find_category_ctpr_composite = find_category_counterpart_composer()
        response_relationship_category = find_category_ctpr_composite.route(
            http_request
        )

        if response_relationship_category.status_code > 300:
            # Handling Errors
            return (
                jsonify(
                    {
                        "error": {
                            "status": response_relationship_category.status_code,
                            "title": response_relationship_category.body["error"],
                        }
                    }
                ),
                response_relationship_category.status_code,
            )

        data_relationship_ctg_ctpr.append(
            {
                "id": relationship.id,
                "countrapartida": formatted_counterpart(
                    response_relationship_counterpart.body
                ),
                "categoria": formatted_category_counterpart(
                    response_relationship_category.body
                ),
            }
        )

    data["relacao_contrapartidas_categoria"] = data_relationship_ctg_ctpr

    # Get TypeProject
    response_type_project = flask_adapter_get(
        request=request, api_route=find_type_project_composer()
    )

    if response_type_project.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_type_project.status_code,
                        "title": response_type_project.body["error"],
                    }
                }
            ),
            response_type_project.status_code,
        )

    data["tipos_projetos"] = formatted_type_project(response_type_project.body)

    # Get Counterpart
    response_counterpart = flask_adapter_get(
        request=request, api_route=find_counterpart_composer()
    )

    if response_counterpart.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_counterpart.status_code,
                        "title": response_counterpart.body["error"],
                    }
                }
            ),
            response_counterpart.status_code,
        )

    data["contrapartidas"] = formatted_counterpart(response_counterpart.body)

    # Get Category Counterpart
    response_catg_cprt = flask_adapter_get(
        request=request, api_route=find_category_counterpart_composer()
    )

    if response_catg_cprt.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_catg_cprt.status_code,
                        "title": response_catg_cprt.body["error"],
                    }
                }
            ),
            response_catg_cprt.status_code,
        )

    data["categoriasContrapartida"] = formatted_category_counterpart(
        response_catg_cprt.body
    )

    # Get AbginvestTpprojLei
    response_abginvest_tpproj_lei = flask_adapter_get(
        request=request, api_route=find_abginvest_tpproj_lei_composer()
    )

    if response_abginvest_tpproj_lei.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_abginvest_tpproj_lei.status_code,
                        "title": response_abginvest_tpproj_lei.body["error"],
                    }
                }
            ),
            response_abginvest_tpproj_lei.status_code,
        )

    data["abginvest_tpproj_lei"] = formatted_abginvest_tpproj_lei(
        response_abginvest_tpproj_lei.body
    )

    # Get TypeFile
    response_type_file = flask_adapter_get(
        request=request, api_route=find_type_file_composer()
    )

    if response_type_file.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_type_file.status_code,
                        "title": response_type_file.body["error"],
                    }
                }
            ),
            response_type_file.status_code,
        )

    data["tipos_arquivos"] = formatted_type_file(response_type_file.body)

    # Get Thematic
    response_thematic = flask_adapter_get(
        request=request, api_route=find_thematic_composer()
    )

    if response_thematic.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_thematic.status_code,
                        "title": response_thematic.body["error"],
                    }
                }
            ),
            response_thematic.status_code,
        )

    data["tematicas"] = formatted_thematic(response_thematic.body)

    # Get BenefitCategorizationType
    response_categorization_type = flask_adapter_get(
        request=request, api_route=find_categorization_type_composer()
    )

    if response_categorization_type.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_categorization_type.status_code,
                        "title": response_categorization_type.body["error"],
                    }
                }
            ),
            response_categorization_type.status_code,
        )

    data["tipos_categorizacoes_beneficiarios"] = formatted_categorization_type(
        response_categorization_type.body
    )

    # Get BenefitCategorizationType
    response_categorization = flask_adapter_get(
        request=request, api_route=find_categorization_composer()
    )

    if response_categorization.status_code > 300:
        # Handling Errors
        return (
            jsonify(
                {
                    "error": {
                        "status": response_categorization.status_code,
                        "title": response_categorization.body["error"],
                    }
                }
            ),
            response_categorization.status_code,
        )

    data["categorizacoes_beneficiarios"] = formatted_categorization(
        response_categorization.body
    )

    return jsonify(data), response_investment_appr.status_code
