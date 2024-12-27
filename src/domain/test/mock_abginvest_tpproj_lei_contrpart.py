from faker import Faker
from src.domain.models import AbginvestTpprojLeiContrpart

faker = Faker()


def mock_abginvest_tpproj_lei_contrpart() -> AbginvestTpprojLeiContrpart:
    """Mocking AbginvestTpprojLeiContrpart"""

    return AbginvestTpprojLeiContrpart(
        id=faker.random_number(digits=5),
        ordem=faker.random_number(digits=5),
        relacao_contrapartida_categoria_id=faker.random_number(digits=5),
        abginvest_tpproj_lei_id=faker.random_number(digits=5),
    )
