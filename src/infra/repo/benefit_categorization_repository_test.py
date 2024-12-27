import uuid
from faker import Faker
from sqlalchemy import select
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import CategorizacaoBeneficiario, TipoCategorizacaoBeneficiario
from src.infra.repo import BenefitCategorizationRepository

faker = Faker()
categorization = BenefitCategorizationRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_categorization():
    """Should insert insert_categorization"""

    valor = faker.text(max_nb_chars=64)

    id = str(uuid.uuid4().hex)
    description_categorization_type = faker.text(max_nb_chars=50)
    info = faker.text(max_nb_chars=150)

    categorization_type = TipoCategorizacaoBeneficiario(
        id=id, descricao=description_categorization_type, info=info
    )

    # Insert Categorization
    with DBConnectionHandler() as db_connection:
        try:
            # Add Categorization for test
            db_connection.session.add(categorization_type)
            db_connection.session.flush()
            db_connection.session.commit()

            # SQL commands
            new_categorization = categorization.insert_categorization(
                valor=valor, tipo_id=categorization_type.id
            )

            # Select Categorization
            query = select(CategorizacaoBeneficiario).where(
                CategorizacaoBeneficiario.id == new_categorization.id
            )

            for query_categorization in db_connection.session.execute(query):
                assert new_categorization.id == query_categorization[0].id
                assert new_categorization.valor == query_categorization[0].valor
                assert new_categorization.tipo_id == query_categorization[0].tipo_id

            # Deleting Categorization Inserted
            type_caracterization_inserted = db_connection.session.get(
                TipoCategorizacaoBeneficiario, categorization_type.id
            )
            caracterization_inserted = db_connection.session.get(
                CategorizacaoBeneficiario, new_categorization.id
            )
            db_connection.session.delete(caracterization_inserted)
            db_connection.session.delete(type_caracterization_inserted)
            db_connection.session.flush()
            db_connection.session.commit()

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_categorization():
    """Should select all categorization"""

    valor = faker.text(max_nb_chars=64)

    id = str(uuid.uuid4().hex)
    description_categorization_type = faker.text(max_nb_chars=50)
    info = faker.text(max_nb_chars=150)
    categorization_type = TipoCategorizacaoBeneficiario(
        id=id, descricao=description_categorization_type, info=info
    )

    # Insert Categorization
    with DBConnectionHandler() as db_connection:
        try:
            # Add Categorization for test
            db_connection.session.add(categorization_type)

            data = CategorizacaoBeneficiario(
                valor=valor, tipo_id=categorization_type.id
            )

            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_categorization_1 = categorization.select_all_categorizations()
            query_categorization_2 = categorization.select_categorization(id=data.id)
            query_categorization_3 = categorization.select_categorization(
                tipo_id=categorization_type.id
            )

            assert data in query_categorization_1
            assert data in query_categorization_2
            assert data in query_categorization_3

            # Deleting Categorization Inserted
            type_caracterization_inserted = db_connection.session.get(
                TipoCategorizacaoBeneficiario, categorization_type.id
            )
            caracterization_inserted = db_connection.session.get(
                CategorizacaoBeneficiario, data.id
            )
            db_connection.session.delete(caracterization_inserted)
            db_connection.session.delete(type_caracterization_inserted)
            db_connection.session.flush()
            db_connection.session.commit()

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
