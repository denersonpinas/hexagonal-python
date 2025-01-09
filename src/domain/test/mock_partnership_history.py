from faker import Faker
from src.domain.models import PartnershipHistory

faker = Faker()


def mock_partnership_history() -> PartnershipHistory:
    """Mocking PartnershipHistory"""

    return PartnershipHistory(
        id=faker.uuid4(),
        numero_de_patrocinadores=faker.random_int(min=0),
        numero_de_renovacao=faker.random_int(min=0),
        proposta_id=faker.uuid4(),
        informacoes_adicionais=faker.text(max_nb_chars=500),
    )
