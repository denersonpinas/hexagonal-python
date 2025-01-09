from src.data.interface.city_repository_interface import CityRepositoryInterface
from src.domain.models import City
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.municipio import Municipio


class CityRepository(CityRepositoryInterface):
    """Class to manage City Repository"""

    @classmethod
    def insert_city(cls, name: str, state: str) -> City:
        """Insert data in city entity
        :param  -   name: city name
                -   state: state abbreviation
        :return -   tuple with city inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_city = Municipio(nome=name, uf=state)
                db_connection.session.add(new_city)
                db_connection.session.flush()
                db_connection.session.commit()

                return City(id=new_city.id, name=new_city.nome, state=new_city.uf)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
