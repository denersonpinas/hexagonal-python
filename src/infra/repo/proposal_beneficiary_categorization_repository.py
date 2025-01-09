from uuid import UUID
from src.data.interface.proposal_beneficiary_categorization_repository_interface import (
    ProposalBeneficiaryCategorizationRepositoryInterface,
)
from src.domain.models import ProposalBeneficiaryCategorization
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_beneficiario_categorizacao import (
    PropostaBeneficiarioCategorizacao,
)


class ProposalBeneficiaryCategorizationRepository(
    ProposalBeneficiaryCategorizationRepositoryInterface
):
    """Class to manage Proposal Beneficiary Categorization Repository"""

    @classmethod
    def insert_proposal_beneficiary_categorization(
        cls, categorizacao_id: int, proposta_beneficiario_id: UUID
    ) -> ProposalBeneficiaryCategorization:
        """Insert data in proposal beneficiary categorization entity
        :param  -   categorizacao_id: categorization ID
                -   proposta_beneficiario_id: proposal beneficiary ID
        :return -   tuple with proposal beneficiary categorization inserted
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_proposal_beneficiary_categorization = (
                    PropostaBeneficiarioCategorizacao(
                        categorizacao_id=categorizacao_id,
                        proposta_beneficiario_id=proposta_beneficiario_id,
                    )
                )
                db_connection.session.add(new_proposal_beneficiary_categorization)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProposalBeneficiaryCategorization(
                    id=new_proposal_beneficiary_categorization.id,
                    categorizacao_id=new_proposal_beneficiary_categorization.categorizacao_id,
                    proposta_beneficiario_id=new_proposal_beneficiary_categorization.proposta_beneficiario_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
