from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import AbginvestTpprojLeiRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import AbginvestTpprojLei
from src.infra.entities import AbginvestTpprojLei as AbginvestTpprojLeiEntitie


class AbginvestTpprojLeiRepository(AbginvestTpprojLeiRepositoryInterface):
    """Class to manage AbginvestTpprojLei Repository"""

    @classmethod
    def insert_abginvest_tpproj_lei(
        cls, abordagem_investimento_id: int, lei_id: int, tipo_projeto_id: int
    ) -> AbginvestTpprojLei:
        """Insert data in category abginvestTpprjLei entity
        :param  -   abordagem_investimento_id: id investment approach of the relationship abginvest tpprj lei
                -   lei_id: id law of the relationship abginvest tpprj lei
                -   tipo_projeto_id: id type project of the relationship abginvest tpprj lei
        :return -   tuple with abginvest tpprj lei inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_abginvest_tpproj_lei = AbginvestTpprojLeiEntitie(
                    abordagem_investimento_id=abordagem_investimento_id,
                    lei_id=lei_id,
                    tipo_projeto_id=tipo_projeto_id,
                )
                db_connection.session.add(new_abginvest_tpproj_lei)
                db_connection.session.commit()

                return AbginvestTpprojLei(
                    id=new_abginvest_tpproj_lei.id,
                    abordagem_investimento_id=new_abginvest_tpproj_lei.abordagem_investimento_id,
                    lei_id=new_abginvest_tpproj_lei.lei_id,
                    tipo_projeto_id=new_abginvest_tpproj_lei.tipo_projeto_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_all_abginvest_tpproj_lei(cls) -> List[AbginvestTpprojLei]:
        """Select all data in AbginvestTpprojLei entity
        :param  -   is None
        :return -   List with all AbginvestTpprojLei
        """

        with DBConnectionHandler() as db_connection:
            try:
                query_data = []

                data = db_connection.session.query(AbginvestTpprojLeiEntitie).all()
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
    def select_abginvest_tpproj_lei(
        cls,
        id: int = None,
        abordagem_investimento_id: int = None,
        lei_id: int = None,
        tipo_projeto_id: int = None,
    ) -> List[AbginvestTpprojLei]:
        """Select data in AbginvestTpprojLei entity by id and/or
        abordagem_investimento_id and/or lei_id and/or tipo_projeto_id
        :param  -   abordagem_investimento_id: id investment approach of the relationship abginvest tpprj lei
                -   lei_id: id law of the relationship abginvest tpprj lei
                -   tipo_projeto_id: id type project of the relationship abginvest tpprj lei
        :return -   List with AbginvestTpprojLei selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                query_data = None

                if (
                    id
                    and not abordagem_investimento_id
                    and not lei_id
                    and not tipo_projeto_id
                ):
                    data = (
                        db_connection.session.query(AbginvestTpprojLeiEntitie)
                        .filter_by(id=id)
                        .one()
                    )
                    query_data = [data]

                elif (
                    abordagem_investimento_id
                    and not id
                    and not lei_id
                    and not tipo_projeto_id
                ):
                    data = (
                        db_connection.session.query(AbginvestTpprojLeiEntitie)
                        .filter_by(abordagem_investimento_id=abordagem_investimento_id)
                        .all()
                    )

                    query_data = data

                elif (
                    lei_id
                    and not id
                    and not abordagem_investimento_id
                    and not tipo_projeto_id
                ):
                    data = (
                        db_connection.session.query(AbginvestTpprojLeiEntitie)
                        .filter_by(lei_id=lei_id)
                        .all()
                    )
                    query_data = data

                elif (
                    tipo_projeto_id
                    and not id
                    and not abordagem_investimento_id
                    and not lei_id
                ):
                    data = (
                        db_connection.session.query(AbginvestTpprojLeiEntitie)
                        .filter_by(tipo_projeto_id=tipo_projeto_id)
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
