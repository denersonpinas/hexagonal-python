from faker import Faker
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from src.constants import REFERENCE_TABLE
from src.infra.entities import AbginvestTpprojLeiContrpart
from src.infra.repo import AbginvestTpprojLeiContrpartRepository

faker = Faker()
abginvest_tpproj_lei_contpart_repo = AbginvestTpprojLeiContrpartRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_abginvest_tpproj_lei_contrpart():
    """Should insert abginvest tpproj lei"""

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

    category_id = faker.random_number(digits=5)
    name_category = faker.text(max_nb_chars=120)
    description_category = faker.text(max_nb_chars=500)

    counterpart_id = faker.random_number(digits=5)
    description_counterpart = faker.word()
    example_aplicability = faker.word()
    required = faker.boolean()

    relationship_category_counterpart_id = faker.random_number(digits=5)

    order = faker.random_number(digits=5)

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

    # SQL commands
    new_abginvest_tpproj_contrpart = (
        abginvest_tpproj_lei_contpart_repo.insert_abginvest_tpproj_lei_contrpart(
            ordem=order,
            id_relacao_contrapartida_categoria=relationship_category_counterpart_id,
            id_abginvest_tpproj_lei=abginvest_id,
        )
    )

    # Select type_project
    with engine.begin() as conn:
        try:
            query_type_project = conn.execute(
                text(
                    "SELECT * FROM {}_abginvest_tpproj_lei_contrpart WHERE id='{}';".format(
                        REFERENCE_TABLE, new_abginvest_tpproj_contrpart.id
                    )
                )
            ).fetchone()
            conn.commit()

            assert new_abginvest_tpproj_contrpart.id == query_type_project.id
            assert new_abginvest_tpproj_contrpart.ordem == query_type_project.ordem
            assert (
                new_abginvest_tpproj_contrpart.id_relacao_contrapartida_categoria
                == query_type_project.id_relacao_contrapartida_categoria
            )
            assert (
                new_abginvest_tpproj_contrpart.id_abginvest_tpproj_lei
                == query_type_project.id_abginvest_tpproj_lei
            )
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    # Deleting abginvest_tpproj_lei_contrpart inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_abginvest_tpproj_lei_contrpart WHERE id='{}';".format(
                        REFERENCE_TABLE, new_abginvest_tpproj_contrpart.id
                    )
                )
            )
            conn.commit()
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


def test_select_abginvest_tpproj_lei_contrpart():
    """Shoul select a abginvest tpproj lei in AbginvestTpprojLeiContrparttable and compare it"""

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

    category_id = faker.random_number(digits=5)
    name_category = faker.text(max_nb_chars=120)
    description_category = faker.text(max_nb_chars=500)

    counterpart_id = faker.random_number(digits=5)
    description_counterpart = faker.word()
    example_aplicability = faker.word()
    required = faker.boolean()

    relationship_category_counterpart_id = faker.random_number(digits=5)

    abginvest_contrpart_id = faker.random_number(digits=5)
    order = faker.random_number(digits=5)

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

    # SQL commands
    data = AbginvestTpprojLeiContrpart(
        id=abginvest_contrpart_id,
        ordem=order,
        id_relacao_contrapartida_categoria=relationship_category_counterpart_id,
        id_abginvest_tpproj_lei=abginvest_id,
    )

    # Insert AbginvestTpprojLei
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    """
                        INSERT INTO {}_abginvest_tpproj_lei_contrpart
                        (id, ordem, id_relacao_contrapartida_categoria, id_abginvest_tpproj_lei)
                        VALUES ('{}', '{}', '{}', '{}');
                    """.format(
                        REFERENCE_TABLE,
                        abginvest_contrpart_id,
                        order,
                        relationship_category_counterpart_id,
                        abginvest_id,
                    )
                )
            )
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            conn.close()

    query_counterpart1 = (
        abginvest_tpproj_lei_contpart_repo.select_abginvest_tpproj_lei_contrpart(
            id=abginvest_contrpart_id
        )
    )
    query_counterpart2 = (
        abginvest_tpproj_lei_contpart_repo.select_abginvest_tpproj_lei_contrpart(
            id_abginvest_tpproj_lei=abginvest_id
        )
    )

    query_counterpart3 = (
        abginvest_tpproj_lei_contpart_repo.select_all_abginvest_tpproj_lei_contrpart()
    )

    assert data in query_counterpart1
    assert data in query_counterpart2
    assert data in query_counterpart3

    # Deleting abginvest_tpproj_lei_contrpart inserted with test
    with engine.begin() as conn:
        try:
            conn.execute(
                text(
                    "DELETE FROM {}_abginvest_tpproj_lei_contrpart WHERE id='{}';".format(
                        REFERENCE_TABLE, abginvest_contrpart_id
                    )
                )
            )
            conn.commit()
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
