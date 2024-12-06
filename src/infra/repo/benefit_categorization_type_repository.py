from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import BenefitCategorizationTypeRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import BenefitCategorizationType
from src.infra.entities import TipoCategorizacaoBeneficiario


class BenefitCategorizationTypeRepository(BenefitCategorizationTypeRepositoryInterface):
    """Class to manage Benefit Categorization Type Repository"""

    @classmethod
    def insert_categorization_type(
        cls, id: str, descricao: str, info: str
    ) -> BenefitCategorizationType:
        """Insert data in Benefit Categorization Type entity
        :param  -   descricao: Description of the categorization type
                    info: Additional information
        :return -   BenefitCategorizationType object
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_type = TipoCategorizacaoBeneficiario(
                    id=id, descricao=descricao, info=info
                )
                db_connection.session.add(new_type)
                db_connection.session.commit()

                return BenefitCategorizationType(
                    id=new_type.id, descricao=new_type.descricao, info=new_type.info
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_categorization_type(
        cls, id: str = None
    ) -> List[BenefitCategorizationType]:
        """Select data in Benefit Categorization Type entity by id
        :param  -   id: id of the register
        :return -   List with BenefitCategorizationType selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                query_data = None

                if id:
                    data = (
                        db_connection.session.query(TipoCategorizacaoBeneficiario)
                        .filter_by(id=id)
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

    @classmethod
    def select_all_categorization_types(cls) -> List[BenefitCategorizationType]:
        """Select all data in Benefit Categorization Type entity
        :return -   List with all BenefitCategorizationType
        """
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.query(TipoCategorizacaoBeneficiario).all()
                return data
            except NoResultFound:
                return []
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
