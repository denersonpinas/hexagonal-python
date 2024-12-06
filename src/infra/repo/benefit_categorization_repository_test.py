from uuid import uuid4
from faker import Faker
from sqlalchemy import text

from src.constants.reference import REFERENCE_TABLE
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import CategorizacaoBeneficiario
from src.infra.repo import BenefitCategorizationRepository

faker = Faker()
categorization_type = BenefitCategorizationRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_categorization():
    """Should insert insert_categorization"""

    valor = faker.text(max_nb_chars=64)

    id_categorization_type = str(uuid4().hex)
    description_categorization_type = faker.text(max_nb_chars=50)
    info = faker.text(max_nb_chars=150)

    # Insert categorization_type
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_tipocategorizacaobeneficiario (id, descricao, info)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE,
                        id_categorization_type,
                        description_categorization_type,
                        info,
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # SQL commands
    new_categorization = categorization_type.insert_categorization(
        valor=valor, tipo_id=id_categorization_type
    )

    # Select categorization_type
    with engine.begin() as conn:
        try:
            query_categorization = conn.execute(
                text(
                    "SELECT * FROM {}_categorizacaobeneficiario WHERE id='{}';".format(
                        REFERENCE_TABLE, new_categorization.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_categorization.id == query_categorization.id
            assert new_categorization.valor == query_categorization.valor
            assert new_categorization.tipo_id == query_categorization.tipo_id
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting categorizacaobeneficiario inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_categorizacaobeneficiario WHERE id='{}';".format(
                        REFERENCE_TABLE, new_categorization.id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting tipocategorizacaobeneficiario inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_tipocategorizacaobeneficiario WHERE id='{}';".format(
                        REFERENCE_TABLE, id_categorization_type
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()


def test_select_categorization():
    """Should select all categorization"""

    id = faker.random_number(digits=5)
    valor = faker.text(max_nb_chars=64)

    id_categorization_type = str(uuid4().hex)
    description_categorization_type = faker.text(max_nb_chars=50)
    info = faker.text(max_nb_chars=150)
    data = CategorizacaoBeneficiario(id=id, valor=valor, tipo_id=id_categorization_type)

    # Insert categorization_type
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_tipocategorizacaobeneficiario (id, descricao, info)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE,
                        id_categorization_type,
                        description_categorization_type,
                        info,
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Insert categorization_type
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_categorizacaobeneficiario (id, valor, tipo_id)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id, valor, id_categorization_type
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_categorization_1 = categorization_type.select_all_categorizations()
    query_categorization_2 = categorization_type.select_categorization(id=id)
    query_categorization_3 = categorization_type.select_categorization(
        tipo_id=id_categorization_type
    )

    assert data in query_categorization_1
    assert data in query_categorization_2
    assert data in query_categorization_3

    # Deleting categorizacaobeneficiario inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_categorizacaobeneficiario WHERE id='{}';".format(
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

    # Deleting tipocategorizacaobeneficiario inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_tipocategorizacaobeneficiario WHERE id='{}';".format(
                        REFERENCE_TABLE, id_categorization_type
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()
