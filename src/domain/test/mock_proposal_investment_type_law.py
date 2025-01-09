from uuid import uuid4
from faker import Faker
from src.domain.models import ProposalInvestmentTypeLaw

faker = Faker()


def mock_proposal_investment_type_law() -> ProposalInvestmentTypeLaw:
    """Mocking ProposalInvestmentTypeLaw"""

    return ProposalInvestmentTypeLaw(
        id=uuid4(), abginvest_tpproj_lei_id=faker.random_int(min=1), proposta_id=uuid4()
    )
