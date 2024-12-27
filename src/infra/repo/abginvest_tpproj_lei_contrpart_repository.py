from typing import List
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import AbginvestTpprojLeiContrpartRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import AbginvestTpprojLeiContrpart
from src.infra.entities import (
    AbginvestTpprojLeiContrpart as AbginvestTpprojLeiContrpartEntitie,
)
from src.infra.entities.abginvest_tpproj_lei import AbginvestTpprojLei
from src.infra.entities.categoria_contrapartida import CategoriaContrapartida
from src.infra.entities.relacao_categoria_contrapartida import (
    RelacaoCategoriaContrapartida,
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
                    relacao_contrapartida_categoria_id=id_relacao_contrapartida_categoria,
                    abginvest_tpproj_lei_id=id_abginvest_tpproj_lei,
                )
                db_connection.session.add(new_abginvest_tpproj_lei_contrpart)
                db_connection.session.flush()
                db_connection.session.commit()

                return AbginvestTpprojLeiContrpart(
                    id=new_abginvest_tpproj_lei_contrpart.id,
                    ordem=new_abginvest_tpproj_lei_contrpart.ordem,
                    relacao_contrapartida_categoria_id=(
                        new_abginvest_tpproj_lei_contrpart.relacao_contrapartida_categoria_id
                    ),
                    abginvest_tpproj_lei_id=new_abginvest_tpproj_lei_contrpart.abginvest_tpproj_lei_id,
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
        with DBConnectionHandler() as db_connection:
            try:
                query = select(AbginvestTpprojLeiContrpartEntitie).options(
                    joinedload(
                        AbginvestTpprojLeiContrpartEntitie.relacao_categoria_contrapartida
                    )
                    .joinedload(RelacaoCategoriaContrapartida.categoria)
                    .joinedload(CategoriaContrapartida.subcategoria_de),
                    joinedload(
                        AbginvestTpprojLeiContrpartEntitie.relacao_categoria_contrapartida
                    ).joinedload(RelacaoCategoriaContrapartida.contrapartida),
                    joinedload(
                        AbginvestTpprojLeiContrpartEntitie.relacao_categoria_contrapartida
                    ),
                    joinedload(
                        AbginvestTpprojLeiContrpartEntitie.abginvest_tpproj_lei
                    ).joinedload(AbginvestTpprojLei.tipo_projeto),
                    joinedload(
                        AbginvestTpprojLeiContrpartEntitie.abginvest_tpproj_lei
                    ).joinedload(AbginvestTpprojLei.abordagem_investimento),
                    joinedload(
                        AbginvestTpprojLeiContrpartEntitie.abginvest_tpproj_lei
                    ).joinedload(AbginvestTpprojLei.lei),
                )
                return list(
                    db_connection.session.execute(query).unique().scalars().all()
                )
            except NoResultFound:
                return []
            except Exception as e:
                db_connection.session.rollback()
                raise e

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
                query = None

                if id and not id_abginvest_tpproj_lei:
                    query = (
                        select(AbginvestTpprojLeiContrpartEntitie)
                        .where(AbginvestTpprojLeiContrpartEntitie.id == id)
                        .options(
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.relacao_categoria_contrapartida
                            )
                            .joinedload(RelacaoCategoriaContrapartida.categoria)
                            .joinedload(CategoriaContrapartida.subcategoria_de),
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.relacao_categoria_contrapartida
                            ).joinedload(RelacaoCategoriaContrapartida.contrapartida),
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.relacao_categoria_contrapartida
                            ),
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.abginvest_tpproj_lei
                            ).joinedload(AbginvestTpprojLei.tipo_projeto),
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.abginvest_tpproj_lei
                            ).joinedload(AbginvestTpprojLei.abordagem_investimento),
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.abginvest_tpproj_lei
                            ).joinedload(AbginvestTpprojLei.lei),
                        )
                    )

                elif id_abginvest_tpproj_lei and not id:
                    query = (
                        select(AbginvestTpprojLeiContrpartEntitie)
                        .where(
                            AbginvestTpprojLeiContrpartEntitie.abginvest_tpproj_lei_id
                            == id_abginvest_tpproj_lei
                        )
                        .options(
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.relacao_categoria_contrapartida
                            )
                            .joinedload(RelacaoCategoriaContrapartida.categoria)
                            .joinedload(CategoriaContrapartida.subcategoria_de),
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.relacao_categoria_contrapartida
                            ).joinedload(RelacaoCategoriaContrapartida.contrapartida),
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.relacao_categoria_contrapartida
                            ),
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.abginvest_tpproj_lei
                            ).joinedload(AbginvestTpprojLei.tipo_projeto),
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.abginvest_tpproj_lei
                            ).joinedload(AbginvestTpprojLei.abordagem_investimento),
                            joinedload(
                                AbginvestTpprojLeiContrpartEntitie.abginvest_tpproj_lei
                            ).joinedload(AbginvestTpprojLei.lei),
                        )
                    )
                response: List[AbginvestTpprojLeiContrpart] = []
                for row in db_connection.session.execute(query).all():
                    response.append(row[0])
                return response
            except NoResultFound:
                return []
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return []
