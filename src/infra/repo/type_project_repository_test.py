from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.tipo_projeto import TipoProjeto
from .type_project_repository import TypeProjectRepository

faker = Faker()
type_project = TypeProjectRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_type_project():
    """Should insert TypeProject"""

    name = faker.text(max_nb_chars=100)
    description = faker.text(max_nb_chars=250)

    # SQL commands
    new_type_project = type_project.insert_type_project(
        nome=name, descricao=description
    )

    # Select TypeProject
    query = select(TipoProjeto).where(TipoProjeto.id == new_type_project.id)
    with DBConnectionHandler() as db_connection:
        try:
            for query_type_project in db_connection.session.execute(query):
                assert new_type_project.id == query_type_project[0].id
                assert new_type_project.nome == query_type_project[0].nome
                assert new_type_project.descricao == query_type_project[0].descricao

            # Deleting TypeProject Inserted
            type_project_inserted = db_connection.session.get(
                TipoProjeto, new_type_project.id
            )
            db_connection.session.delete(type_project_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_all_type_project():
    """Should select all type project"""

    name = faker.text(max_nb_chars=100)
    description = faker.text(max_nb_chars=250)
    data = TipoProjeto(nome=name, descricao=description)

    # Insert TypeProject
    with DBConnectionHandler() as db_connection:
        try:
            # Add TypeProject for test
            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_type_project = type_project.select_all_type_project()
            assert data in query_type_project

            # Deleting TypeProject Inserted
            type_project_inserted = db_connection.session.get(TipoProjeto, data.id)
            db_connection.session.delete(type_project_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
