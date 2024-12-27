from typing import List
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import TypeProjectRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import TypeProject
from src.infra.entities import TipoProjeto


class TypeProjectRepository(TypeProjectRepositoryInterface):
    """Class to manage TypeProject Repository"""

    @classmethod
    def insert_type_project(cls, nome: str, descricao: str) -> TypeProject:
        """Insert data in TypeProject entity
        :param  -   nome: type project name
                -   descricao: type project description
        :return -   tuple with type project inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_type_project = TipoProjeto(nome=nome, descricao=descricao)
                db_connection.session.add(new_type_project)
                db_connection.session.flush()
                db_connection.session.commit()

                return TypeProject(
                    id=new_type_project.id,
                    nome=new_type_project.nome,
                    descricao=new_type_project.descricao,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_all_type_project(cls) -> List[TypeProject]:
        """Select all data in TypeProject entity
        :param  -   is None
        :return -   List with all TypeProject
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = select(TipoProjeto)
                response: List[TypeProject] = []
                for row in db_connection.session.execute(query).all():
                    response.append(row[0])
                return response
            except NoResultFound:
                return []
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return []
