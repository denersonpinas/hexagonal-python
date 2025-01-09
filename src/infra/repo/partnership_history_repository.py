from typing import Optional
from src.data.interface.partnership_history_repository_interface import (
    PartnershipHistoryRepositoryInterface,
)
from src.domain.models import PartnershipHistory
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.historico_de_parcerias import HistoricoDeParcerias


class PartnershipHistoryRepository(PartnershipHistoryRepositoryInterface):
    """Class to manage Partnership History Repository"""

    @classmethod
    def insert_partnership_history(
        cls,
        sponsors_number: int,
        renewal_number: int,
        proposal_id: str,
        additional_info: Optional[str] = None,
    ) -> PartnershipHistory:
        """Insert data in partnership history entity
        :param  -   sponsors_number: number of sponsors
                -   renewal_number: number of renewals
                -   proposal_id: foreign key to proposal
                -   additional_info: additional information
        :return -   tuple with partnership history inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_history = HistoricoDeParcerias(
                    numero_de_patrocinadores=sponsors_number,
                    numero_de_renovacao=renewal_number,
                    proposta_id=proposal_id,
                    informacoes_adicionais=additional_info,
                )
                db_connection.session.add(new_history)
                db_connection.session.flush()
                db_connection.session.commit()

                return PartnershipHistory(
                    id=new_history.id,
                    numero_de_patrocinadores=new_history.numero_de_patrocinadores,
                    numero_de_renovacao=new_history.numero_de_renovacao,
                    proposta_id=new_history.proposta_id,
                    informacoes_adicionais=new_history.informacoes_adicionais,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
