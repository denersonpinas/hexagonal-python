import json
import os
import uuid
from flask import Blueprint, jsonify, request

# from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import secure_filename

from src.constants.reference import UPLOAD_FOLDER
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
    register_proposal_composer,
    register_proponent_composer,
    register_proposal_beneficiary_composer,
    register_proposal_beneficiary_categorization_composer,
    register_proposal_sponsor_composer,
    register_proposal_meta_composer,
    register_proposal_execution_location_composer,
    register_city_composer,
    register_supply_history_composer,
    register_project_history_composer,
    register_goal_history_composer,
    register_project_contact_point_composer,
    register_legal_representative_composer,
    register_partnership_history_composer,
    register_proposal_file_composer,
    register_proposal_milestone_composer,
    register_proposal_investment_type_law_composer,
    register_proposal_counterpart_composer,
    register_proposal_thematic_composer,
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

        data_cp = response_relationship_counterpart.body
        cata_categ = response_relationship_category.body
        data_relationship_ctg_ctpr.append(
            {
                "id": relationship.id,
                "contrapartida": {
                    "id": data_cp[0].id,
                    "descricao": data_cp[0].descricao,
                    "obrigatoria": data_cp[0].obrigatoria,
                    "exemplo_aplicabilidade": data_cp[0].exemplo_aplicabilidade,
                },
                "categoria": {
                    "id": cata_categ[0].id,
                    "subcategoria_de": cata_categ[0].subcategoria_de_id,
                    "nome": cata_categ[0].nome,
                    "descricao": cata_categ[0].descricao,
                },
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

            data_abginvest_contrpart = {}
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

                data_abginvest_contrpart = {
                    "id": relations_categ_contrpart.id,
                    "contrapartida": {
                        "id": res_counterpart[0].id,
                        "descricao": res_counterpart[0].descricao,
                        "obrigatoria": res_counterpart[0].obrigatoria,
                        "exemplo_aplicabilidade": res_counterpart[
                            0
                        ].exemplo_aplicabilidade,
                    },
                    "categoria": {
                        "id": res_relations[0].id,
                        "subcategoria_de": res_relations[0].subcategoria_de_id,
                        "nome": res_relations[0].nome,
                        "descricao": res_relations[0].descricao,
                    },
                }

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


@api_routes_bp.route("/bff/cadastro_projeto/", methods=["POST"])
def register_bff_project_create():
    """Register bff project create route"""
    data = {
        "id": "",
        "proponente": {},
        "locais_execucao": [],
        "tematicas": [],
        "metas": [],
        "marcos": [],
        "beneficiarios": [],
        "patrocinadores": [],
        "abginvests_tpprojs_leis": [],
        "arquivo_detalhes": [],
        "titulo_projeto": "",
        "resumo_projeto": "",
        "descricao_projeto": "",
        "dados_bancario_instituicao": "",
        "dados_bancario_agencia_conta_bancaria": "",
        "dados_bancario_conta_corrente": "",
        "dados_bancario_cnpj_fundo": None,
        "dados_bancario_razao_social_fundo": None,
        "dados_bancario_contato_fundo_nome": None,
        "dados_bancario_contato_fundo_email": None,
        "valor_total_projeto": "",
        "valor_total_lei_incentivo": "",
        "valor_total_captado": "",
        "valor_total_captado_lei_incentivo": "",
        "valor_total_incentivado_nubank": "",
        "observacoes": "",
        "data_inicio_projeto": "",
        "data_fim_projeto": "",
    }

    # Get Data Form =========================================================
    data = request.form.get("proposta_json")

    # Converte para JSON
    json_data = json.loads(data)

    # Saved Proposal
    http_request = HttpRequest(body=json_data)
    register_proposal_composite = register_proposal_composer()
    response_proposal = register_proposal_composite.route(http_request)

    # Saved Proponent
    proponent_data = json_data["proponente"]
    http_request = HttpRequest(
        body={
            "cnpj": proponent_data["cnpj"],
            "proposal_id": response_proposal.body.id,
            "company_name": proponent_data["razao_social"],
            "trade_name": proponent_data["nome_fantasia"],
            "zip_code": proponent_data["endereco_cep"],
            "state": proponent_data["endereco_uf"],
            "city": proponent_data["endereco_municipio"],
            "neighborhood": proponent_data["endereco_bairro"],
            "street": proponent_data["endereco_logradouro"],
            "number": proponent_data["endereco_numero"],
            "complement": proponent_data["endereco_complemento"],
            "website": proponent_data["site"],
            "social_media": proponent_data["rede_social"],
            "curriculum_summary": "",
        }
    )
    register_proponent_composite = register_proponent_composer()
    response_proponent = register_proponent_composite.route(http_request)

    # Saved Beneficiary
    beneficiary_data = json_data["beneficiarios"]
    for beneficiary in beneficiary_data:
        http_request_pb = HttpRequest(
            body={
                "quantidade": beneficiary["quantidade"],
                "proposta_id": response_proposal.body.id,
            }
        )
        register_beneficiary_composite = register_proposal_beneficiary_composer()
        response_beneficiary = register_beneficiary_composite.route(http_request_pb)
        http_request_pbc = HttpRequest(
            body={
                "categorizacao_id": int(beneficiary["categorizacoes_ids"][0]),
                "proposta_beneficiario_id": response_beneficiary.body.id,
            }
        )
        register_beneficiary_catg_composite = (
            register_proposal_beneficiary_categorization_composer()
        )
        register_beneficiary_catg_composite.route(http_request_pbc)

    # Saved Proposal Sponsor
    sponsor_data = json_data["patrocinadores"]
    for sponsor in sponsor_data:
        http_request = HttpRequest(
            body={
                "nome": sponsor["nome"],
                "formato": sponsor["formato"],
                "valor": sponsor["valor"],
                "proposta_id": response_proposal.body.id,
            }
        )
        register_proposal_sponsor_composite = register_proposal_sponsor_composer()
        register_proposal_sponsor_composite.route(http_request)

    # Saved Proposal Sponsor
    goals_data = json_data["metas"]
    for goal in goals_data:
        http_request = HttpRequest(
            body={
                "goal": goal["meta"],
                "quantity": goal["quantitativo"],
                "order": goal["ordem"],
                "proposal_id": response_proposal.body.id,
            }
        )
        register_proposal_meta_composite = register_proposal_meta_composer()
        register_proposal_meta_composite.route(http_request)

    # Saved Execution Location
    city_data = json_data["locais_execucao"]
    for city in city_data:
        http_request_city = HttpRequest(
            body={"name": city["nome"], "state": city["uf"]}
        )
        register_city_composite = register_city_composer()
        response_city = register_city_composite.route(http_request_city)

        http_request_exlo = HttpRequest(
            body={
                "city_id": response_city.body.id,
                "proposal_id": response_proposal.body.id,
            }
        )
        register_proposal_execution_location_composite = (
            register_proposal_execution_location_composer()
        )
        register_proposal_execution_location_composite.route(http_request_exlo)

    # Saved Supply History
    supply_history_data = proponent_data["historico_de_fornecimento"]
    for supply_history in supply_history_data:
        http_request = HttpRequest(
            body={
                "service_provided": supply_history["servico_prestado"],
                "hiring_manager": supply_history["responsavel_contratacao"],
                "proposal_id": response_proponent.body.proposta_id,
            }
        )
        register_supply_history_composite = register_supply_history_composer()
        register_supply_history_composite.route(http_request)

    # Saved Project History
    project_history_data = proponent_data["historico_projetos"]
    for project_history in project_history_data:
        goals_history_data = project_history["historico_de_metas"]
        http_request_ph = HttpRequest(
            body={
                "investment_year": project_history["ano_investimento"],
                "title": project_history["titulo"],
                "investment_type": project_history["tipo_investimento"],
                "proposal_id": response_proponent.body.proposta_id,
            }
        )
        register_project_history_composite = register_project_history_composer()
        response_project_history = register_project_history_composite.route(
            http_request_ph
        )

        for goals_history in goals_history_data:
            http_request_gh = HttpRequest(
                body={
                    "expected": goals_history["previsto"],
                    "achieved": goals_history["alcancado"],
                    "project_history_id": response_project_history.body.id,
                }
            )
            register_goals_history_composite = register_goal_history_composer()
            register_goals_history_composite.route(http_request_gh)

    # Saved Project Contact Point
    project_contact_point_data = proponent_data["ponto_de_contato"]
    for project_contact_point in project_contact_point_data:
        http_request = HttpRequest(
            body={
                "name": project_contact_point["nome"],
                "email": project_contact_point["email"],
                "position": project_contact_point["cargo"],
                "proposal_id": response_proponent.body.proposta_id,
            }
        )
        register_project_contact_point_composite = (
            register_project_contact_point_composer()
        )
        register_project_contact_point_composite.route(http_request)

    # Saved Legal Representative
    legal_representative_data = proponent_data["representante_legal"]
    for legal_representative in legal_representative_data:
        http_request = HttpRequest(
            body={
                "name": legal_representative["nome"],
                "cpf": legal_representative["cpf"],
                "email": legal_representative["email"],
                "position": legal_representative["cargo"],
                "proposal_id": response_proponent.body.proposta_id,
            }
        )
        register_legal_representative_composite = (
            register_legal_representative_composer()
        )
        register_legal_representative_composite.route(http_request)

    # Saved Partnership History
    partnership_history_data = proponent_data["historico_de_parcerias"]
    for partnership_history in partnership_history_data:
        http_request = HttpRequest(
            body={
                "sponsors_number": partnership_history["numero_de_patrocinadores"],
                "renewal_number": partnership_history["numero_de_renovacao"],
                "additional_info": partnership_history["informacoes_adicionais"],
                "proposal_id": response_proponent.body.proposta_id,
            }
        )
        register_partnership_history_composite = register_partnership_history_composer()
        register_partnership_history_composite.route(http_request)

    # Saved Proposal File
    proposal_file_data = json_data["arquivos_tipos_ids"]
    cont = 0
    for chave, file in dict(request.files).items():
        name = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
        extension = secure_filename(file.filename).split(".")[1]
        savePath = os.path.join(UPLOAD_FOLDER, name)
        file.save(savePath)
        size = os.path.getsize(savePath)

        http_request = HttpRequest(
            body={
                "name": name.split(".")[0],
                "extension": f".{extension}",
                "size": size,
                "uri": name,
                "type_id": proposal_file_data[cont],
                "proposal_id": response_proposal.body.id,
            }
        )
        register_proposal_file_composite = register_proposal_file_composer()
        register_proposal_file_composite.route(http_request)
        cont += 1

    # Saved Proposal Milestone
    proposal_milestone_data = json_data["marcos"]
    for proposal_milestone in proposal_milestone_data:
        http_request = HttpRequest(
            body={
                "description": proposal_milestone["descricao"],
                "execution_date": proposal_milestone["execucao"],
                "proposal_id": response_proposal.body.id,
            }
        )
        register_proposal_milestone_composite = register_proposal_milestone_composer()
        register_proposal_milestone_composite.route(http_request)

    # Saved Proposal Investment Type Law
    proposal_investment_type_law_data = json_data["abginvests_tpprojs_leis"]
    for proposal_investment_type_law in proposal_investment_type_law_data:
        http_request_pitl = HttpRequest(
            body={
                "investment_type_law_id": proposal_investment_type_law[
                    "abginvest_tpproj_lei"
                ],
                "proposal_id": response_proposal.body.id,
            }
        )
        register_proposal_investment_type_law_composite = (
            register_proposal_investment_type_law_composer()
        )
        response_proposal_investment_type_law = (
            register_proposal_investment_type_law_composite.route(http_request_pitl)
        )

        proposal_counterpart = proposal_investment_type_law["contrapartidas"]
        for counterpart in proposal_counterpart:
            http_request = HttpRequest(
                body={
                    "description": counterpart["descricao"],
                    "quantity": counterpart["quantitativo"],
                    "investment_type_law_counterpart_id": counterpart[
                        "abginvest_tpproj_lei_contrpart_id"
                    ],
                    "proposal_investment_type_law_id": response_proposal_investment_type_law.body.id,
                }
            )
            register_proposal_counterpart_composite = (
                register_proposal_counterpart_composer()
            )
            register_proposal_counterpart_composite.route(http_request)

    # Saved Proposal Thematic
    proposal_thematic_data = json_data["tematicas_ids"]
    for proposal_thematic in proposal_thematic_data:
        http_request = HttpRequest(
            body={
                "thematic_id": proposal_thematic,
                "proposal_id": response_proposal.body.id,
            }
        )
        register_proposal_thematic_composite = register_proposal_thematic_composer()
        response_proposal_thematic = register_proposal_thematic_composite.route(
            http_request
        )

    message = {
        "Type": "Form Data",
        "id": response_proposal.body.id,
        "attibutes": {},
    }

    return jsonify({"data": message}), response_proposal_thematic.status_code
