from faker import Faker
from src.domain.models import AbginvestTpprojLeiContrpart

faker = Faker()


def mock_abginvest_tpproj_lei_contrpart() -> AbginvestTpprojLeiContrpart:
    """Mocking AbginvestTpprojLeiContrpart"""

    return AbginvestTpprojLeiContrpart(
        id=faker.random_number(digits=5),
        ordem=faker.random_number(digits=5),
        id_relacao_contrapartida_categoria=faker.random_number(digits=5),
        id_abginvest_tpproj_lei=faker.random_number(digits=5),
    )
