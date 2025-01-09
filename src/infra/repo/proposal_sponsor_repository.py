from uuid import UUID
from src.data.interface.proposal_sponsor_repository_interface import (
    ProposalSponsorRepositoryInterface,
)
from src.domain.models import ProposalSponsor
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_patrocinador import PropostaPatrocinador


class ProposalSponsorRepository(ProposalSponsorRepositoryInterface):
    """Class to manage Proposal Sponsor Repository"""

    @classmethod
    def insert_proposal_sponsor(
        cls, nome: str, formato: str, valor: float, proposta_id: UUID
    ) -> ProposalSponsor:
        """Insert data in proposal sponsor entity
        :param  -   nome: sponsor name
                -   formato: sponsor format
                -   valor: sponsor value
                -   proposta_id: proposal ID
        :return -   tuple with proposal sponsor inserted
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_proposal_sponsor = PropostaPatrocinador(
                    nome=nome, formato=formato, valor=valor, proposta_id=proposta_id
                )
                db_connection.session.add(new_proposal_sponsor)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProposalSponsor(
                    id=new_proposal_sponsor.id,
                    nome=new_proposal_sponsor.nome,
                    formato=new_proposal_sponsor.formato,
                    valor=new_proposal_sponsor.valor,
                    proposta_id=new_proposal_sponsor.proposta_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
