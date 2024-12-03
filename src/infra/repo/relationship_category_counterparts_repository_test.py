from faker import Faker
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.constants import REFERENCE_TABLE
from src.infra.entities import RelacaoCategoriaContrapartida
from .relationship_category_counterparts_repository import (
    RelationshipCategoryCounterpartsRepository,
)

faker = Faker()
relationship_category_counterpart_repo = RelationshipCategoryCounterpartsRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_relationship_category_counterpart():
    """Should insert relationship category counterpart"""

    category_id = faker.random_number(digits=5)
    name_category = faker.text(max_nb_chars=120)
    description_category = faker.text(max_nb_chars=500)

    counterpart_id = faker.random_number(digits=5)
    description_counterpart = faker.word()
    example_aplicability = faker.word()
    required = faker.boolean()

    # Insert category counterpart
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                        INSERT INTO {}_categoriacontrapartida (id, nome, descricao)
                        VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE,
                        category_id,
                        name_category,
                        description_category,
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

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
                        description_counterpart,
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

    # SQL Commands
    new_rel_category_counterpart = relationship_category_counterpart_repo.insert_relationship_category_counterparts(
        categoria_id=category_id, contrapartida_id=counterpart_id
    )

    # Select relationship category counterpart
    with engine.begin() as conn:
        try:
            query_counterpart_primary = conn.execute(
                text(
                    "SELECT * FROM {}_relacaocategoriacontrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, new_rel_category_counterpart.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_rel_category_counterpart.id == query_counterpart_primary.id
            assert (
                new_rel_category_counterpart.categoria_id
                == query_counterpart_primary.categoria_id
            )
            assert (
                new_rel_category_counterpart.contrapartida_id
                == query_counterpart_primary.contrapartida_id
            )
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting relationship category counterpart inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_relacaocategoriacontrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, new_rel_category_counterpart.id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting category counterpart inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_categoriacontrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, category_id
                    )
                )
            )
            conn.commit()
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


def test_select_category_counterpart():
    """Shoul select a category counterpart in CategoriaContrapartida table and compare it"""

    category_id = faker.random_number(digits=5)
    name_category = faker.text(max_nb_chars=120)
    description_category = faker.text(max_nb_chars=500)

    counterpart_id = faker.random_number(digits=5)
    description_counterpart = faker.word()
    example_aplicability = faker.word()
    required = faker.boolean()

    relationship_category_counterpart_id = faker.random_number(digits=5)

    data = RelacaoCategoriaContrapartida(
        id=relationship_category_counterpart_id,
        categoria_id=category_id,
        contrapartida_id=counterpart_id,
    )

    # Insert category counterpart
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                        INSERT INTO {}_categoriacontrapartida (id, nome, descricao)
                        VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE,
                        category_id,
                        name_category,
                        description_category,
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

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
                        description_counterpart,
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

    # Insert relationship category counterpart
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                        INSERT INTO {}_relacaocategoriacontrapartida (id, categoria_id,
                        contrapartida_id) VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE,
                        relationship_category_counterpart_id,
                        category_id,
                        counterpart_id,
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_1 = (
        relationship_category_counterpart_repo.select_all_relationship_category_counterparts()
    )
    query_2 = relationship_category_counterpart_repo.select_relationship_category_counterparts(
        id=relationship_category_counterpart_id
    )
    query_3 = relationship_category_counterpart_repo.select_relationship_category_counterparts(
        categoria_id=category_id
    )
    query_4 = relationship_category_counterpart_repo.select_relationship_category_counterparts(
        contrapartida_id=counterpart_id
    )

    assert data in query_1
    assert data in query_2
    assert data in query_3
    assert data in query_4

    # Deleting relationship category counterpart inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_relacaocategoriacontrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, relationship_category_counterpart_id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting category counterpart inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_categoriacontrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, category_id
                    )
                )
            )
            conn.commit()
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
