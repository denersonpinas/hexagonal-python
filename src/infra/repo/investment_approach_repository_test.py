from faker import Faker
from sqlalchemy import select
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.abordagem_investimento import AbordagemInvestimento
from .investment_approach_repository import InvestmentApproachRepository

faker = Faker()
investment_approach = InvestmentApproachRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_investment_approach():
    """Should insert investment approach"""

    description = faker.word()
    incentivized = faker.boolean()

    # SQL commands
    new_investment_approach = investment_approach.insert_investment_approach(
        descricao=description, incentivado=incentivized
    )

    # Select InvestmentApproach
    query = select(AbordagemInvestimento).where(
        AbordagemInvestimento.id == new_investment_approach.id
    )
    with DBConnectionHandler() as db_connection:
        try:
            for query_investment_appr in db_connection.session.execute(query):
                assert new_investment_approach.id == query_investment_appr[0].id
                assert (
                    new_investment_approach.descricao
                    == query_investment_appr[0].descricao
                )
                assert (
                    new_investment_approach.incentivado
                    == query_investment_appr[0].incentivado
                )

            # Deleting Law Inserted
            investment_approach_inserted = db_connection.session.get(
                AbordagemInvestimento, new_investment_approach.id
            )
            db_connection.session.delete(investment_approach_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_investment_approach():
    """Should select investment approach"""

    description = faker.word()
    incentivized = faker.boolean()
    data = AbordagemInvestimento(descricao=description, incentivado=incentivized)

    # Insert InvestmentApproach
    with DBConnectionHandler() as db_connection:
        try:
            # Add InvestmentApproach for test
            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_investment_appr = investment_approach.select_all_investment_approach()
            assert data in query_investment_appr

            # Deleting InvestmentApproach Inserted
            investment_appr_inserted = db_connection.session.get(
                AbordagemInvestimento, data.id
            )
            db_connection.session.delete(investment_appr_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
