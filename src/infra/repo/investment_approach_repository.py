from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import (
    InvestmentApproachRepositoryInterface,
)
from src.infra.config import DBConnectionHandler
from src.domain.models import InvestmentApproach
from src.infra.entities.abordagem_investimento import AbordagemInvestimento


class InvestmentApproachRepository(InvestmentApproachRepositoryInterface):
    """Class to manage Investment Approach Repository"""

    @classmethod
    def insert_investment_approach(
        cls, descricao: str, incentivado: bool
    ) -> InvestmentApproach:
        """Insert data in investment approach entity
        :param  -   descricao: investment approach description
                -   incentivado: if investment approach is incentivized
        :return -   tuple with investment approach inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_investment_approach = AbordagemInvestimento(
                    descricao=descricao, incentivado=incentivado
                )
                db_connection.session.add(new_investment_approach)
                db_connection.session.commit()

                return InvestmentApproach(
                    id=new_investment_approach.id,
                    descricao=new_investment_approach.descricao,
                    incentivado=new_investment_approach.incentivado,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_all_investment_approach(cls) -> List[InvestmentApproach]:
        """Select all data in investment approach entity
        :param  -   is None
        :return -   List with all Investment Approach
        """

        with DBConnectionHandler() as db_connection:
            try:
                query_data = []

                data = db_connection.session.query(AbordagemInvestimento).all()
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
