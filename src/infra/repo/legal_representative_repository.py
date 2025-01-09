from typing import Optional
from src.data.interface.legal_representative_repository_interface import (
    LegalRepresentativeRepositoryInterface,
)
from src.domain.models import LegalRepresentative
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.representante_legal import RepresentanteLegal


class LegalRepresentativeRepository(LegalRepresentativeRepositoryInterface):
    """Class to manage Legal Representative Repository"""

    @classmethod
    def insert_legal_representative(
        cls,
        name: str,
        cpf: str,
        email: str,
        position: str,
        proposal_id: str,
        summary: Optional[str] = None,
    ) -> LegalRepresentative:
        """Insert data in legal representative entity
        :param  -   name: representative name
                -   cpf: representative document number
                -   email: representative email
                -   position: representative position
                -   proposal_id: foreign key to proposal
                -   summary: representative summary
        :return -   tuple with legal representative inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_representative = RepresentanteLegal(
                    nome=name,
                    cpf=cpf,
                    email=email,
                    cargo=position,
                    proposta_id=proposal_id,
                    resumo=summary,
                )
                db_connection.session.add(new_representative)
                db_connection.session.flush()
                db_connection.session.commit()

                return LegalRepresentative(
                    id=new_representative.id,
                    nome=new_representative.nome,
                    cpf=new_representative.cpf,
                    email=new_representative.email,
                    cargo=new_representative.cargo,
                    proposta_id=new_representative.proposta_id,
                    resumo=new_representative.resumo,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
