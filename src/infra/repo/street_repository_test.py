from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.logradouro import Logradouro
from src.infra.entities.bairro import Bairro
from src.infra.entities.municipio import Municipio
from .street_repository import StreetRepository

faker = Faker()
street = StreetRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_street():
    """Should insert Street"""

    name = faker.street_name()

    with DBConnectionHandler() as db_connection:
        try:
            city = Municipio(nome=faker.city(), uf=faker.state_abbr())
            db_connection.session.add(city)
            db_connection.session.flush()

            neighborhood = Bairro(nome=faker.city_prefix(), cidade_id_id=city.id)
            db_connection.session.add(neighborhood)
            db_connection.session.flush()
            db_connection.session.commit()

            neighborhood_id = neighborhood.id

            # SQL commands
            new_street = street.insert_street(
                name=name, neighborhood_id=neighborhood_id
            )

            # Select Street
            query = select(Logradouro).where(Logradouro.id == new_street.id)

            for query_street in db_connection.session.execute(query):
                assert new_street.id == query_street[0].id
                assert new_street.nome == query_street[0].nome
                assert new_street.bairro_id_id == query_street[0].bairro_id_id

            # Deleting Street Inserted
            street_inserted = db_connection.session.get(Logradouro, new_street.id)
            db_connection.session.delete(street_inserted)

            # Deleting Neighborhood Created
            neighborhood_inserted = db_connection.session.get(Bairro, neighborhood_id)
            db_connection.session.delete(neighborhood_inserted)

            # Deleting City Created
            city_inserted = db_connection.session.get(Municipio, city.id)
            db_connection.session.delete(city_inserted)

            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
