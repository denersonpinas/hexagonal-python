from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import AbginvestTpprojLeiContrpartRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import AbginvestTpprojLeiContrpart
from src.infra.entities import (
    AbginvestTpprojLeiContrpart as AbginvestTpprojLeiContrpartEntitie,
)


class AbginvestTpprojLeiContrpartRepository(
    AbginvestTpprojLeiContrpartRepositoryInterface
):
    """Class to manage AbginvestTpprojLeiContrpart Repository"""

    @classmethod
    def insert_abginvest_tpproj_lei_contrpart(
        cls,
        ordem: int,
        id_relacao_contrapartida_categoria: int,
        id_abginvest_tpproj_lei: int,
    ) -> AbginvestTpprojLeiContrpart:
        """Insert data in category abginvestTpprjLeiContrpart entity
        :param  -   ordem: order of the create AbginvestTpprjLeiContrpart
                -   id_relacao_contrapartida: id of the relationship
                counterpart relation with AbginvestTpprjLeiContrpart
                -   id_abginvest_tpproj_lei: id of the relationship AbginvestTpprjLei with AbginvestTpprjLeiContrpart
        :return -   tuple with AbginvestTpprjLeiContrpart inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_abginvest_tpproj_lei_contrpart = AbginvestTpprojLeiContrpartEntitie(
                    ordem=ordem,
                    id_relacao_contrapartida_categoria=id_relacao_contrapartida_categoria,
                    id_abginvest_tpproj_lei=id_abginvest_tpproj_lei,
                )
                db_connection.session.add(new_abginvest_tpproj_lei_contrpart)
                db_connection.session.commit()

                return AbginvestTpprojLeiContrpart(
                    id=new_abginvest_tpproj_lei_contrpart.id,
                    ordem=new_abginvest_tpproj_lei_contrpart.ordem,
                    id_relacao_contrapartida_categoria=(
                        new_abginvest_tpproj_lei_contrpart.id_relacao_contrapartida_categoria
                    ),
                    id_abginvest_tpproj_lei=new_abginvest_tpproj_lei_contrpart.id_abginvest_tpproj_lei,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_all_abginvest_tpproj_lei_contrpart(
        cls,
    ) -> List[AbginvestTpprojLeiContrpart]:
        """Select all data in AbginvestTpprojLeiContrpart entity
        :param  -   is None
        :return -   List with all AbginvestTpprojLeiContrpart
        """

        with DBConnectionHandler() as db_connection:
            try:
                query_data = []

                data = db_connection.session.query(
                    AbginvestTpprojLeiContrpartEntitie
                ).all()
                query_data = data

                return query_data
            except NoResultFound:
                return []
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return []

    @classmethod
    def select_abginvest_tpproj_lei_contrpart(
        cls, id: int = None, id_abginvest_tpproj_lei: int = None
    ) -> List[AbginvestTpprojLeiContrpart]:
        """Select data in AbginvestTpprojLeiContrpart entity by id and/or
        abordagem_investimento_id and/or lei_id and/or tipo_pojeto_id
        :param  -   id: id of the  register
                -   id_abginvest_tpproj_lei: id of the relationship AbginvestTpprjLei with AbginvestTpprjLeiContrpart
        :return -   List with AbginvestTpprojLeiContrpart selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                query_data = None

                if id and not id_abginvest_tpproj_lei:
                    data = (
                        db_connection.session.query(AbginvestTpprojLeiContrpartEntitie)
                        .filter_by(id=id)
                        .one()
                    )
                    query_data = [data]

                elif id_abginvest_tpproj_lei and not id:
                    data = (
                        db_connection.session.query(AbginvestTpprojLeiContrpartEntitie)
                        .filter_by(id_abginvest_tpproj_lei=id_abginvest_tpproj_lei)
                        .all()
                    )

                    query_data = data

                return query_data
            except NoResultFound:
                return []
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None
