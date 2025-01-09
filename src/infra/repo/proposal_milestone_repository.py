from src.data.interface.proposal_milestone_repository_interface import (
    ProposalMilestoneRepositoryInterface,
)
from src.domain.models import ProposalMilestone
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_marcos import PropostaMarcos


class ProposalMilestoneRepository(ProposalMilestoneRepositoryInterface):
    """Class to manage Proposal Milestone Repository"""

    @classmethod
    def insert_proposal_milestone(
        cls, description: str, execution_date: str, proposal_id: str
    ) -> ProposalMilestone:
        """Insert data in proposal milestone entity
        :param  -   description: milestone description
                -   execution_date: milestone execution date
                -   proposal_id: foreign key to proposal
        :return -   tuple with proposal milestone inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_milestone = PropostaMarcos(
                    descricao=description,
                    execucao=execution_date,
                    proposta_id=proposal_id,
                )
                db_connection.session.add(new_milestone)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProposalMilestone(
                    id=new_milestone.id,
                    descricao=new_milestone.descricao,
                    execucao=new_milestone.execucao,
                    proposta_id=new_milestone.proposta_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
