import uuid
from faker import Faker
from sqlalchemy import select
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import TipoCategorizacaoBeneficiario
from src.infra.repo import BenefitCategorizationTypeRepository

faker = Faker()
categorization_type = BenefitCategorizationTypeRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_categorization_type():
    """Should insert CategorizationType"""

    id = str(uuid.uuid4().hex)
    description = faker.text(max_nb_chars=50)
    info = faker.text(max_nb_chars=150)

    # SQL commands
    new_categorization_type = categorization_type.insert_categorization_type(
        id=id, info=info, descricao=description
    )

    # Select CategorizationType
    query = select(TipoCategorizacaoBeneficiario).where(
        TipoCategorizacaoBeneficiario.id == new_categorization_type.id
    )
    with DBConnectionHandler() as db_connection:
        try:
            for query_categorization_type in db_connection.session.execute(query):
                assert new_categorization_type.id == query_categorization_type[0].id
                assert new_categorization_type.info == query_categorization_type[0].info
                assert (
                    new_categorization_type.descricao
                    == query_categorization_type[0].descricao
                )

            # Deleting CategorizationType Inserted
            categorization_type_inserted = db_connection.session.get(
                TipoCategorizacaoBeneficiario, new_categorization_type.id
            )
            db_connection.session.delete(categorization_type_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_all_categorization_type():
    """Should select all categorization_type"""

    id = str(uuid.uuid4().hex)
    description = faker.text(max_nb_chars=50)
    info = faker.text(max_nb_chars=150)
    data = TipoCategorizacaoBeneficiario(id=id, info=info, descricao=description)

    # Insert CategorizationType
    with DBConnectionHandler() as db_connection:
        try:
            # Add CategorizationType for test
            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_categorization_type_1 = (
                categorization_type.select_all_categorization_types()
            )
            query_categorization_type_2 = (
                categorization_type.select_categorization_type(id=data.id)
            )

            assert data in query_categorization_type_1
            assert data in query_categorization_type_2

            # Deleting CategorizationType Inserted
            categorization_type_inserted = db_connection.session.get(
                TipoCategorizacaoBeneficiario, data.id
            )
            db_connection.session.delete(categorization_type_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
