from uuid import uuid4
from faker import Faker
from src.domain.models import ProposalCounterpart

faker = Faker()


def mock_proposal_counterpart() -> ProposalCounterpart:
    """Mocking ProposalCounterpart"""

    return ProposalCounterpart(
        id=uuid4(),
        descricao=faker.text(max_nb_chars=500),
        quantitativo=faker.random_int(min=1),
        previsto=faker.random_int(min=1),
        abginvest_tpproj_lei_contrpart_id=faker.random_int(min=1),
        proposta_abginvest_tpproj_lei_id=uuid4(),
    )
