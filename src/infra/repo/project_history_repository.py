from sqlalchemy import UUID
from src.data.interface.project_history_repository_interface import (
    ProjectHistoryRepositoryInterface,
)
from src.domain.models import ProjectHistory
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.historico_projeto import HistoricoProjeto


class ProjectHistoryRepository(ProjectHistoryRepositoryInterface):
    """Class to manage Project History Repository"""

    @classmethod
    def insert_project_history(
        cls, investment_year: int, title: str, investment_type: str, proposal_id: UUID
    ) -> ProjectHistory:
        """Insert data in project history entity
        :param  -   investment_year: year of investment
                -   title: project title
                -   investment_type: type of investment
                -   proposal_id: foreign key to proposal
        :return -   tuple with project history inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_history = HistoricoProjeto(
                    ano_investimento=investment_year,
                    titulo=title,
                    tipo_investimento=investment_type,
                    proposta_id=proposal_id,
                )
                db_connection.session.add(new_history)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProjectHistory(
                    id=new_history.id,
                    ano_investimento=new_history.ano_investimento,
                    titulo=new_history.titulo,
                    tipo_investimento=new_history.tipo_investimento,
                    proposta_id=new_history.proposta_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
