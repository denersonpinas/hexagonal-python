from faker import Faker
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.constants import REFERENCE_TABLE
from src.infra.entities import CategoriaContrapartida
from .category_counterpart_repository import CategoryCounterpartRepository

faker = Faker()
category_counterpart_repo = CategoryCounterpartRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_category_counterpart():
    """Should insert category counterpart"""

    name_primary = faker.text(max_nb_chars=120)
    description_primary = faker.text(max_nb_chars=500)

    name_secundary = faker.text(max_nb_chars=120)
    description_secundary = faker.text(max_nb_chars=500)

    # SQL Commands
    new_counterpart_primary = category_counterpart_repo.insert_category_counterpart(
        nome=name_primary, descricao=description_primary
    )

    new_counterpart_secundary = category_counterpart_repo.insert_category_counterpart(
        nome=name_secundary,
        descricao=description_secundary,
        subcategoria_id=new_counterpart_primary.id,
    )

    # Select category counterpart
    with engine.begin() as conn:
        try:
            query_counterpart_primary = conn.execute(
                text(
                    "SELECT * FROM {}_categoriacontrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, new_counterpart_primary.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_counterpart_primary.id == query_counterpart_primary.id
            assert new_counterpart_primary.nome == query_counterpart_primary.nome
            assert (
                new_counterpart_primary.descricao == query_counterpart_primary.descricao
            )
            assert (
                new_counterpart_primary.subcategoria_id
                == query_counterpart_primary.subcategoria_id
            )
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Select subcategory of the category counterpart
    with engine.begin() as conn:
        try:
            query_counterpart_secundary = conn.execute(
                text(
                    "SELECT * FROM {}_categoriacontrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, new_counterpart_secundary.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_counterpart_secundary.id == query_counterpart_secundary.id
            assert new_counterpart_secundary.nome == query_counterpart_secundary.nome
            assert (
                new_counterpart_secundary.descricao
                == query_counterpart_secundary.descricao
            )
            assert (
                new_counterpart_secundary.subcategoria_id
                == query_counterpart_secundary.subcategoria_id
            )
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting subcategory of the category counterpart inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_categoriacontrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, new_counterpart_secundary.id
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
                        REFERENCE_TABLE, new_counterpart_primary.id
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

    category_counterpart_id_primary = faker.random_number(digits=5)
    name_primary = faker.text(max_nb_chars=120)
    description_primary = faker.text(max_nb_chars=500)

    data_primary = CategoriaContrapartida(
        id=category_counterpart_id_primary,
        nome=name_primary,
        descricao=description_primary,
    )

    category_counterpart_id_secundary = faker.random_number(digits=5)
    name_secundary = faker.text(max_nb_chars=120)
    description_secundary = faker.text(max_nb_chars=500)

    data_secundary = CategoriaContrapartida(
        id=category_counterpart_id_secundary,
        nome=name_secundary,
        descricao=description_secundary,
        subcategoria_id=category_counterpart_id_primary,
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
                        category_counterpart_id_primary,
                        name_primary,
                        description_primary,
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Insert subcategory of the category counterpart
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                        INSERT INTO {}_categoriacontrapartida (id, nome, descricao,
                        subcategoria_id)
                        VALUES ('{}', '{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE,
                        category_counterpart_id_secundary,
                        name_secundary,
                        description_secundary,
                        category_counterpart_id_primary,
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_counterpart1 = category_counterpart_repo.select_category_counterpart(
        category_counterpart_id=category_counterpart_id_secundary,
        subcategoria_id=category_counterpart_id_primary,
    )
    query_counterpart2 = category_counterpart_repo.select_category_counterpart(
        category_counterpart_id=category_counterpart_id_primary
    )
    query_counterpart3 = category_counterpart_repo.select_category_counterpart(
        subcategoria_id=category_counterpart_id_primary
    )
    query_counterpart4 = category_counterpart_repo.select_all_category_counterpart()

    assert data_secundary in query_counterpart1
    assert data_primary in query_counterpart2
    assert data_secundary in query_counterpart3
    assert data_primary in query_counterpart4

    # Deleting subcategory of the category counterpart inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_categoriacontrapartida WHERE id='{}';".format(
                        REFERENCE_TABLE, category_counterpart_id_secundary
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
                        REFERENCE_TABLE, category_counterpart_id_primary
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()
