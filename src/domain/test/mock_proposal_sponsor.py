from uuid import uuid4
from faker import Faker
from src.domain.models import ProposalSponsor

faker = Faker()


def mock_proposal_sponsor() -> ProposalSponsor:
    """Mocking ProposalSponsor"""

    return ProposalSponsor(
        id=uuid4(),
        nome=faker.name()[:100],
        formato=faker.word()[:50],
        valor=faker.pyfloat(positive=True),
        proposta_id=uuid4(),
    )
