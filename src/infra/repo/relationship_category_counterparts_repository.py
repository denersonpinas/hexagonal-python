from typing import List
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import RelationshipCategoryCounterpartsRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import RelationshipCategoryCounterparts
from src.infra.entities import RelacaoCategoriaContrapartida
from src.infra.entities.categoria_contrapartida import CategoriaContrapartida


class RelationshipCategoryCounterpartsRepository(
    RelationshipCategoryCounterpartsRepositoryInterface
):
    """Class to manage Relationship Category Counterparts Repository"""

    @classmethod
    def insert_relationship_category_counterparts(
        cls, categoria_id: int, contrapartida_id: int
    ) -> RelationshipCategoryCounterparts:
        """Insert data in RelacaoCategoriaContrapartidas entity
        :param  -   categoria_id: id Category in Relationship Category Counterparts
                -   contrapartida_id: id Counterparts in Relationship Category Counterparts
        :return -   tuple with RelationshipCategoryCounterparts inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_relation_categ_countr = RelacaoCategoriaContrapartida(
                    categoria_id=categoria_id, contrapartida_id=contrapartida_id
                )
                db_connection.session.add(new_relation_categ_countr)
                db_connection.session.flush()
                db_connection.session.commit()

                return RelationshipCategoryCounterparts(
                    id=new_relation_categ_countr.id,
                    categoria_id=new_relation_categ_countr.categoria_id,
                    contrapartida_id=new_relation_categ_countr.contrapartida_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @classmethod
    def select_all_relationship_category_counterparts(
        cls,
    ) -> List[RelationshipCategoryCounterparts]:
        """Select all data in RelacaoCategoriaContrapartidas entity
        :param  -   is None
        :return -   List with all RelationshipCategoryCounterparts
        """

        with DBConnectionHandler() as db_connection:
            try:
                # Usando joinedload para carregar os relacionamentos
                query = select(RelacaoCategoriaContrapartida).options(
                    joinedload(RelacaoCategoriaContrapartida.categoria).joinedload(
                        CategoriaContrapartida.subcategoria_de
                    ),
                    joinedload(RelacaoCategoriaContrapartida.contrapartida),
                )
                response: List[RelationshipCategoryCounterparts] = []
                rows = db_connection.session.scalars(query).all()
                response.extend(rows)

                return response
            except NoResultFound:
                return []
            except Exception as e:
                db_connection.session.rollback()
                raise e

    @classmethod
    def select_relationship_category_counterparts(
        cls, id: int = None, categoria_id: int = None, contrapartida_id: int = None
    ) -> List[RelationshipCategoryCounterparts]:
        """Select data in RelacaoCategoriaContrapartidas entity by id or categoria_id or contrapartida_id
        :param  -   id: Id of the register
                -   categoria_id: id Category in Relationship Category Counterparts
                -   contrapartida_id: id Counterparts in Relationship Category Counterparts
        :return -   List with Relationship Category Counterparts selected
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = None
                response: List[RelationshipCategoryCounterparts] = []
                if id and not categoria_id and not contrapartida_id:
                    query = (
                        select(RelacaoCategoriaContrapartida)
                        .where(RelacaoCategoriaContrapartida.id == id)
                        .options(
                            joinedload(
                                RelacaoCategoriaContrapartida.categoria
                            ).joinedload(CategoriaContrapartida.subcategoria_de),
                            joinedload(RelacaoCategoriaContrapartida.contrapartida),
                        )
                    )
                    for row in db_connection.session.execute(query).all():
                        response.append(row[0])
                elif categoria_id and not id and not contrapartida_id:
                    query = (
                        select(RelacaoCategoriaContrapartida)
                        .where(
                            RelacaoCategoriaContrapartida.categoria_id == categoria_id
                        )
                        .options(
                            joinedload(
                                RelacaoCategoriaContrapartida.categoria
                            ).joinedload(CategoriaContrapartida.subcategoria_de),
                            joinedload(RelacaoCategoriaContrapartida.contrapartida),
                        )
                    )
                    for row in db_connection.session.execute(query).all():
                        response.append(row[0])
                elif contrapartida_id and not id and not categoria_id:
                    query = (
                        select(RelacaoCategoriaContrapartida)
                        .where(
                            RelacaoCategoriaContrapartida.contrapartida_id
                            == contrapartida_id
                        )
                        .options(
                            joinedload(
                                RelacaoCategoriaContrapartida.categoria
                            ).joinedload(CategoriaContrapartida.subcategoria_de),
                            joinedload(RelacaoCategoriaContrapartida.contrapartida),
                        )
                    )
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
