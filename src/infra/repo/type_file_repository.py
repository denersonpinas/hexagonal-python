from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import TypeFileRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import TypeFile
from src.infra.entities import TipoArquivo


class TypeFileRepository(TypeFileRepositoryInterface):
    """Class to manage TypeFile Repository"""

    @classmethod
    def insert_type_file(
        cls, id: str, contexto: str, descricao: str, info: str
    ) -> TypeFile:
        """Insert data in category TypeFile entity
        :param  -   contexto: Context of the TypeFile
                -   descricao: Description of the TypeFile
                -   info: infor of the TypeFile
        :return -   tuple with TypeFile inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_type_file = TipoArquivo(
                    id=id,
                    contexto=contexto,
                    descricao=descricao,
                    info=info,
                )
                db_connection.session.add(new_type_file)
                db_connection.session.commit()

                return TypeFile(
                    id=new_type_file.id,
                    contexto=new_type_file.contexto,
                    descricao=new_type_file.descricao,
                    info=new_type_file.info,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_all_type_file(cls) -> List[TypeFile]:
        """Select all data in TypeFile entity
        :param  -   is None
        :return -   List with all TypeFile
        """

        with DBConnectionHandler() as db_connection:
            try:
                query_data = []

                data = db_connection.session.query(TipoArquivo).all()
                query_data = data

                return query_data
            except NoResultFound:
                return []
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return []

    @classmethod
    def select_type_file(cls, id: str = None) -> List[TypeFile]:
        """Select data in TypeFile entity by id
        :param  -   id: id of the register entity
        :return -   List with TypeFile selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                query_data = None

                if id:
                    data = (
                        db_connection.session.query(TipoArquivo).filter_by(id=id).one()
                    )
                    query_data = [data]

                return query_data
            except NoResultFound:
                return []
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None
