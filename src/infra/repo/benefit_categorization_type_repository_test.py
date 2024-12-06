import uuid
from faker import Faker
from sqlalchemy import text

from src.constants.reference import REFERENCE_TABLE
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import TipoCategorizacaoBeneficiario
from src.infra.repo import BenefitCategorizationTypeRepository

faker = Faker()
categorization_type = BenefitCategorizationTypeRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_categorization_type():
    """Should insert insert_categorization_type"""

    id = str(uuid.uuid4().hex)
    description = faker.text(max_nb_chars=50)
    info = faker.text(max_nb_chars=150)

    # SQL commands
    new_categorization_type = categorization_type.insert_categorization_type(
        id=id, info=info, descricao=description
    )

    # Select categorization_type
    with engine.begin() as conn:
        try:
            query_categorization_type = conn.execute(
                text(
                    "SELECT * FROM {}_tipocategorizacaobeneficiario WHERE id='{}';".format(
                        REFERENCE_TABLE, new_categorization_type.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_categorization_type.id == query_categorization_type.id
            assert new_categorization_type.info == query_categorization_type.info
            assert (
                new_categorization_type.descricao == query_categorization_type.descricao
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
                    "DELETE FROM {}_tipocategorizacaobeneficiario WHERE id='{}';".format(
                        REFERENCE_TABLE, new_categorization_type.id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()


def test_select_all_categorization_type():
    """Should select all categorization_type"""

    id = str(uuid.uuid4().hex)
    description = faker.text(max_nb_chars=50)
    info = faker.text(max_nb_chars=150)
    data = TipoCategorizacaoBeneficiario(id=id, info=info, descricao=description)

    # Insert categorization_type
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_tipocategorizacaobeneficiario (id, descricao, info)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id, description, info
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_categorization_type_1 = categorization_type.select_all_categorization_types()
    query_categorization_type_2 = categorization_type.select_categorization_type(id=id)

    assert data in query_categorization_type_1
    assert data in query_categorization_type_2

    # Deleting investment approach inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_tipocategorizacaobeneficiario WHERE id='{}';".format(
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
