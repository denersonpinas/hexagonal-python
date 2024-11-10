from faker import Faker
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.constants import REFERENCE_TABLE
from src.infra.entities import Contrapartida
from .counterpart_repository import CounterpartRepository

faker = Faker()
counterpart_repository = CounterpartRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_counterpart():
    """Should insert counterpart"""

    description = faker.word()
    exaple_aplicability = faker.word()
    requirement = faker.boolean()

    # SQL Commands
    new_counterpart = counterpart_repository.insert_counterpart(
        descricao=description,
        exemplo_aplicabilidade=exaple_aplicability,
        obrigatoria=requirement,
    )

    # Select counterpart
    with engine.begin() as conn:
        try:
            query_counterpart = conn.execute(
                text(
                    "SELECT * FROM {}_contrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, new_counterpart.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_counterpart.id == query_counterpart.id
            assert new_counterpart.descricao == query_counterpart.descricao
            assert (
                new_counterpart.exemplo_aplicabilidade
                == query_counterpart.exemplo_aplicabilidade
            )
            assert new_counterpart.obrigatoria == query_counterpart.obrigatoria
            assert new_counterpart.padrao == query_counterpart.padrao
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting counterpart inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_contrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, new_counterpart.id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()


def test_select_counterpart():
    """Shoul select a counterpart in Counterpart table and compare it"""

    counterpart_id = faker.random_number(digits=5)
    description = faker.word()
    example_aplicability = faker.word()
    required = faker.boolean()
    data = Contrapartida(
        id=counterpart_id,
        descricao=description,
        exemplo_aplicabilidade=example_aplicability,
        obrigatoria=required,
        padrao=True,
    )

    # Insert counterpart
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                        INSERT INTO {}_contrapartida (id, descricao,
                        exemplo_aplicabilidade, obrigatoria,
                        padrao) VALUES ('{}', '{}', '{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE,
                        counterpart_id,
                        description,
                        example_aplicability,
                        required,
                        True,
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_counterpart1 = counterpart_repository.select_counterpart(
        counterpart_id=counterpart_id
    )
    query_counterpart2 = counterpart_repository.select_counterpart(required=required)
    query_counterpart3 = counterpart_repository.select_counterpart(default=True)
    query_counterpart4 = counterpart_repository.select_counterpart(
        counterpart_id=counterpart_id, required=required
    )
    query_counterpart5 = counterpart_repository.select_counterpart(
        required=required, default=True
    )
    query_counterpart6 = counterpart_repository.select_counterpart(
        counterpart_id=counterpart_id, required=required, default=True
    )

    assert data in query_counterpart1
    assert data in query_counterpart2
    assert data in query_counterpart3
    assert data in query_counterpart4
    assert data in query_counterpart5
    assert data in query_counterpart6

    # Deleting counterpart inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_contrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, counterpart_id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()
