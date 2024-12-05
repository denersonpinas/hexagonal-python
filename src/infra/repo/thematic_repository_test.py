from faker import Faker
from sqlalchemy import text

from src.constants.reference import REFERENCE_TABLE
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

    # Select thematic
    with engine.begin() as conn:
        try:
            query_thematic = conn.execute(
                text(
                    "SELECT * FROM {}_tematica WHERE id='{}';".format(
                        REFERENCE_TABLE, new_thematic.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_thematic.id == query_thematic.id
            assert new_thematic.descricao == query_thematic.descricao
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
                    "DELETE FROM {}_tematica WHERE id='{}';".format(
                        REFERENCE_TABLE, new_thematic.id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()


def test_select_thematic():
    """Should select Thematic"""

    id = faker.random_number(digits=5)
    description = faker.text(max_nb_chars=50)
    data = Tematica(id=id, descricao=description)

    # Insert thematic
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_tematica (id, descricao)
                    VALUES ('{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id, description
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_thematic_1 = thematic.select_all_thematic()
    query_thematic_2 = thematic.select_thematic(id=id)

    assert data in query_thematic_1
    assert data in query_thematic_2

    # Deleting investment approach inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_tematica WHERE id='{}';".format(REFERENCE_TABLE, id)
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()
