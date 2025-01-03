from typing import List
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import BenefitCategorizationRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import BenefitCategorization
from src.infra.entities import CategorizacaoBeneficiario


class BenefitCategorizationRepository(BenefitCategorizationRepositoryInterface):
    """Class to manage Benefit Categorization Repository"""

    @classmethod
    def insert_categorization(cls, valor: str, tipo_id: str) -> BenefitCategorization:
        """Insert data in Benefit Categorization entity
        :param  -   valor: Value of the categorization
                    tipo_id: ID of the categorization type
        :return -   BenefitCategorization object
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_categorization = CategorizacaoBeneficiario(
                    valor=valor, tipo_id=tipo_id
                )
                db_connection.session.add(new_categorization)
                db_connection.session.flush()
                db_connection.session.commit()

                return BenefitCategorization(
                    id=new_categorization.id,
                    valor=new_categorization.valor,
                    tipo_id=new_categorization.tipo_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_categorization(
        cls, id: int = None, tipo_id: int = None
    ) -> List[BenefitCategorization]:
        """Select data in Benefit Categorization entity by id
        :param  -   id: id of the register
                -   tipo_id: id TypeBenefitCategorization of the relationship register
        :return -   List with BenefitCategorization selected
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = None

                if id and not tipo_id:
                    query = (
                        select(CategorizacaoBeneficiario)
                        .where(CategorizacaoBeneficiario.id == id)
                        .options(
                            joinedload(
                                CategorizacaoBeneficiario.tipo_categorizacao_beneficiario
                            )
                        )
                    )

                elif tipo_id and not id:
                    query = (
                        select(CategorizacaoBeneficiario)
                        .where(CategorizacaoBeneficiario.tipo_id == tipo_id)
                        .options(
                            joinedload(
                                CategorizacaoBeneficiario.tipo_categorizacao_beneficiario
                            )
                        )
                    )

                response: List[BenefitCategorization] = []
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

    @classmethod
    def select_all_categorizations(cls) -> List[BenefitCategorization]:
        """Select all data in Benefit Categorization entity
        :return -   List with all BenefitCategorization
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = select(CategorizacaoBeneficiario).options(
                    joinedload(
                        CategorizacaoBeneficiario.tipo_categorizacao_beneficiario
                    )
                )
                response: List[BenefitCategorization] = []
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
