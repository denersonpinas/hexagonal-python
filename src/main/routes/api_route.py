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
    find_abginvest_tpproj_lei_contrpart_composer,
    register_investmento_approacht_composer,
    register_law_composer,
    register_type_project_composer,
    register_category_counterpart_composer,
    register_relationship_category_counterpart_composer,
    register_abginvest_tpproj_lei_composer,
    register_type_file_composer,
    register_thematic_composer,
    register_caracterization_type_composer,
    register_caracterization_composer,
    register_abginvest_tpproj_lei_contrpart_composer,
)
from src.main.composer.find_law_composite import find_law_composer
from src.main.functions import (
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


@api_routes_bp.route("/api/abginvest-tpproj-lei-contrpart/", methods=["Post"])
def register_abginvest_tpproj_lei_contrpart():
    """Register AbginvestTpprojLeiContrpart route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_abginvest_tpproj_lei_contrpart_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "AbginvestTpprojLeiContrpart",
            "id": response.body.id,
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/caracterization/", methods=["Post"])
def register_caracterization():
    """Register Caracterization route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_caracterization_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "Caracterization",
            "id": response.body.id,
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/caracterization-type/", methods=["Post"])
def register_caracterization_type():
    """Register CaracterizationType route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_caracterization_type_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "CaracterizationType",
            "id": response.body.id,
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/thematic/", methods=["Post"])
def register_thematic():
    """Register Thematic route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_thematic_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "Thematic",
            "id": response.body.id,
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/type-file/", methods=["Post"])
def register_type_file():
    """Register TypeFile route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_type_file_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "TypeFile",
            "id": response.body.id,
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/abginvest-tpproj-lei/", methods=["Post"])
def register_abginvest_tpproj_lei():
    """Register AbginvestTpprojLei route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_abginvest_tpproj_lei_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "AbginvestTpprojLei",
            "id": response.body.id,
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/relationship-category-counterpart/", methods=["Post"])
def register_relationship_category_counterpart():
    """Register RelationshipCategoryCounterpart route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_relationship_category_counterpart_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "RelationshipCategoryCounterpart",
            "id": response.body.id,
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/category-counterpart/", methods=["Post"])
def register_category_counterpart():
    """Register CategoryCounterpart route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_category_counterpart_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "CategoryCounterpart",
            "id": response.body.id,
            "attibutes": {"description": response.body.descricao},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/type-project/", methods=["Post"])
def register_type_project():
    """Register TypeProject route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_type_project_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "TypeProject",
            "id": response.body.id,
            "attibutes": {"description": response.body.descricao},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/law/", methods=["Post"])
def register_law():
    """Register Law route"""

    message = {}
    response = flask_adapter_post(request=request, api_route=register_law_composer())

    if response.status_code < 300:
        message = {
            "Type": "Law",
            "id": response.body.id,
            "attibutes": {"description": response.body.descricao},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/investment-approach/", methods=["Post"])
def register_investment_approach():
    """Register investment approach route"""

    message = {}
    response = flask_adapter_post(
        request=request, api_route=register_investmento_approacht_composer()
    )

    if response.status_code < 300:
        message = {
            "Type": "Investment Approach",
            "id": response.body.id,
            "attibutes": {"description": response.body.descricao},
        }

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_bp.route("/api/counterpart/", methods=["Post"])
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


@api_routes_bp.route("/api/counterpart/", methods=["GET"])
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


@api_routes_bp.route("/bff/cadastro_projeto/", methods=["GET"])
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
    data_abginvest_tpproj_lei_contrpart = []

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

    for abginvest_lei in response_abginvest_tpproj_lei.body:
        http_request = HttpRequest(
            query={
                "abginvest_tpproj_lei_id": abginvest_lei.id,
            }
        )
        find_abginvest_lei_contrpart = find_abginvest_tpproj_lei_contrpart_composer()
        response_abginvest_lei_contrpart = find_abginvest_lei_contrpart.route(
            http_request
        )

        if response_abginvest_lei_contrpart.status_code > 300:
            # Handling Errors
            return (
                jsonify(
                    {
                        "error": {
                            "status": response_abginvest_lei_contrpart.status_code,
                            "title": response_abginvest_lei_contrpart.body["error"],
                        }
                    }
                ),
                response_abginvest_lei_contrpart.status_code,
            )

        abginvest_counterpart = []
        for abginvest_contrpart in response_abginvest_lei_contrpart.body:
            http_request = HttpRequest(
                query={
                    "id": abginvest_contrpart.relacao_contrapartida_categoria_id,
                }
            )
            find_relation_catg_contrpart = (
                find_relationship_category_counterparts_composer()
            )
            response_relation_catg_contrpart = find_relation_catg_contrpart.route(
                http_request
            )

            if response_relation_catg_contrpart.status_code > 300:
                # Handling Errors
                return (
                    jsonify(
                        {
                            "error": {
                                "status": response_relation_catg_contrpart.status_code,
                                "title": response_relation_catg_contrpart.body["error"],
                            }
                        }
                    ),
                    response_relation_catg_contrpart.status_code,
                )

            data_abginvest_contrpart = []
            for relations_categ_contrpart in response_relation_catg_contrpart.body:
                res_counterpart = []
                if relations_categ_contrpart.contrapartida_id:
                    http_request = HttpRequest(
                        query={
                            "counterpart_id": relations_categ_contrpart.contrapartida_id,
                        }
                    )
                    find_counterpart_composite = find_counterpart_composer()
                    response_relationship_counterpart = (
                        find_counterpart_composite.route(http_request)
                    )

                    if response_relationship_counterpart.status_code > 300:
                        # Handling Errors
                        return (
                            jsonify(
                                {
                                    "error": {
                                        "status": response_relationship_counterpart.status_code,
                                        "title": response_relationship_counterpart.body[
                                            "error"
                                        ],
                                    }
                                }
                            ),
                            response_relationship_counterpart.status_code,
                        )
                    res_counterpart = response_relationship_counterpart.body

                res_relations = []
                if relations_categ_contrpart.categoria_id:
                    http_request = HttpRequest(
                        query={
                            "category_counterpart_id": relations_categ_contrpart.categoria_id,
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
                                        "title": response_relationship_category.body[
                                            "error"
                                        ],
                                    }
                                }
                            ),
                            response_relationship_category.status_code,
                        )
                    res_relations = response_relationship_category.body

                data_abginvest_contrpart.append(
                    {
                        "id": relations_categ_contrpart.id,
                        "countrapartida": formatted_counterpart(res_counterpart),
                        "categoria": formatted_category_counterpart(res_relations),
                    }
                )

                abginvest_counterpart.append(
                    {
                        "id": abginvest_contrpart.ordem,
                        "abginvest_tpproj_lei": abginvest_lei.id,
                        "ordem": abginvest_contrpart.ordem,
                        "relacao_contrapartida_categoria": data_abginvest_contrpart,
                    }
                )
        data_abginvest_tpproj_lei_contrpart.append(
            {
                "id": abginvest_lei.id,
                "contrapartidas": abginvest_counterpart,
                "abordagem_investimento": abginvest_lei.abordagem_investimento_id,
                "tipo_pojeto": abginvest_lei.tipo_pojeto_id,
                "lei": abginvest_lei.lei_id,
            }
        )

    data["abginvest_tpproj_lei"] = data_abginvest_tpproj_lei_contrpart

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
