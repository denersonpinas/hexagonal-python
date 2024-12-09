from faker import Faker
from src.domain.models import AbginvestTpprojLei

faker = Faker()


def mock_abginvest_tpproj_lei() -> AbginvestTpprojLei:
    """Mocking AbginvestTpprojLei"""

    return AbginvestTpprojLei(
        id=faker.random_number(digits=5),
        abordagem_investimento_id=faker.random_number(digits=5),
        lei_id=faker.random_number(digits=5),
        tipo_pojeto_id=faker.random_number(digits=5),
    )
