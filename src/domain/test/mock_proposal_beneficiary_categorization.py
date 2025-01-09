from uuid import uuid4
from faker import Faker
from src.domain.models import ProposalBeneficiaryCategorization

faker = Faker()


def mock_proposal_beneficiary_categorization() -> ProposalBeneficiaryCategorization:
    """Mocking ProposalBeneficiaryCategorization"""

    return ProposalBeneficiaryCategorization(
        id=uuid4(),
        categorizacao_id=faker.random_int(min=1),
        proposta_beneficiario_id=uuid4(),
    )
