from faker import Faker
from src.data.test import RegisterProposalSpy
from src.infra.test import ProposalRepositorySpy
from src.presenters.controllers import RegisterProposalController
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_route():
    """Testing route method in RegisterProposal"""

    register_proposal_use_case = RegisterProposalSpy(ProposalRepositorySpy())
    register_proposal_route = RegisterProposalController(
        register_proposal_use_case=register_proposal_use_case
    )

    attributes = {
        "titulo_projeto": faker.text(max_nb_chars=100),
        "resumo_projeto": faker.text(max_nb_chars=250),
        "descricao_projeto": faker.text(max_nb_chars=500),
        "dados_bancario_instituicao": faker.company(),
        "dados_bancario_agencia_conta_bancaria": faker.bothify(text="####-#"),
        "dados_bancario_conta_corrente": faker.bothify(text="######-#"),
        "dados_bancario_cnpj_fundo": faker.bothify(text="##.###.###/####-##"),
        "dados_bancario_razao_social_fundo": faker.company(),
        "dados_bancario_contato_fundo_nome": faker.name(),
        "dados_bancario_contato_fundo_email": faker.email(),
        "valor_total_projeto": faker.pyfloat(positive=True, max_value=1000000),
        "valor_total_lei_incentivo": faker.pyfloat(positive=True, max_value=1000000),
        "valor_total_captado": faker.pyfloat(positive=True, max_value=1000000),
        "valor_total_captado_lei_incentivo": faker.pyfloat(
            positive=True, max_value=1000000
        ),
        "valor_total_incentivado_nubank": faker.pyfloat(
            positive=True, max_value=1000000
        ),
        "observacoes": faker.text(),
        "data_inicio_projeto": faker.date(),
        "data_fim_projeto": faker.date(),
    }

    response = register_proposal_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_use_case.register_param["titulo_projeto"]
        == attributes["titulo_projeto"]
    )
    assert (
        register_proposal_use_case.register_param["resumo_projeto"]
        == attributes["resumo_projeto"]
    )
    assert (
        register_proposal_use_case.register_param["descricao_projeto"]
        == attributes["descricao_projeto"]
    )
    assert (
        register_proposal_use_case.register_param["dados_bancario_instituicao"]
        == attributes["dados_bancario_instituicao"]
    )
    assert (
        register_proposal_use_case.register_param[
            "dados_bancario_agencia_conta_bancaria"
        ]
        == attributes["dados_bancario_agencia_conta_bancaria"]
    )
    assert (
        register_proposal_use_case.register_param["dados_bancario_conta_corrente"]
        == attributes["dados_bancario_conta_corrente"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing route method fail"""

    register_proposal_use_case = RegisterProposalSpy(ProposalRepositorySpy())
    register_proposal_route = RegisterProposalController(
        register_proposal_use_case=register_proposal_use_case
    )

    attributes = {"titulo_projeto": faker.boolean(), "resumo_projeto": faker.boolean()}

    response = register_proposal_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_no_body_params():
    """Testing route no body param method"""

    register_proposal_use_case = RegisterProposalSpy(ProposalRepositorySpy())
    register_proposal_route = RegisterProposalController(
        register_proposal_use_case=register_proposal_use_case
    )

    response = register_proposal_route.route(HttpRequest())

    # Testing input
    assert register_proposal_use_case.register_param == {}

    # Testing output
    assert response.status_code == 400
    assert response.body


def test_route_missing_required_params():
    """Testing route with missing required parameters"""

    register_proposal_use_case = RegisterProposalSpy(ProposalRepositorySpy())
    register_proposal_route = RegisterProposalController(
        register_proposal_use_case=register_proposal_use_case
    )

    attributes = {
        "titulo_projeto": faker.text(max_nb_chars=100),
        # Missing other required params
    }

    response = register_proposal_route.route(HttpRequest(body=attributes))

    # Testing input
    assert register_proposal_use_case.register_param == {}

    # Testing output
    assert response.status_code == 422
    assert response.body


def test_route_with_optional_params():
    """Testing route with optional parameters"""

    register_proposal_use_case = RegisterProposalSpy(ProposalRepositorySpy())
    register_proposal_route = RegisterProposalController(
        register_proposal_use_case=register_proposal_use_case
    )

    attributes = {
        "titulo_projeto": faker.text(max_nb_chars=100),
        "resumo_projeto": faker.text(max_nb_chars=250),
        "descricao_projeto": faker.text(max_nb_chars=500),
        "dados_bancario_instituicao": faker.company(),
        "dados_bancario_agencia_conta_bancaria": faker.bothify(text="####-#"),
        "dados_bancario_conta_corrente": faker.bothify(text="######-#"),
        # Optional params
        "observacoes": faker.text(),
        "valor_total_projeto": faker.pyfloat(positive=True, max_value=1000000),
    }

    response = register_proposal_route.route(HttpRequest(body=attributes))

    # Testing input
    assert (
        register_proposal_use_case.register_param["titulo_projeto"]
        == attributes["titulo_projeto"]
    )
    assert (
        register_proposal_use_case.register_param["observacoes"]
        == attributes["observacoes"]
    )
    assert (
        register_proposal_use_case.register_param["valor_total_projeto"]
        == attributes["valor_total_projeto"]
    )

    # Testing output
    assert response.status_code == 200
    assert response.body
