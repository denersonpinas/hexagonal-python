from faker import Faker
from src.domain.models import Proponent

faker = Faker()


def mock_proponent() -> Proponent:
    """Mocking Proponent"""

    return Proponent(
        cnpj=faker.numerify(text="#" * 14),
        proposta_id=faker.uuid4(),
        razao_social=faker.company()[:200],
        nome_fantasia=faker.company()[:200],
        endereco_cep=faker.numerify(text="#" * 8),
        endereco_uf=faker.city_suffix()[:100],
        endereco_municipio=faker.city()[:100],
        endereco_bairro=faker.street_name()[:100],
        endereco_logradouro=faker.street_name()[:100],
        endereco_numero=faker.random_int(min=1),
        endereco_complemento=faker.text(max_nb_chars=100),
        site=faker.url()[:100],
        rede_social=faker.url()[:100],
        resumo_curriculo=faker.text(max_nb_chars=500),
    )
