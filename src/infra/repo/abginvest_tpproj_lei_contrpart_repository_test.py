from faker import Faker
from sqlalchemy import select
from src.infra.config import DBConnectionHandler
from src.infra.entities import AbginvestTpprojLeiContrpart
from src.infra.entities.abginvest_tpproj_lei import AbginvestTpprojLei
from src.infra.entities.abordagem_investimento import AbordagemInvestimento
from src.infra.entities.categoria_contrapartida import CategoriaContrapartida
from src.infra.entities.contrapartida import Contrapartida
from src.infra.entities.lei import Lei
from src.infra.entities.relacao_categoria_contrapartida import (
    RelacaoCategoriaContrapartida,
)
from src.infra.entities.tipo_projeto import TipoProjeto
from src.infra.repo import AbginvestTpprojLeiContrpartRepository

faker = Faker()
abginvest_tpproj_lei_contpart_repo = AbginvestTpprojLeiContrpartRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_abginvest_tpproj_lei_contrpart():
    """Should insert abginvest tpproj lei"""

    description = faker.word()
    incentivized = faker.boolean()

    investment_approach = AbordagemInvestimento(
        descricao=description, incentivado=incentivized
    )

    name = faker.text(max_nb_chars=100)
    description_law = faker.text(max_nb_chars=250)

    law = Lei(nome=name, descricao=description_law)

    name_project = faker.text(max_nb_chars=100)
    description_project = faker.text(max_nb_chars=250)

    type_project = TipoProjeto(nome=name_project, descricao=description_project)

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

    order = faker.random_number(digits=2)

    # SQL Commands
    with DBConnectionHandler() as db_connection:
        try:
            # Add Law, InvestmentApproach, TypeProject, CategoryCounterpart and Counterpart for test
            db_connection.session.add(investment_approach)
            db_connection.session.add(law)
            db_connection.session.add(type_project)
            db_connection.session.add(category)
            db_connection.session.add(counterpart)
            db_connection.session.flush()
            db_connection.session.commit()

            # Add AbginvestTpprojLei and RelasionshipCateogryCounterpart for test
            abginvest_tpproj_lei = AbginvestTpprojLei(
                abordagem_investimento_id=investment_approach.id,
                lei_id=law.id,
                tipo_pojeto_id=type_project.id,
            )

            relationship_catg_count = RelacaoCategoriaContrapartida(
                categoria_id=category.id, contrapartida_id=counterpart.id
            )

            db_connection.session.add(abginvest_tpproj_lei)
            db_connection.session.add(relationship_catg_count)
            db_connection.session.flush()
            db_connection.session.commit()

            new_abginvest_tpproj_contrpart = abginvest_tpproj_lei_contpart_repo.insert_abginvest_tpproj_lei_contrpart(
                ordem=order,
                id_relacao_contrapartida_categoria=relationship_catg_count.id,
                id_abginvest_tpproj_lei=abginvest_tpproj_lei.id,
            )

            # Select AbginvestTpprojLeiCoutrpart
            query = select(AbginvestTpprojLeiContrpart).where(
                AbginvestTpprojLeiContrpart.id == new_abginvest_tpproj_contrpart.id
            )

            for query_abginvest_tpproj_contrpart in db_connection.session.execute(
                query
            ):
                assert (
                    new_abginvest_tpproj_contrpart.id
                    == query_abginvest_tpproj_contrpart[0].id
                )
                assert (
                    new_abginvest_tpproj_contrpart.ordem
                    == query_abginvest_tpproj_contrpart[0].ordem
                )
                assert (
                    new_abginvest_tpproj_contrpart.relacao_contrapartida_categoria_id
                    == query_abginvest_tpproj_contrpart[
                        0
                    ].relacao_contrapartida_categoria_id
                )
                assert (
                    new_abginvest_tpproj_contrpart.abginvest_tpproj_lei_id
                    == query_abginvest_tpproj_contrpart[0].abginvest_tpproj_lei_id
                )

            # Deleting All registers Insert
            law_inserted = db_connection.session.get(Lei, law.id)
            investment_approach_inserted = db_connection.session.get(
                AbordagemInvestimento, investment_approach.id
            )
            type_project_inserted = db_connection.session.get(
                TipoProjeto, type_project.id
            )
            category_inserted = db_connection.session.get(
                CategoriaContrapartida, category.id
            )
            counterpart_inserted = db_connection.session.get(
                Contrapartida, counterpart.id
            )
            abginvest_tpproj_inserted = db_connection.session.get(
                AbginvestTpprojLei, abginvest_tpproj_lei.id
            )
            relationship_catg_count_inserted = db_connection.session.get(
                RelacaoCategoriaContrapartida, relationship_catg_count.id
            )
            abginvest_tpproj_contrpart_inserted = db_connection.session.get(
                AbginvestTpprojLeiContrpart, new_abginvest_tpproj_contrpart.id
            )
            db_connection.session.delete(abginvest_tpproj_contrpart_inserted)
            db_connection.session.delete(relationship_catg_count_inserted)
            db_connection.session.delete(abginvest_tpproj_inserted)
            db_connection.session.delete(category_inserted)
            db_connection.session.delete(counterpart_inserted)
            db_connection.session.delete(law_inserted)
            db_connection.session.delete(investment_approach_inserted)
            db_connection.session.delete(type_project_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


def test_select_abginvest_tpproj_lei_contrpart():
    """Shoul select a abginvest tpproj lei in AbginvestTpprojLeiContrparttable and compare it"""

    description = faker.word()
    incentivized = faker.boolean()

    investment_approach = AbordagemInvestimento(
        descricao=description, incentivado=incentivized
    )

    name = faker.text(max_nb_chars=100)
    description_law = faker.text(max_nb_chars=250)

    law = Lei(nome=name, descricao=description_law)

    name_project = faker.text(max_nb_chars=100)
    description_project = faker.text(max_nb_chars=250)

    type_project = TipoProjeto(nome=name_project, descricao=description_project)

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

    order = faker.random_number(digits=2)

    # SQL Commands
    with DBConnectionHandler() as db_connection:
        try:
            # Add Law, InvestmentApproach, TypeProject, CategoryCounterpart and Counterpart for test
            db_connection.session.add(investment_approach)
            db_connection.session.add(law)
            db_connection.session.add(type_project)
            db_connection.session.add(category)
            db_connection.session.add(counterpart)
            db_connection.session.flush()
            db_connection.session.commit()

            # Add AbginvestTpprojLei and RelasionshipCateogryCounterpart for test
            abginvest_tpproj_lei = AbginvestTpprojLei(
                abordagem_investimento_id=investment_approach.id,
                lei_id=law.id,
                tipo_pojeto_id=type_project.id,
            )

            relationship_catg_count = RelacaoCategoriaContrapartida(
                categoria_id=category.id, contrapartida_id=counterpart.id
            )

            db_connection.session.add(abginvest_tpproj_lei)
            db_connection.session.add(relationship_catg_count)
            db_connection.session.flush()
            db_connection.session.commit()

            data = AbginvestTpprojLeiContrpart(
                ordem=order,
                relacao_contrapartida_categoria_id=relationship_catg_count.id,
                abginvest_tpproj_lei_id=abginvest_tpproj_lei.id,
            )

            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_counterpart1 = abginvest_tpproj_lei_contpart_repo.select_abginvest_tpproj_lei_contrpart(
                id=data.id
            )
            query_counterpart2 = abginvest_tpproj_lei_contpart_repo.select_abginvest_tpproj_lei_contrpart(
                id_abginvest_tpproj_lei=abginvest_tpproj_lei.id
            )

            query_counterpart3 = (
                abginvest_tpproj_lei_contpart_repo.select_all_abginvest_tpproj_lei_contrpart()
            )

            assert data in query_counterpart3
            assert data in query_counterpart1
            assert data in query_counterpart2

            # Deleting All registers Insert
            law_inserted = db_connection.session.get(Lei, law.id)
            investment_approach_inserted = db_connection.session.get(
                AbordagemInvestimento, investment_approach.id
            )
            type_project_inserted = db_connection.session.get(
                TipoProjeto, type_project.id
            )
            category_inserted = db_connection.session.get(
                CategoriaContrapartida, category.id
            )
            counterpart_inserted = db_connection.session.get(
                Contrapartida, counterpart.id
            )
            abginvest_tpproj_inserted = db_connection.session.get(
                AbginvestTpprojLei, abginvest_tpproj_lei.id
            )
            relationship_catg_count_inserted = db_connection.session.get(
                RelacaoCategoriaContrapartida, relationship_catg_count.id
            )
            abginvest_tpproj_contrpart_inserted = db_connection.session.get(
                AbginvestTpprojLeiContrpart, data.id
            )
            db_connection.session.delete(abginvest_tpproj_contrpart_inserted)
            db_connection.session.delete(relationship_catg_count_inserted)
            db_connection.session.delete(abginvest_tpproj_inserted)
            db_connection.session.delete(category_inserted)
            db_connection.session.delete(counterpart_inserted)
            db_connection.session.delete(law_inserted)
            db_connection.session.delete(investment_approach_inserted)
            db_connection.session.delete(type_project_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
