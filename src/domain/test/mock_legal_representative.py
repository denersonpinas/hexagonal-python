from faker import Faker
from src.domain.models import LegalRepresentative

faker = Faker()


def mock_legal_representative() -> LegalRepresentative:
    """Mocking LegalRepresentative"""

    return LegalRepresentative(
        id=faker.uuid4(),
        nome=faker.name()[:100],
        cpf=faker.numerify(text="#" * 11),
        email=faker.email()[:100],
        cargo=faker.job()[:100],
        proposta_id=faker.uuid4(),
        resumo=faker.text(max_nb_chars=500),
    )
