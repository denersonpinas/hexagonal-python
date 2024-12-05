import uuid
from faker import Faker
from sqlalchemy import text

from src.constants.reference import REFERENCE_TABLE
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

    # Select type_file
    with engine.begin() as conn:
        try:
            query_type_file = conn.execute(
                text(
                    "SELECT * FROM {}_tipoarquivo WHERE id='{}';".format(
                        REFERENCE_TABLE, new_type_file.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_type_file.id == query_type_file.id
            assert new_type_file.contexto == query_type_file.contexto
            assert new_type_file.descricao == query_type_file.descricao
            assert new_type_file.info == query_type_file.info
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting investment approach inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_tipoarquivo WHERE id='{}';".format(
                        REFERENCE_TABLE, new_type_file.id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()


def test_select_type_file():
    """Should select TypeFile"""

    id = faker.text(max_nb_chars=32)
    constext = faker.text(max_nb_chars=32)
    description = faker.text(max_nb_chars=120)
    info = faker.text(max_nb_chars=1000)
    data = TipoArquivo(id=id, contexto=constext, descricao=description, info=info)

    # Insert type_file
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_tipoarquivo (id, contexto, descricao, info)
                    VALUES ('{}', '{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id, constext, description, info
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_type_file_1 = type_file.select_all_type_file()
    query_type_file_2 = type_file.select_type_file(id=id)

    assert data in query_type_file_1
    assert data in query_type_file_2

    # Deleting investment approach inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_tipoarquivo WHERE id='{}';".format(
                        REFERENCE_TABLE, id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()
