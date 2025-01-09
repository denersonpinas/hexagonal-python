from src.data.interface.street_repository_interface import StreetRepositoryInterface
from src.domain.models import Street
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.logradouro import Logradouro


class StreetRepository(StreetRepositoryInterface):
    """Class to manage Street Repository"""

    @classmethod
    def insert_street(cls, name: str, neighborhood_id: int) -> Street:
        """Insert data in street entity
        :param  -   name: street name
                -   neighborhood_id: foreign key to neighborhood
        :return -   tuple with street inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_street = Logradouro(nome=name, bairro_id_id=neighborhood_id)
                db_connection.session.add(new_street)
                db_connection.session.flush()
                db_connection.session.commit()

                return Street(
                    id=new_street.id,
                    nome=new_street.nome,
                    bairro_id_id=new_street.bairro_id_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
