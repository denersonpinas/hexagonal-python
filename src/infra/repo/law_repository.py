from typing import List
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound

from src.data.interface.law_repository_interface import LawRepositoryInterface
from src.domain.models import Law
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.lei import Lei


class LawRepository(LawRepositoryInterface):
    """Class to manage Law Repository"""

    @classmethod
    def insert_law(cls, nome: str, descricao: str) -> Law:
        """Insert data in law entity
        :param  -   nome: law name
                -   descricao: law description
        :return -   tuple with law inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_law = Lei(nome=nome, descricao=descricao)
                db_connection.session.add(new_law)
                db_connection.session.flush()
                db_connection.session.commit()

                return Law(
                    id=new_law.id,
                    nome=new_law.nome,
                    descricao=new_law.descricao,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_all_law(cls) -> List[Law]:
        """Select all data in Law entity
        :param  -   is None
        :return -   List with all Law
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = select(Lei)
                response: List[Law] = []
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
