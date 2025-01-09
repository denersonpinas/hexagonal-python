from faker import Faker
from src.domain.models import ProposalMilestone

faker = Faker()


def mock_proposal_milestone() -> ProposalMilestone:
    """Mocking ProposalMilestone"""

    return ProposalMilestone(
        id=faker.uuid4(),
        descricao=faker.text(max_nb_chars=500),
        execucao=faker.date(),
        proposta_id=faker.uuid4(),
    )
