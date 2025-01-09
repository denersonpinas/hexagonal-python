from sqlalchemy import UUID
from src.data.interface.proposal_execution_location_repository_interface import (
    ProposalExecutionLocationRepositoryInterface,
)
from src.domain.models import ProposalExecutionLocation
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_local_execucao import PropostaLocalExecucao


class ProposalExecutionLocationRepository(ProposalExecutionLocationRepositoryInterface):
    """Class to manage Proposal Execution Location Repository"""

    @classmethod
    def insert_proposal_execution_location(
        cls, city_id: int, proposal_id: UUID
    ) -> ProposalExecutionLocation:
        """Insert data in proposal execution location entity
        :param  -   city_id: foreign key to city
                -   proposal_id: foreign key to proposal
        :return -   tuple with proposal execution location inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_location = PropostaLocalExecucao(
                    municipio_id=city_id, proposta_id=proposal_id
                )
                db_connection.session.add(new_location)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProposalExecutionLocation(
                    id=new_location.id,
                    municipio_id=new_location.municipio_id,
                    proposta_id=new_location.proposta_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
