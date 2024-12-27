from typing import List
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import CategoryCounterpartRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import CategoryCounterpart
from src.infra.entities import CategoriaContrapartida


class CategoryCounterpartRepository(CategoryCounterpartRepositoryInterface):
    """Class to manage CategoryCounterpart Repository"""

    @classmethod
    def insert_category_counterpart(
        cls, nome: str, descricao: str, subcategoria_de_id: int = None
    ) -> CategoryCounterpart:
        """Insert data in category counterpart entity
        :param  -   nome: category counterpart name
                -   descricao: category counterpart description
                -   subcategoria_de_id: id subcategory of the category counterpart
        :return -   tuple with category counterpart inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_category_counterpart = CategoriaContrapartida(
                    nome=nome,
                    descricao=descricao,
                    subcategoria_de_id=subcategoria_de_id,
                )
                db_connection.session.add(new_category_counterpart)
                db_connection.session.flush()
                db_connection.session.commit()

                return CategoryCounterpart(
                    id=new_category_counterpart.id,
                    nome=new_category_counterpart.nome,
                    descricao=new_category_counterpart.descricao,
                    subcategoria_de_id=new_category_counterpart.subcategoria_de_id,
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
                query = select(CategoriaContrapartida).options(
                    joinedload(CategoriaContrapartida.subcategoria_de)
                )
                return db_connection.session.scalars(query).all()
            except NoResultFound:
                return []
            except Exception as e:
                db_connection.session.rollback()
                raise e

    @classmethod
    def select_category_counterpart(
        cls, category_counterpart_id: int = None, subcategoria_de_id: int = None
    ) -> List[CategoryCounterpart]:
        """Select data in category counterpart entity by id and/or subcategoria_de_id"""
        with DBConnectionHandler() as db_connection:
            try:
                query = select(CategoriaContrapartida)

                if category_counterpart_id and subcategoria_de_id:
                    query = query.where(
                        CategoriaContrapartida.id == category_counterpart_id,
                        CategoriaContrapartida.subcategoria_de_id == subcategoria_de_id,
                    )
                elif category_counterpart_id:
                    query = query.where(
                        CategoriaContrapartida.id == category_counterpart_id
                    )
                elif subcategoria_de_id:
                    query = query.where(
                        CategoriaContrapartida.subcategoria_de_id == subcategoria_de_id
                    )

                result = db_connection.session.execute(query).scalars().all()

                for obj in result:
                    db_connection.session.expunge(obj)
                return list(result)
            except NoResultFound:
                return []
            except Exception as e:
                db_connection.session.rollback()
                raise e
