from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import CategoryCounterpartRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import CategoryCounterpart
from src.infra.entities import CategoriaContrapartida


class CategoryCounterpartRepository(CategoryCounterpartRepositoryInterface):
    """Class to manage CategoryCounterpart Repository"""

    @classmethod
    def insert_category_counterpart(
        cls, nome: str, descricao: str, subcategoria_id: int = None
    ) -> CategoryCounterpart:
        """Insert data in category counterpart entity
        :param  -   nome: category counterpart name
                -   descricao: category counterpart description
                -   subcategoria_id: id subcategory of the category counterpart
        :return -   tuple with category counterpart inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_category_counterpart = CategoriaContrapartida(
                    nome=nome, descricao=descricao, subcategoria_id=subcategoria_id
                )
                db_connection.session.add(new_category_counterpart)
                db_connection.session.commit()

                return CategoryCounterpart(
                    id=new_category_counterpart.id,
                    nome=new_category_counterpart.nome,
                    descricao=new_category_counterpart.descricao,
                    subcategoria_id=new_category_counterpart.subcategoria_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_all_category_counterpart(cls) -> List[CategoryCounterpart]:
        """Select all data in CategoryCounterpart entity
        :param  -   is None
        :return -   List with all CategoryCounterpart
        """

        with DBConnectionHandler() as db_connection:
            try:
                query_data = []

                data = db_connection.session.query(CategoriaContrapartida).all()
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
    def select_category_counterpart(
        cls, category_counterpart_id: int = None, subcategoria_id: int = None
    ) -> List[CategoryCounterpart]:
        """Select data in category counterpart entity by id and/or subcategoria_id
        :param  -   category_counterpart_id: Id of the registry
                -   subcategoria_id: Id subcategory of the registry
        :return -   List with Category Counterpart selected
        """

        with DBConnectionHandler() as db_connection:
            try:
                query_data = None

                if category_counterpart_id and subcategoria_id:
                    data = (
                        db_connection.session.query(CategoriaContrapartida)
                        .filter_by(
                            id=category_counterpart_id, subcategoria_id=subcategoria_id
                        )
                        .one()
                    )
                    query_data = [data]

                elif not category_counterpart_id and subcategoria_id:
                    data = (
                        db_connection.session.query(CategoriaContrapartida)
                        .filter_by(subcategoria_id=subcategoria_id)
                        .all()
                    )

                    query_data = data

                elif category_counterpart_id and not subcategoria_id:
                    data = (
                        db_connection.session.query(CategoriaContrapartida)
                        .filter_by(id=category_counterpart_id)
                        .one()
                    )
                    query_data = [data]

                return query_data
            except NoResultFound:
                return []
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None
