from uuid import uuid4
from faker import Faker
from src.domain.models import ProposalFile

faker = Faker()


def mock_proposal_file() -> ProposalFile:
    """Mocking ProposalFile"""

    return ProposalFile(
        id=uuid4(),
        nome=faker.file_name()[:100],
        extensao=faker.file_extension()[:10],
        tamanho=faker.random_int(min=1),
        uri=faker.uri()[:500],
        proposta_id=uuid4(),
        tipo_id=uuid4(),
    )
