from src.data.interface.goal_history_repository_interface import (
    GoalHistoryRepositoryInterface,
)
from src.domain.models import GoalHistory
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.historico_de_metas import HistoricoDeMetas


class GoalHistoryRepository(GoalHistoryRepositoryInterface):
    """Class to manage Goal History Repository"""

    @classmethod
    def insert_goal_history(
        cls, expected: str, achieved: str, project_history_id: int
    ) -> GoalHistory:
        """Insert data in goal history entity
        :param  -   expected: expected goal
                -   achieved: achieved goal
                -   project_history_id: foreign key to project history
        :return -   tuple with goal history inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_goal = HistoricoDeMetas(
                    previsto=expected,
                    alcancado=achieved,
                    historico_projetos_id=project_history_id,
                )
                db_connection.session.add(new_goal)
                db_connection.session.flush()
                db_connection.session.commit()

                return GoalHistory(
                    id=new_goal.id,
                    previsto=new_goal.previsto,
                    alcancado=new_goal.alcancado,
                    historico_projetos_id=new_goal.historico_projetos_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
