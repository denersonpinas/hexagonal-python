from faker import Faker
from sqlalchemy import text

from src.constants.reference import REFERENCE_TABLE
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.lei import Lei
from .law_repository import LawRepository

faker = Faker()
law = LawRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_law():
    """Should insert law"""

    name = faker.text(max_nb_chars=100)
    description = faker.text(max_nb_chars=250)

    # SQL commands
    new_law = law.insert_law(nome=name, descricao=description)

    # Select law
    with engine.begin() as conn:
        try:
            query_law = conn.execute(
                text(
                    "SELECT * FROM {}_lei WHERE id='{}';".format(
                        REFERENCE_TABLE, new_law.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_law.id == query_law.id
            assert new_law.nome == query_law.nome
            assert new_law.descricao == query_law.descricao
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
                    "DELETE FROM {}_lei WHERE id='{}';".format(
                        REFERENCE_TABLE, new_law.id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()


def test_select_all_law():
    """Should select all law"""

    id = faker.random_number(digits=5)
    name = faker.text(max_nb_chars=100)
    description = faker.text(max_nb_chars=250)
    data = Lei(id=id, nome=name, descricao=description)

    # Insert law
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_lei (id, nome, descricao)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id, name, description
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_law = law.select_all_law()

    assert data in query_law

    # Deleting investment approach inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text("DELETE FROM {}_lei WHERE id='{}';".format(REFERENCE_TABLE, id))
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()
