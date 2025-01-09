from sqlalchemy import UUID
from src.data.interface.project_contact_point_repository_interface import (
    ProjectContactPointRepositoryInterface,
)
from src.domain.models import ProjectContactPoint
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.ponto_de_contato_projeto import PontoDeContatoProjeto


class ProjectContactPointRepository(ProjectContactPointRepositoryInterface):
    """Class to manage Project Contact Point Repository"""

    @classmethod
    def insert_project_contact(
        cls, name: str, email: str, position: str, proposal_id: UUID
    ) -> ProjectContactPoint:
        """Insert data in project contact point entity
        :param  -   name: contact person name
                -   email: contact email
                -   position: contact position
                -   proposal_id: foreign key to proposal
        :return -   tuple with project contact point inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_contact = PontoDeContatoProjeto(
                    nome=name, email=email, cargo=position, proposta_id=proposal_id
                )
                db_connection.session.add(new_contact)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProjectContactPoint(
                    id=new_contact.id,
                    nome=new_contact.nome,
                    email=new_contact.email,
                    cargo=new_contact.cargo,
                    proposta_id=new_contact.proposta_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
