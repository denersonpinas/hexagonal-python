from faker import Faker
from sqlalchemy import select
from src.infra.config import DBConnectionHandler
from src.infra.entities import Contrapartida
from .counterpart_repository import CounterpartRepository

faker = Faker()
counterpart_repository = CounterpartRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_counterpart():
    """Should insert Counterpart"""

    description = faker.word()
    exaple_aplicability = faker.word()
    requirement = faker.boolean()

    # SQL Commands
    new_counterpart = counterpart_repository.insert_counterpart(
        descricao=description,
        exemplo_aplicabilidade=exaple_aplicability,
        obrigatoria=requirement,
    )

    # Select Counterpart
    query = select(Contrapartida).where(Contrapartida.id == new_counterpart.id)
    with DBConnectionHandler() as db_connection:
        try:
            for query_counterpart in db_connection.session.execute(query):
                assert new_counterpart.id == query_counterpart[0].id
                assert new_counterpart.descricao == query_counterpart[0].descricao
                assert (
                    new_counterpart.exemplo_aplicabilidade
                    == query_counterpart[0].exemplo_aplicabilidade
                )
                assert new_counterpart.obrigatoria == query_counterpart[0].obrigatoria
                assert new_counterpart.padrao == query_counterpart[0].padrao

            # Deleting Counterpart Inserted
            counterpart_inserted = db_connection.session.get(
                Contrapartida, new_counterpart.id
            )
            db_connection.session.delete(counterpart_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_counterpart():
    """Shoul select a counterpart in Counterpart table and compare it"""

    description = faker.word()
    example_aplicability = faker.word()
    required = faker.boolean()
    data = Contrapartida(
        descricao=description,
        exemplo_aplicabilidade=example_aplicability,
        obrigatoria=required,
        padrao=True,
    )

    # Insert Counterpart
    with DBConnectionHandler() as db_connection:
        try:
            # Add Counterpart for test
            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_counterpart1 = counterpart_repository.select_counterpart(
                counterpart_id=data.id
            )
            query_counterpart2 = counterpart_repository.select_counterpart(
                required=required
            )
            query_counterpart3 = counterpart_repository.select_counterpart(default=True)
            query_counterpart4 = counterpart_repository.select_counterpart(
                counterpart_id=data.id, required=required
            )
            query_counterpart5 = counterpart_repository.select_counterpart(
                required=required, default=True
            )
            query_counterpart6 = counterpart_repository.select_counterpart(
                counterpart_id=data.id, required=required, default=True
            )
            query_counterpart7 = counterpart_repository.select_all_counterpart()

            assert data in query_counterpart1
            assert data in query_counterpart2
            assert data in query_counterpart3
            assert data in query_counterpart4
            assert data in query_counterpart5
            assert data in query_counterpart6
            assert data in query_counterpart7

            # Deleting Counterpart Inserted
            counterpart_inserted = db_connection.session.get(Contrapartida, data.id)
            db_connection.session.delete(counterpart_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
