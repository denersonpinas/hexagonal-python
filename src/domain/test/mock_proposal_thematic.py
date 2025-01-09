from faker import Faker
from src.domain.models import ProposalThematic

faker = Faker()


def mock_proposal_thematic() -> ProposalThematic:
    """Mocking ProposalThematic"""

    return ProposalThematic(
        id=faker.uuid4(), proposta_id=faker.uuid4(), tematica_id=faker.random_int(min=1)
    )
