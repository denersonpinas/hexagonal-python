from faker import Faker
from sqlalchemy import text

from src.constants.reference import REFERENCE_TABLE
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.tipo_projeto import TipoProjeto
from .type_project_repository import TypeProjectRepository

faker = Faker()
type_project = TypeProjectRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_type_project():
    """Should insert type project"""

    name = faker.text(max_nb_chars=100)
    description = faker.text(max_nb_chars=250)

    # SQL commands
    new_type_project = type_project.insert_type_project(
        nome=name, descricao=description
    )

    # Select type_project
    with engine.begin() as conn:
        try:
            query_type_project = conn.execute(
                text(
                    "SELECT * FROM {}_tipoprojeto WHERE id='{}';".format(
                        REFERENCE_TABLE, new_type_project.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_type_project.id == query_type_project.id
            assert new_type_project.nome == query_type_project.nome
            assert new_type_project.descricao == query_type_project.descricao
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
                    "DELETE FROM {}_tipoprojeto WHERE id='{}';".format(
                        REFERENCE_TABLE, new_type_project.id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()


def test_select_all_type_project():
    """Should select all type project"""

    id = faker.random_number(digits=5)
    name = faker.text(max_nb_chars=100)
    description = faker.text(max_nb_chars=250)
    data = TipoProjeto(id=id, nome=name, descricao=description)

    # Insert type_project
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_tipoprojeto (id, nome, descricao)
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

    query_type_project = type_project.select_all_type_project()

    assert data in query_type_project

    # Deleting investment approach inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_tipoprojeto WHERE id='{}';".format(
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
