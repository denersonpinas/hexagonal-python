from src.data.interface.supply_history_repository_interface import (
    SupplyHistoryRepositoryInterface,
)
from src.domain.models import SupplyHistory
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.historico_de_fornecimento import HistoricoDeFornecimento


class SupplyHistoryRepository(SupplyHistoryRepositoryInterface):
    """Class to manage Supply History Repository"""

    @classmethod
    def insert_supply_history(
        cls, service_provided: str, hiring_manager: str, proposal_id: str
    ) -> SupplyHistory:
        """Insert data in supply history entity
        :param  -   service_provided: service provided description
                -   hiring_manager: hiring manager name
                -   proposal_id: foreign key to proposal
        :return -   tuple with supply history inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_history = HistoricoDeFornecimento(
                    servico_prestado=service_provided,
                    responsavel_contratacao=hiring_manager,
                    proposta_id=proposal_id,
                )
                db_connection.session.add(new_history)
                db_connection.session.flush()
                db_connection.session.commit()

                return SupplyHistory(
                    id=new_history.id,
                    servico_prestado=new_history.servico_prestado,
                    responsavel_contratacao=new_history.responsavel_contratacao,
                    proposta_id=new_history.proposta_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
