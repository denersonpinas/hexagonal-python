from typing import Optional
from sqlalchemy import UUID
from src.data.interface.proposal_counterpart_repository_interface import (
    ProposalCounterpartRepositoryInterface,
)
from src.domain.models import ProposalCounterpart
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_contrapartida import PropostaContrapartida


class ProposalCounterpartRepository(ProposalCounterpartRepositoryInterface):
    """Class to manage Proposal Counterpart Repository"""

    @classmethod
    def insert_proposal_counterpart(
        cls,
        id: UUID,
        description: str,
        quantity: int,
        investment_type_law_counterpart_id: int,
        proposal_investment_type_law_id: UUID,
        expected: Optional[int] = None,
    ) -> ProposalCounterpart:
        """Insert data in proposal counterpart entity
        :param  -   id: unique identifier
                -   description: counterpart description
                -   quantity: counterpart quantity
                -   investment_type_law_counterpart_id: foreign key to investment type law counterpart
                -   proposal_investment_type_law_id: foreign key to proposal investment type law
                -   expected: expected quantity
        :return -   tuple with proposal counterpart inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_counterpart = PropostaContrapartida(
                    id=id,
                    descricao=description,
                    quantitativo=quantity,
                    previsto=expected,
                    abginvest_tpproj_lei_contrpart_id=investment_type_law_counterpart_id,
                    proposta_abginvest_tpproj_lei_id=proposal_investment_type_law_id,
                )
                db_connection.session.add(new_counterpart)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProposalCounterpart(
                    id=new_counterpart.id,
                    descricao=new_counterpart.descricao,
                    quantitativo=new_counterpart.quantitativo,
                    previsto=new_counterpart.previsto,
                    abginvest_tpproj_lei_contrpart_id=new_counterpart.abginvest_tpproj_lei_contrpart_id,
                    proposta_abginvest_tpproj_lei_id=new_counterpart.proposta_abginvest_tpproj_lei_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
