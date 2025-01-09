from src.data.interface.neighborhood_repository_interface import (
    NeighborhoodRepositoryInterface,
)
from src.domain.models import Neighborhood
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.bairro import Bairro


class NeighborhoodRepository(NeighborhoodRepositoryInterface):
    """Class to manage Neighborhood Repository"""

    @classmethod
    def insert_neighborhood(cls, name: str, city_id: int) -> Neighborhood:
        """Insert data in neighborhood entity
        :param  -   name: neighborhood name
                -   city_id: foreign key to city
        :return -   tuple with neighborhood inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_neighborhood = Bairro(nome=name, cidade_id_id=city_id)
                db_connection.session.add(new_neighborhood)
                db_connection.session.flush()
                db_connection.session.commit()

                return Neighborhood(
                    id=new_neighborhood.id,
                    name=new_neighborhood.nome,
                    city_id=new_neighborhood.cidade_id_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
