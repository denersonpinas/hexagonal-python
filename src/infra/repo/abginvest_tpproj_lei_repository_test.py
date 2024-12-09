from faker import Faker
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.constants import REFERENCE_TABLE
from src.infra.entities import AbginvestTpprojLei
from .abginvest_tpproj_lei_repository import AbginvestTpprojLeiRepository

faker = Faker()
abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_abginvest_tpproj_lei():
    """Should insert abginvest tpproj lei"""

    id = faker.random_number(digits=5)
    description = faker.word()
    incentivized = faker.boolean()

    id_law = faker.random_number(digits=5)
    name = faker.text(max_nb_chars=100)
    description_law = faker.text(max_nb_chars=250)

    id_project = faker.random_number(digits=5)
    name_project = faker.text(max_nb_chars=100)
    description_project = faker.text(max_nb_chars=250)

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

    # Insert law
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_lei (id, nome, descricao)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id_law, name, description_law
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Insert type_project
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_tipoprojeto (id, nome, descricao)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id_project, name_project, description_project
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

    new_abginvest_tpproj = abginvest_tpproj_lei_repo.insert_abginvest_tpproj_lei(
        abordagem_investimento_id=id, lei_id=id_law, tipo_pojeto_id=id_project
    )

    # Select type_project
    with engine.begin() as conn:
        try:
            query_type_project = conn.execute(
                text(
                    "SELECT * FROM {}_abginvest_tpproj_lei WHERE id='{}';".format(
                        REFERENCE_TABLE, new_abginvest_tpproj.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_abginvest_tpproj.id == query_type_project.id
            assert (
                new_abginvest_tpproj.abordagem_investimento_id
                == query_type_project.abordagem_investimento_id
            )
            assert new_abginvest_tpproj.lei_id == query_type_project.lei_id
            assert (
                new_abginvest_tpproj.tipo_pojeto_id == query_type_project.tipo_pojeto_id
            )
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting abginvest_tpproj_lei inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_abginvest_tpproj_lei WHERE id='{}';".format(
                        REFERENCE_TABLE, new_abginvest_tpproj.id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting investment_approach inserted with test
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

    # Deleting law inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_lei WHERE id='{}';".format(REFERENCE_TABLE, id_law)
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting type_project inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_tipoprojeto WHERE id='{}';".format(
                        REFERENCE_TABLE, id_project
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()


def test_select_abginvest_tpproj_lei():
    """Shoul select a abginvest tpproj lei in AbginvestTpprojLei table and compare it"""

    id_aprooach = faker.random_number(digits=5)
    description = faker.word()
    incentivized = faker.boolean()

    id_law = faker.random_number(digits=5)
    name = faker.text(max_nb_chars=100)
    description_law = faker.text(max_nb_chars=250)

    id_project = faker.random_number(digits=5)
    name_project = faker.text(max_nb_chars=100)
    description_project = faker.text(max_nb_chars=250)

    abginvest_id = faker.random_number(digits=5)

    # Insert investment approach
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_abordageminvestimento (id, descricao, incentivado)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id_aprooach, description, incentivized
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Insert law
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_lei (id, nome, descricao)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id_law, name, description_law
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Insert type_project
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                    INSERT INTO {}_tipoprojeto (id, nome, descricao)
                    VALUES ('{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, id_project, name_project, description_project
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

    data = AbginvestTpprojLei(
        id=abginvest_id,
        abordagem_investimento_id=id_aprooach,
        lei_id=id_law,
        tipo_pojeto_id=id_project,
    )

    # Insert AbginvestTpprojLei
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                        INSERT INTO {}_abginvest_tpproj_lei (id, abordagem_investimento_id, lei_id, tipo_pojeto_id)
                        VALUES ('{}', '{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE, abginvest_id, id_aprooach, id_law, id_project
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_counterpart1 = abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
        id=abginvest_id
    )
    query_counterpart2 = abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
        abordagem_investimento_id=id_aprooach
    )
    query_counterpart3 = abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
        lei_id=id_law
    )
    query_counterpart4 = abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
        tipo_pojeto_id=id_project
    )
    query_counterpart5 = abginvest_tpproj_lei_repo.select_all_abginvest_tpproj_lei()

    assert data in query_counterpart1
    assert data in query_counterpart2
    assert data in query_counterpart3
    assert data in query_counterpart4
    assert data in query_counterpart5

    # Deleting abginvest_tpproj_lei inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_abginvest_tpproj_lei WHERE id='{}';".format(
                        REFERENCE_TABLE, abginvest_id
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting investment_approach inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_abordageminvestimento WHERE id='{}';".format(
                        REFERENCE_TABLE, id_aprooach
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting law inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_lei WHERE id='{}';".format(REFERENCE_TABLE, id_law)
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting type_project inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_tipoprojeto WHERE id='{}';".format(
                        REFERENCE_TABLE, id_project
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()
