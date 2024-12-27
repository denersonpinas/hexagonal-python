from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.lei import Lei
from .law_repository import LawRepository

faker = Faker()
law = LawRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_law():
    """Should insert Law"""

    name = faker.text(max_nb_chars=100)
    description = faker.text(max_nb_chars=250)

    # SQL commands
    new_law = law.insert_law(nome=name, descricao=description)

    # Select Law
    query = select(Lei).where(Lei.id == new_law.id)
    with DBConnectionHandler() as db_connection:
        try:
            for query_law in db_connection.session.execute(query):
                assert new_law.id == query_law[0].id
                assert new_law.nome == query_law[0].nome
                assert new_law.descricao == query_law[0].descricao

            # Deleting Law Inserted
            law_inserted = db_connection.session.get(Lei, new_law.id)
            db_connection.session.delete(law_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_all_law():
    """Should select all Law"""

    name = faker.text(max_nb_chars=100)
    description = faker.text(max_nb_chars=250)
    data = Lei(nome=name, descricao=description)

    # Insert Law
    with DBConnectionHandler() as db_connection:
        try:
            # Add Law for test
            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_law = law.select_all_law()
            assert data in query_law

            # Deleting Law Inserted
            law_inserted = db_connection.session.get(Lei, data.id)
            db_connection.session.delete(law_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
