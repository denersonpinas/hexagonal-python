from typing import List
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import ThematicRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import Thematic
from src.infra.entities import Tematica


class ThematicRepository(ThematicRepositoryInterface):
    """Class to manage Thematic Repository"""

    @classmethod
    def insert_thematic(cls, descricao: str) -> Thematic:
        """Insert data in category Thematic entity
        :param  -   descricao: Description of the Thematic
        :return -   tuple with Thematic inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_thematic = Tematica(descricao=descricao)
                db_connection.session.add(new_thematic)
                db_connection.session.flush()
                db_connection.session.commit()

                return Thematic(id=new_thematic.id, descricao=new_thematic.descricao)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_all_thematic(cls) -> List[Thematic]:
        """Select all data in Thematic entity
        :param  -   is None
        :return -   List with all Thematic
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = select(Tematica)
                response: List[Thematic] = []
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

    @classmethod
    def select_thematic(cls, id: int = None) -> List[Thematic]:
        """Select data in Thematic entity by id
        :param  -   id: id of the register entity
        :return -   List with Thematic selected
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = select(Tematica).where(Tematica.id == id)
                response: List[Thematic] = []
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
