from uuid import uuid4
from faker import Faker
from src.domain.models import ProposalBeneficiary

faker = Faker()


def mock_proposal_beneficiary() -> ProposalBeneficiary:
    """Mocking ProposalBeneficiary"""

    return ProposalBeneficiary(
        id=uuid4(), quantidade=faker.random_int(min=1), proposta_id=uuid4()
    )
