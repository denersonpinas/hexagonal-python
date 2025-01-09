from sqlalchemy import UUID
from src.data.interface.proposal_investment_type_law_repository_interface import (
    ProposalInvestmentTypeLawRepositoryInterface,
)
from src.domain.models import ProposalInvestmentTypeLaw
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_abginvest_tpproj_lei import PropostaAbginvestTpprojLei


class ProposalInvestmentTypeLawRepository(ProposalInvestmentTypeLawRepositoryInterface):
    """Class to manage Proposal Investment Type Law Repository"""

    @classmethod
    def insert_proposal_investment_type_law(
        cls, id: UUID, investment_type_law_id: int, proposal_id: UUID
    ) -> ProposalInvestmentTypeLaw:
        """Insert data in proposal investment type law entity
        :param  -   id: unique identifier
                -   investment_type_law_id: foreign key to investment type law
                -   proposal_id: foreign key to proposal
        :return -   tuple with proposal investment type law inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_investment_type_law = PropostaAbginvestTpprojLei(
                    id=id,
                    abginvest_tpproj_lei_id=investment_type_law_id,
                    proposta_id=proposal_id,
                )
                db_connection.session.add(new_investment_type_law)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProposalInvestmentTypeLaw(
                    id=new_investment_type_law.id,
                    abginvest_tpproj_lei_id=new_investment_type_law.abginvest_tpproj_lei_id,
                    proposta_id=new_investment_type_law.proposta_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
