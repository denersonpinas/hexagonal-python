from faker import Faker
from src.domain.models import GoalHistory

faker = Faker()


def mock_goal_history() -> GoalHistory:
    """Mocking GoalHistory"""

    return GoalHistory(
        id=faker.random_int(min=1),
        previsto=faker.text(max_nb_chars=500),
        alcancado=faker.text(max_nb_chars=500),
        historico_projetos_id=faker.random_int(min=1),
    )
