from faker import Faker
from sqlalchemy import text

from src.constants.reference import REFERENCE_TABLE
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

    # Select investment approach
    with engine.begin() as conn:
        try:
            query_investment_appr = conn.execute(
                text(
                    "SELECT * FROM {}_abordageminvestimento WHERE id='{}';".format(
                        REFERENCE_TABLE, new_investment_approach.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_investment_approach.id == query_investment_appr.id
            assert new_investment_approach.descricao == query_investment_appr.descricao
            assert (
                new_investment_approach.incentivado == query_investment_appr.incentivado
            )
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting investment approach inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_abordageminvestimento WHERE id='{}';".format(
                        REFERENCE_TABLE, new_investment_approach.id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()


def test_select_investment_approach():
    """Should select investment approach"""

    id = faker.random_number(digits=5)
    description = faker.word()
    incentivized = faker.boolean()
    data = AbordagemInvestimento(id=id, descricao=description, incentivado=incentivized)

    # Insert investment approach
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_abordageminvestimento (id, descricao, incentivado)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id, description, incentivized
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_investment_appr = investment_approach.select_all_investment_approach()

    assert data in query_investment_appr

    # Deleting investment approach inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_abordageminvestimento WHERE id='{}';".format(
                        REFERENCE_TABLE, id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()
