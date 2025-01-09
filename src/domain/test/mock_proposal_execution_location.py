from uuid import uuid4
from faker import Faker
from src.domain.models import ProposalExecutionLocation

faker = Faker()


def mock_proposal_execution_location() -> ProposalExecutionLocation:
    """Mocking ProposalExecutionLocation"""

    return ProposalExecutionLocation(
        id=uuid4(), municipio_id=faker.random_int(min=1), proposta_id=uuid4()
    )
