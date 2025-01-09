from faker import Faker
from src.infra.test import ProposalRepositorySpy
from .register import RegisterProposal

faker = Faker()


def test_register():
    """Testing register method"""

    proposal_repository = ProposalRepositorySpy()
    register_proposal = RegisterProposal(proposal_repository)

    attributes = {
        "titulo_projeto": faker.text(max_nb_chars=100),
        "resumo_projeto": faker.text(max_nb_chars=500),
        "descricao_projeto": faker.text(max_nb_chars=1000),
        "dados_bancario_instituicao": faker.company(),
        "dados_bancario_agencia_conta_bancaria": faker.numerify(text="####-#"),
        "dados_bancario_conta_corrente": faker.numerify(text="######-#"),
        "dados_bancario_cnpj_fundo": faker.numerify(text="##.###.###/####-##"),
        "dados_bancario_razao_social_fundo": faker.company(),
        "dados_bancario_contato_fundo_nome": faker.name(),
        "dados_bancario_contato_fundo_email": faker.email(),
        "valor_total_projeto": faker.pyfloat(positive=True),
        "valor_total_lei_incentivo": faker.pyfloat(positive=True),
        "valor_total_captado": faker.pyfloat(positive=True),
        "valor_total_captado_lei_incentivo": faker.pyfloat(positive=True),
        "valor_total_incentivado_nubank": faker.pyfloat(positive=True),
        "observacoes": faker.text(),
        "data_inicio_projeto": faker.date(),
        "data_fim_projeto": faker.date(),
    }

    response = register_proposal.register(**attributes)

    # Testing inputs
    assert proposal_repository.insert_proposal_params == attributes

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_max_len():
    """Testing register with long texts method"""

    proposal_repository = ProposalRepositorySpy()
    register_proposal = RegisterProposal(proposal_repository)

    attributes = {
        "titulo_projeto": faker.text(max_nb_chars=1000),
        "resumo_projeto": faker.text(max_nb_chars=1000),
        "descricao_projeto": faker.text(max_nb_chars=2000),
        "dados_bancario_instituicao": faker.company(),
        "dados_bancario_agencia_conta_bancaria": faker.numerify(text="####-#"),
        "dados_bancario_conta_corrente": faker.numerify(text="######-#"),
        "valor_total_projeto": faker.pyfloat(positive=True),
        "valor_total_lei_incentivo": faker.pyfloat(positive=True),
        "valor_total_captado": faker.pyfloat(positive=True),
        "valor_total_captado_lei_incentivo": faker.pyfloat(positive=True),
        "valor_total_incentivado_nubank": faker.pyfloat(positive=True),
    }

    response = register_proposal.register(**attributes)

    # Testing inputs
    assert proposal_repository.insert_proposal_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_register_fail():
    """Testing register method fail"""

    proposal_repository = ProposalRepositorySpy()
    register_proposal = RegisterProposal(proposal_repository)

    attributes = {
        "titulo_projeto": faker.random_number(),
        "resumo_projeto": faker.random_number(),
        "descricao_projeto": faker.random_number(),
        "dados_bancario_instituicao": faker.random_number(),
        "dados_bancario_agencia_conta_bancaria": faker.random_number(),
        "dados_bancario_conta_corrente": faker.random_number(),
        "dados_bancario_cnpj_fundo": faker.random_number(),
        "dados_bancario_razao_social_fundo": faker.random_number(),
        "dados_bancario_contato_fundo_nome": faker.random_number(),
        "dados_bancario_contato_fundo_email": faker.random_number(),
        "valor_total_projeto": faker.name(),
        "valor_total_lei_incentivo": faker.name(),
        "valor_total_captado": faker.name(),
        "valor_total_captado_lei_incentivo": faker.name(),
        "valor_total_incentivado_nubank": faker.name(),
        "observacoes": faker.random_number(),
        "data_inicio_projeto": faker.random_number(),
        "data_fim_projeto": faker.random_number(),
    }

    response = register_proposal.register(**attributes)

    # Testing inputs
    assert proposal_repository.insert_proposal_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
