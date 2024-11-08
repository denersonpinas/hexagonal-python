from faker import Faker
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.constants import REFERENCE_TABLE
from .counterpart_repository import CounterpartRepository

faker = Faker()
counterpart_repository = CounterpartRepository()
db_connection_handler = DBConnectionHandler()

def test_insert_counterpart():
    '''Should insert counterpart'''

    description = faker.word()
    exaple_aplicability = faker.word()
    requirement= faker.boolean()
    engine = db_connection_handler.get_engine()

    # SQL Commands
    new_counterpart = counterpart_repository.insert_counterparts(descricao=description, exemplo_aplicabilidade=exaple_aplicability, obrigatoria=requirement)

    # Select counterpart
    with engine.begin() as conn:
        try:
            query_counterpart = conn.execute(
                text("SELECT * FROM {}_contrapartida WHERE id='{}';".format(REFERENCE_TABLE, new_counterpart.id))
            ).fetchone()
            conn.commit()

            assert new_counterpart.id == query_counterpart.id
            assert new_counterpart.descricao == query_counterpart.descricao
            assert new_counterpart.exemplo_aplicabilidade == query_counterpart.exemplo_aplicabilidade
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
            query_counterpart = conn.execute(
                text("DELETE FROM {}_contrapartida WHERE id='{}';".format(REFERENCE_TABLE, new_counterpart.id))
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

