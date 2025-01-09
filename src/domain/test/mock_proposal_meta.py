from uuid import uuid4
from faker import Faker
from src.domain.models import ProposalMeta

faker = Faker()


def mock_proposal_meta() -> ProposalMeta:
    """Mocking ProposalMeta"""

    return ProposalMeta(
        id=uuid4(),
        ordem=faker.random_int(min=1),
        meta=faker.text(max_nb_chars=500),
        quantitativo=faker.random_int(min=1),
        proposta_id=uuid4(),
    )
