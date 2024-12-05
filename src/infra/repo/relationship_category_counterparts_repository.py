from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import RelationshipCategoryCounterpartsRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import RelationshipCategoryCounterparts
from src.infra.entities import RelacaoCategoriaContrapartida


class RelationshipCategoryCounterpartsRepository(
    RelationshipCategoryCounterpartsRepositoryInterface
):
    """Class to manage Relationship Category Counterparts Repository"""

    @classmethod
    def insert_relationship_category_counterparts(
        self, categoria_id: int, contrapartida_id: int
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
        self,
    ) -> List[RelationshipCategoryCounterparts]:
        """Select all data in RelacaoCategoriaContrapartidas entity
        :param  -   is None
        :return -   List with all RelationshipCategoryCounterparts
        """

        with DBConnectionHandler() as db_connection:
            try:
                query_data = []

                data = db_connection.session.query(RelacaoCategoriaContrapartida).all()
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
    def select_relationship_category_counterparts(
        self, id: int = None, categoria_id: int = None, contrapartida_id: int = None
    ) -> List[RelationshipCategoryCounterparts]:
        """Select data in RelacaoCategoriaContrapartidas entity by id or categoria_id or contrapartida_id
        :param  -   id: Id of the register
                -   categoria_id: id Category in Relationship Category Counterparts
                -   contrapartida_id: id Counterparts in Relationship Category Counterparts
        :return -   List with Relationship Category Counterparts selected
        """

        with DBConnectionHandler() as db_connection:
            try:
                query_data = None

                if id and not categoria_id and not contrapartida_id:
                    data = (
                        db_connection.session.query(RelacaoCategoriaContrapartida)
                        .filter_by(id=id)
                        .one()
                    )
                    query_data = [data]

                elif categoria_id and not id and not contrapartida_id:
                    data = (
                        db_connection.session.query(RelacaoCategoriaContrapartida)
                        .filter_by(categoria_id=categoria_id)
                        .all()
                    )
                    query_data = data

                elif contrapartida_id and not id and not categoria_id:
                    data = (
                        db_connection.session.query(RelacaoCategoriaContrapartida)
                        .filter_by(contrapartida_id=contrapartida_id)
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
