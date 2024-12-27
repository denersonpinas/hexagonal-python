import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import TipoArquivo
from .type_file_repository import TypeFileRepository

faker = Faker()
type_file = TypeFileRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_type_file():
    """Should insert TypeFile"""

    id = str(uuid.uuid4().hex)
    constext = faker.text(max_nb_chars=32)
    description = faker.text(max_nb_chars=120)
    info = faker.text(max_nb_chars=1000)

    # SQL commands
    new_type_file = type_file.insert_type_file(
        id=id, contexto=constext, descricao=description, info=info
    )

    # Select Thematic
    query = select(TipoArquivo).where(TipoArquivo.id == new_type_file.id)
    with DBConnectionHandler() as db_connection:
        try:
            for query_type_file in db_connection.session.execute(query):
                assert new_type_file.id == query_type_file[0].id
                assert new_type_file.contexto == query_type_file[0].contexto
                assert new_type_file.descricao == query_type_file[0].descricao
                assert new_type_file.info == query_type_file[0].info

            # Deleting Thematic Inserted
            type_file_inserted = db_connection.session.get(
                TipoArquivo, new_type_file.id
            )
            db_connection.session.delete(type_file_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_type_file():
    """Should select TypeFile"""

    id = str(uuid.uuid4().hex)
    constext = faker.text(max_nb_chars=32)
    description = faker.text(max_nb_chars=120)
    info = faker.text(max_nb_chars=1000)
    data = TipoArquivo(id=id, contexto=constext, descricao=description, info=info)

    # Insert Thematic
    with DBConnectionHandler() as db_connection:
        try:
            # Add Thematic for test
            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_type_file_1 = type_file.select_all_type_file()
            query_type_file_2 = type_file.select_type_file(id=data.id)

            assert data in query_type_file_1
            assert data in query_type_file_2

            # Deleting Thematic Inserted
            type_file_inserted = db_connection.session.get(TipoArquivo, data.id)
            db_connection.session.delete(type_file_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
