from uuid import uuid4
from faker import Faker
from src.domain.models import Proposal

faker = Faker()


def mock_proposal() -> Proposal:
    """Mocking Proposal"""

    return Proposal(
        id=uuid4(),
        titulo_projeto=faker.text(max_nb_chars=100),
        resumo_projeto=faker.text(max_nb_chars=500),
        descricao_projeto=faker.text(max_nb_chars=1000),
        dados_bancario_instituicao=faker.company(),
        dados_bancario_agencia_conta_bancaria=faker.numerify(text="####-#"),
        dados_bancario_conta_corrente=faker.numerify(text="######-#"),
        dados_bancario_cnpj_fundo=faker.numerify(text="##.###.###/####-##"),
        dados_bancario_razao_social_fundo=faker.company(),
        dados_bancario_contato_fundo_nome=faker.name(),
        dados_bancario_contato_fundo_email=faker.email(),
        valor_total_projeto=faker.pyfloat(positive=True),
        valor_total_lei_incentivo=faker.pyfloat(positive=True),
        valor_total_captado=faker.pyfloat(positive=True),
        valor_total_captado_lei_incentivo=faker.pyfloat(positive=True),
        valor_total_incentivado_nubank=faker.pyfloat(positive=True),
        observacoes=faker.text(),
        data_inicio_projeto=faker.date(),
        data_fim_projeto=faker.date(),
    )
