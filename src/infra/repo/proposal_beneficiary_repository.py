from uuid import UUID
from src.data.interface.proposal_beneficiary_repository_interface import (
    ProposalBeneficiaryRepositoryInterface,
)
from src.domain.models import ProposalBeneficiary
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_beneficiario import PropostaBeneficiario


class ProposalBeneficiaryRepository(ProposalBeneficiaryRepositoryInterface):
    """Class to manage Proposal Beneficiary Repository"""

    @classmethod
    def insert_proposal_beneficiary(
        cls, id: UUID, quantidade: int, proposta_id: UUID
    ) -> ProposalBeneficiary:
        """Insert data in proposal beneficiary entity
        :param  -   quantidade: beneficiary quantity
                -   proposta_id: proposal ID
        :return -   tuple with proposal beneficiary inserted
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_proposal_beneficiary = PropostaBeneficiario(
                    id=id, quantidade=quantidade, proposta_id=proposta_id
                )
                db_connection.session.add(new_proposal_beneficiary)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProposalBeneficiary(
                    id=new_proposal_beneficiary.id,
                    quantidade=new_proposal_beneficiary.quantidade,
                    proposta_id=new_proposal_beneficiary.proposta_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
