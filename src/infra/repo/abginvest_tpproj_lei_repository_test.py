from faker import Faker
from sqlalchemy import select
from src.infra.config import DBConnectionHandler
from src.infra.entities import AbginvestTpprojLei
from src.infra.entities.abordagem_investimento import AbordagemInvestimento
from src.infra.entities.lei import Lei
from src.infra.entities.tipo_projeto import TipoProjeto
from .abginvest_tpproj_lei_repository import AbginvestTpprojLeiRepository

faker = Faker()
abginvest_tpproj_lei_repo = AbginvestTpprojLeiRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_abginvest_tpproj_lei():
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

    # SQL Commands
    with DBConnectionHandler() as db_connection:
        try:
            # Add Law, InvestmentApproach and TypeProject for test
            db_connection.session.add(investment_approach)
            db_connection.session.add(law)
            db_connection.session.add(type_project)
            db_connection.session.flush()
            db_connection.session.commit()

            new_abginvest_tpproj = (
                abginvest_tpproj_lei_repo.insert_abginvest_tpproj_lei(
                    abordagem_investimento_id=investment_approach.id,
                    lei_id=law.id,
                    tipo_pojeto_id=type_project.id,
                )
            )

            # Select AbginvestTpprojLei
            query = select(AbginvestTpprojLei).where(
                AbginvestTpprojLei.id == new_abginvest_tpproj.id
            )

            for query_abginvest_tpproj in db_connection.session.execute(query):
                assert new_abginvest_tpproj.id == query_abginvest_tpproj[0].id
                assert (
                    new_abginvest_tpproj.abordagem_investimento_id
                    == query_abginvest_tpproj[0].abordagem_investimento_id
                )
                assert new_abginvest_tpproj.lei_id == query_abginvest_tpproj[0].lei_id
                assert (
                    new_abginvest_tpproj.tipo_pojeto_id
                    == query_abginvest_tpproj[0].tipo_pojeto_id
                )

            # Deleting Law Inserted
            law_inserted = db_connection.session.get(Lei, law.id)
            investment_approach_inserted = db_connection.session.get(
                AbordagemInvestimento, investment_approach.id
            )
            type_project_inserted = db_connection.session.get(
                TipoProjeto, type_project.id
            )
            abginvest_tpproj_inserted = db_connection.session.get(
                AbginvestTpprojLei, new_abginvest_tpproj.id
            )
            db_connection.session.delete(abginvest_tpproj_inserted)
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


def test_select_abginvest_tpproj_lei():
    """Shoul select a abginvest tpproj lei in AbginvestTpprojLei table and compare it"""

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

    # SQL Commands
    with DBConnectionHandler() as db_connection:
        try:
            # Add Law, InvestmentApproach and TypeProject for test
            db_connection.session.add(investment_approach)
            db_connection.session.add(law)
            db_connection.session.add(type_project)
            db_connection.session.flush()
            db_connection.session.commit()

            data = AbginvestTpprojLei(
                abordagem_investimento_id=investment_approach.id,
                lei_id=law.id,
                tipo_pojeto_id=type_project.id,
            )

            # Add AbginvestTpprojLei for test
            db_connection.session.add(data)
            db_connection.session.flush()
            db_connection.session.commit()

            query_counterpart1 = abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
                id=data.id
            )
            query_counterpart2 = abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
                abordagem_investimento_id=investment_approach.id
            )
            query_counterpart3 = abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
                lei_id=law.id
            )
            query_counterpart4 = abginvest_tpproj_lei_repo.select_abginvest_tpproj_lei(
                tipo_pojeto_id=type_project.id
            )
            query_counterpart5 = (
                abginvest_tpproj_lei_repo.select_all_abginvest_tpproj_lei()
            )

            assert data in query_counterpart5
            assert data in query_counterpart1
            assert data in query_counterpart2
            assert data in query_counterpart3
            assert data in query_counterpart4

            # Deleting Law Inserted
            law_inserted = db_connection.session.get(Lei, law.id)
            investment_approach_inserted = db_connection.session.get(
                AbordagemInvestimento, investment_approach.id
            )
            type_project_inserted = db_connection.session.get(
                TipoProjeto, type_project.id
            )
            abginvest_tpproj_inserted = db_connection.session.get(
                AbginvestTpprojLei, data.id
            )
            db_connection.session.delete(abginvest_tpproj_inserted)
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
