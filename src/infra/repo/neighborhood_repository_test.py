from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.bairro import Bairro
from src.infra.entities.municipio import Municipio
from .neighborhood_repository import NeighborhoodRepository

faker = Faker()
neighborhood = NeighborhoodRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_neighborhood():
    """Should insert Neighborhood"""

    name = faker.city_prefix()

    with DBConnectionHandler() as db_connection:
        try:

            city = Municipio(nome=faker.city(), uf=faker.state_abbr())
            db_connection.session.add(city)
            db_connection.session.flush()
            db_connection.session.commit()
            city_id = city.id

            new_neighborhood = neighborhood.insert_neighborhood(
                name=name, city_id=city_id
            )

            # Select Neighborhood
            query = select(Bairro).where(Bairro.id == new_neighborhood.id)

            for query_neighborhood in db_connection.session.execute(query):
                assert new_neighborhood.id == query_neighborhood[0].id
                assert new_neighborhood.name == query_neighborhood[0].nome
                assert new_neighborhood.city_id == query_neighborhood[0].cidade_id_id

            # Deleting Neighborhood Inserted
            neighborhood_inserted = db_connection.session.get(
                Bairro, new_neighborhood.id
            )
            db_connection.session.delete(neighborhood_inserted)

            # Deleting City Created
            city_inserted = db_connection.session.get(Municipio, city_id)
            db_connection.session.delete(city_inserted)

            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
