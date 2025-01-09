from src.data.interface.proposal_thematic_repository_interface import (
    ProposalThematicRepositoryInterface,
)
from src.domain.models import ProposalThematic
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_tematica import PropostaTematica


class ProposalThematicRepository(ProposalThematicRepositoryInterface):
    """Class to manage Proposal Thematic Repository"""

    @classmethod
    def insert_proposal_thematic(
        cls, proposal_id: str, thematic_id: int
    ) -> ProposalThematic:
        """Insert data in proposal thematic entity
        :param  -   proposal_id: foreign key to proposal
                -   thematic_id: foreign key to thematic
        :return -   tuple with proposal thematic inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_thematic = PropostaTematica(
                    proposta_id=proposal_id, tematica_id=thematic_id
                )
                db_connection.session.add(new_thematic)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProposalThematic(
                    id=new_thematic.id,
                    proposta_id=new_thematic.proposta_id,
                    tematica_id=new_thematic.tematica_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
