from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.municipio import Municipio
from .city_repository import CityRepository

faker = Faker()
city = CityRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_city():
    """Should insert City"""

    name = faker.city()
    state = faker.state_abbr()

    # SQL commands
    new_city = city.insert_city(name=name, state=state)

    # Select City
    query = select(Municipio).where(Municipio.id == new_city.id)
    with DBConnectionHandler() as db_connection:
        try:
            for query_city in db_connection.session.execute(query):
                assert new_city.id == query_city[0].id
                assert new_city.name == query_city[0].nome
                assert new_city.state == query_city[0].uf

            # Deleting City Inserted
            city_inserted = db_connection.session.get(Municipio, new_city.id)
            db_connection.session.delete(city_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
