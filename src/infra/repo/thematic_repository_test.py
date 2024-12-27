from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.tematica import Tematica
from src.infra.repo import ThematicRepository

faker = Faker()
thematic = ThematicRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_thematic():
    """Should insert Thematic"""
    description = faker.text(max_nb_chars=50)

    # SQL commands
    new_thematic = thematic.insert_thematic(descricao=description)

    # Select Thematic
    query = select(Tematica).where(Tematica.id == new_thematic.id)
    with DBConnectionHandler() as db_connection:
        try:
            for query_thematic in db_connection.session.execute(query):
                assert new_thematic.id == query_thematic[0].id
                assert new_thematic.descricao == query_thematic[0].descricao

            # Deleting Thematic Inserted
            thematic_inserted = db_connection.session.get(Tematica, new_thematic.id)
            db_connection.session.delete(thematic_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_thematic():
    """Should select Thematic"""

    description = faker.text(max_nb_chars=50)
    data = Tematica(descricao=description)

    # Insert Thematic
    with DBConnectionHandler() as db_connection:
        try:
            # Add Thematic for test
            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_thematic_1 = thematic.select_all_thematic()
            query_thematic_2 = thematic.select_thematic(id=data.id)

            assert data in query_thematic_1
            assert data in query_thematic_2

            # Deleting Thematic Inserted
            thematic_inserted = db_connection.session.get(Tematica, data.id)
            db_connection.session.delete(thematic_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
