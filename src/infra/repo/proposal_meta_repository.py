from uuid import UUID
from src.data.interface.proposal_meta_repository_interface import (
    PropostaMetaRepositoryInterface,
)
from src.infra.config.db_config import DBConnectionHandler
from src.domain.models import ProposalMeta
from src.infra.entities.proposta_meta import PropostaMeta


class ProposalMetaRepository(PropostaMetaRepositoryInterface):
    """Class to manage ProposalMeta Repository"""

    @classmethod
    def insert_proposal_meta(
        cls, order: int, goal: str, quantity: int, proposal_id: UUID
    ) -> ProposalMeta:
        """Insert data into proposal_meta entity
        :param  -   order: order of the proposal meta
                -   goal: description of the goal
                -   quantity: quantity of the goal
                -   proposal_id: UUID of the associated proposal
        :return -   tuple with the inserted proposal_meta
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_proposal_meta = PropostaMeta(
                    ordem=order,
                    meta=goal,
                    quantitativo=quantity,
                    proposta_id=proposal_id,
                )
                db_connection.session.add(new_proposal_meta)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProposalMeta(
                    id=new_proposal_meta.id,
                    ordem=new_proposal_meta.ordem,
                    meta=new_proposal_meta.meta,
                    quantitativo=new_proposal_meta.quantitativo,
                    proposta_id=new_proposal_meta.proposta_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
