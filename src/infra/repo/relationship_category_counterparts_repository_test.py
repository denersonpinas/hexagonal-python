from faker import Faker
from sqlalchemy import select
from src.infra.config import DBConnectionHandler
from src.infra.entities import RelacaoCategoriaContrapartida
from src.infra.entities.categoria_contrapartida import CategoriaContrapartida
from src.infra.entities.contrapartida import Contrapartida
from .relationship_category_counterparts_repository import (
    RelationshipCategoryCounterpartsRepository,
)

faker = Faker()
reltp_categ_count_repo = RelationshipCategoryCounterpartsRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_relationship_category_counterpart():
    """Should insert relationship category counterpart"""

    name_category = faker.text(max_nb_chars=120)
    description_category = faker.text(max_nb_chars=500)

    category = CategoriaContrapartida(
        nome=name_category,
        descricao=description_category,
    )

    description_counterpart = faker.word()
    example_aplicability = faker.word()
    required = faker.boolean()

    counterpart = Contrapartida(
        descricao=description_counterpart,
        exemplo_aplicabilidade=example_aplicability,
        obrigatoria=required,
        padrao=True,
    )

    # SQL Commands
    with DBConnectionHandler() as db_connection:
        try:
            # Add Law, InvestmentApproach, TypeProject, CategoryCounterpart and Counterpart for test
            db_connection.session.add(category)
            db_connection.session.add(counterpart)
            db_connection.session.flush()
            db_connection.session.commit()

            new_rel_category_counterpart = (
                reltp_categ_count_repo.insert_relationship_category_counterparts(
                    categoria_id=category.id, contrapartida_id=counterpart.id
                )
            )

            # Select AbginvestTpprojLeiCoutrpart
            query = select(RelacaoCategoriaContrapartida).where(
                RelacaoCategoriaContrapartida.id == new_rel_category_counterpart.id
            )

            for query_rel_category_counterpart in db_connection.session.execute(query):
                assert (
                    new_rel_category_counterpart.id
                    == query_rel_category_counterpart[0].id
                )
                assert (
                    new_rel_category_counterpart.categoria_id
                    == query_rel_category_counterpart[0].categoria_id
                )
                assert (
                    new_rel_category_counterpart.contrapartida_id
                    == query_rel_category_counterpart[0].contrapartida_id
                )

            # Deleting All registers Insert
            category_inserted = db_connection.session.get(
                CategoriaContrapartida, category.id
            )
            counterpart_inserted = db_connection.session.get(
                Contrapartida, counterpart.id
            )
            relationship_catg_count_inserted = db_connection.session.get(
                RelacaoCategoriaContrapartida, new_rel_category_counterpart.id
            )
            db_connection.session.delete(relationship_catg_count_inserted)
            db_connection.session.delete(category_inserted)
            db_connection.session.delete(counterpart_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_relationship_category_counterpart():
    """Shoul select a category counterpart in CategoriaContrapartida table and compare it"""

    name_category = faker.text(max_nb_chars=120)
    description_category = faker.text(max_nb_chars=500)

    category = CategoriaContrapartida(
        nome=name_category,
        descricao=description_category,
    )

    description_counterpart = faker.word()
    example_aplicability = faker.word()
    required = faker.boolean()

    counterpart = Contrapartida(
        descricao=description_counterpart,
        exemplo_aplicabilidade=example_aplicability,
        obrigatoria=required,
        padrao=True,
    )

    # SQL Commands
    with DBConnectionHandler() as db_connection:
        try:
            # Add Law, InvestmentApproach, TypeProject, CategoryCounterpart and Counterpart for test
            db_connection.session.add(category)
            db_connection.session.add(counterpart)
            db_connection.session.flush()
            db_connection.session.commit()

            data = RelacaoCategoriaContrapartida(
                categoria_id=category.id,
                contrapartida_id=counterpart.id,
            )

            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_1 = (
                reltp_categ_count_repo.select_all_relationship_category_counterparts()
            )
            query_2 = reltp_categ_count_repo.select_relationship_category_counterparts(
                id=data.id
            )
            query_3 = reltp_categ_count_repo.select_relationship_category_counterparts(
                categoria_id=category.id
            )
            query_4 = reltp_categ_count_repo.select_relationship_category_counterparts(
                contrapartida_id=counterpart.id
            )

            assert data in query_1
            assert data in query_2
            assert data in query_3
            assert data in query_4

            # Deleting All registers Insert
            category_inserted = db_connection.session.get(
                CategoriaContrapartida, category.id
            )
            counterpart_inserted = db_connection.session.get(
                Contrapartida, counterpart.id
            )
            relationship_catg_count_inserted = db_connection.session.get(
                RelacaoCategoriaContrapartida, data.id
            )
            db_connection.session.delete(relationship_catg_count_inserted)
            db_connection.session.delete(category_inserted)
            db_connection.session.delete(counterpart_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
