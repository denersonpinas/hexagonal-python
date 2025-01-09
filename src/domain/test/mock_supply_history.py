from faker import Faker
from src.domain.models import SupplyHistory

faker = Faker()


def mock_supply_history() -> SupplyHistory:
    """Mocking SupplyHistory"""

    return SupplyHistory(
        id=faker.uuid4(),
        servico_prestado=faker.text(max_nb_chars=500),
        responsavel_contratacao=faker.name()[:100],
        proposta_id=faker.uuid4(),
    )
