from faker import Faker
from sqlalchemy import select
from src.infra.config import DBConnectionHandler
from src.infra.entities import CategoriaContrapartida
from .category_counterpart_repository import CategoryCounterpartRepository

faker = Faker()
category_counterpart_repo = CategoryCounterpartRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_category_counterpart():
    """Should insert CategoryCounterpart"""

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
        subcategoria_de_id=new_counterpart_primary.id,
    )

    # Select CategoryCounterpart
    query_1 = select(CategoriaContrapartida).where(
        CategoriaContrapartida.id == new_counterpart_primary.id
    )
    query_2 = select(CategoriaContrapartida).where(
        CategoriaContrapartida.subcategoria_de_id == new_counterpart_secundary.id
    )
    with DBConnectionHandler() as db_connection:
        try:
            for query_counterpart_primary in db_connection.session.execute(query_1):
                assert new_counterpart_primary.id == query_counterpart_primary[0].id
                assert new_counterpart_primary.nome == query_counterpart_primary[0].nome
                assert (
                    new_counterpart_primary.descricao
                    == query_counterpart_primary[0].descricao
                )
                assert (
                    new_counterpart_primary.subcategoria_de_id
                    == query_counterpart_primary[0].subcategoria_de_id
                )

            for query_counterpart_secundary in db_connection.session.execute(query_2):
                assert new_counterpart_secundary.id == query_counterpart_secundary[0].id
                assert (
                    new_counterpart_secundary.nome
                    == query_counterpart_secundary[0].nome
                )
                assert (
                    new_counterpart_secundary.descricao
                    == query_counterpart_secundary[0].descricao
                )
                assert (
                    new_counterpart_secundary.subcategoria_de_id
                    == query_counterpart_secundary[0].subcategoria_de_id
                )

            # Deleting CategoryCounterpart Inserted
            counterpart_secundary_inserted = db_connection.session.get(
                CategoriaContrapartida, new_counterpart_secundary.id
            )
            counterpart_primary_inserted = db_connection.session.get(
                CategoriaContrapartida, new_counterpart_primary.id
            )
            db_connection.session.delete(counterpart_secundary_inserted)
            db_connection.session.delete(counterpart_primary_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_category_counterpart():
    """Should select a category counterpart in CategoriaContrapartida table and compare it"""
    name_primary = faker.text(max_nb_chars=120)
    description_primary = faker.text(max_nb_chars=500)

    data_primary = CategoriaContrapartida(
        nome=name_primary,
        descricao=description_primary,
    )

    name_secundary = faker.text(max_nb_chars=120)
    description_secundary = faker.text(max_nb_chars=500)

    with DBConnectionHandler() as db_connection:
        try:
            db_connection.session.add(data_primary)
            db_connection.session.flush()
            db_connection.session.commit()

            data_secundary = CategoriaContrapartida(
                nome=name_secundary,
                descricao=description_secundary,
                subcategoria_de_id=data_primary.id,
            )

            db_connection.session.add(data_secundary)
            db_connection.session.flush()
            db_connection.session.commit()

            # Captura os IDs antes de desvincular
            secundary_id = data_secundary.id
            primary_id = data_primary.id

            # Desvincula os objetos da sessão antes de fazer a comparação
            db_connection.session.expunge(data_secundary)
            db_connection.session.expunge(data_primary)

            query_counterpart1 = category_counterpart_repo.select_category_counterpart(
                category_counterpart_id=secundary_id,
                subcategoria_de_id=primary_id,
            )
            query_counterpart2 = category_counterpart_repo.select_category_counterpart(
                category_counterpart_id=primary_id
            )
            query_counterpart3 = category_counterpart_repo.select_category_counterpart(
                subcategoria_de_id=primary_id
            )
            query_counterpart4 = (
                category_counterpart_repo.select_all_category_counterpart()
            )

            # Compara por ID em vez do objeto completo
            assert any(obj.id == secundary_id for obj in query_counterpart1)
            assert any(obj.id == primary_id for obj in query_counterpart2)
            assert any(obj.id == secundary_id for obj in query_counterpart3)
            assert any(obj.id == primary_id for obj in query_counterpart4)

            # Deleting CategoryCounterpart Inserted
            counterpart_secundary_inserted = db_connection.session.get(
                CategoriaContrapartida, secundary_id
            )
            counterpart_primary_inserted = db_connection.session.get(
                CategoriaContrapartida, primary_id
            )
            db_connection.session.delete(counterpart_secundary_inserted)
            db_connection.session.delete(counterpart_primary_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
