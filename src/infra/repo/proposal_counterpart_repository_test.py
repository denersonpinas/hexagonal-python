import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.abginvest_tpproj_lei_contrpart import (
    AbginvestTpprojLeiContrpart,
)
from src.infra.entities.abordagem_investimento import AbordagemInvestimento
from src.infra.entities.categoria_contrapartida import CategoriaContrapartida
from src.infra.entities.contrapartida import Contrapartida
from src.infra.entities.lei import Lei
from src.infra.entities.proposta_abginvest_tpproj_lei import PropostaAbginvestTpprojLei
from src.infra.entities.proposta import Proposta
from src.infra.entities.abginvest_tpproj_lei import AbginvestTpprojLei
from src.infra.entities.proposta_contrapartida import PropostaContrapartida
from src.infra.entities.relacao_categoria_contrapartida import (
    RelacaoCategoriaContrapartida,
)
from src.infra.entities.tipo_projeto import TipoProjeto
from src.infra.repo.proposal_counterpart_repository import ProposalCounterpartRepository

faker = Faker()
proposal_counterpart = ProposalCounterpartRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_proposal_counterpart():
    """Should insert Proposal Counterpart"""

    description_investment_approach = faker.word()
    incentivized = faker.boolean()

    investment_approach = AbordagemInvestimento(
        descricao=description_investment_approach, incentivado=incentivized
    )

    name = faker.text(max_nb_chars=100)
    description_law = faker.text(max_nb_chars=250)

    law = Lei(nome=name, descricao=description_law)

    name_project = faker.text(max_nb_chars=100)
    description_project = faker.text(max_nb_chars=250)

    type_project = TipoProjeto(nome=name_project, descricao=description_project)

    id_proposal = str(uuid.uuid4().hex)
    titulo_projeto = faker.text(max_nb_chars=100)
    resumo_projeto = faker.text(max_nb_chars=250)
    descricao_projeto = faker.text(max_nb_chars=500)
    dados_bancario_instituicao = faker.company()
    dados_bancario_agencia_conta_bancaria = faker.bban()[:14]
    dados_bancario_conta_corrente = faker.bban()[:14]
    valor_total_projeto = faker.pyfloat(left_digits=6, right_digits=2, positive=True)
    valor_total_lei_incentivo = faker.pyfloat(
        left_digits=6, right_digits=2, positive=True
    )
    dados_bancario_cnpj_fundo = faker.bban()[:14]
    dados_bancario_razao_social_fundo = faker.bban()[:14]
    dados_bancario_contato_fundo_nome = faker.bban()[:14]
    dados_bancario_contato_fundo_email = faker.bban()[:14]
    valor_total_captado = faker.pyfloat(left_digits=6, right_digits=2, positive=True)
    valor_total_captado_lei_incentivo = faker.pyfloat(
        left_digits=6, right_digits=2, positive=True
    )
    valor_total_incentivado_nubank = faker.pyfloat(
        left_digits=6, right_digits=2, positive=True
    )
    observacoes = faker.text(max_nb_chars=250)
    data_inicio_projeto = faker.date()
    data_fim_projeto = faker.date()
    proposal = Proposta(
        id=id_proposal,
        titulo_projeto=titulo_projeto,
        resumo_projeto=resumo_projeto,
        descricao_projeto=descricao_projeto,
        dados_bancario_instituicao=dados_bancario_instituicao,
        dados_bancario_agencia_conta_bancaria=dados_bancario_agencia_conta_bancaria,
        dados_bancario_conta_corrente=dados_bancario_conta_corrente,
        dados_bancario_cnpj_fundo=dados_bancario_cnpj_fundo,
        dados_bancario_razao_social_fundo=dados_bancario_razao_social_fundo,
        dados_bancario_contato_fundo_nome=dados_bancario_contato_fundo_nome,
        dados_bancario_contato_fundo_email=dados_bancario_contato_fundo_email,
        valor_total_projeto=valor_total_projeto,
        valor_total_lei_incentivo=valor_total_lei_incentivo,
        valor_total_captado=valor_total_captado,
        valor_total_captado_lei_incentivo=valor_total_captado_lei_incentivo,
        valor_total_incentivado_nubank=valor_total_incentivado_nubank,
        observacoes=observacoes,
        data_inicio_projeto=data_inicio_projeto,
        data_fim_projeto=data_fim_projeto,
    )

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

    # Test data
    unique_id = str(uuid.uuid4().hex)
    description = faker.text(max_nb_chars=200)
    quantity = faker.random_int(min=1, max=100)
    expected = faker.random_int(min=1, max=100)

    with DBConnectionHandler() as db_connection:
        try:
            db_connection.session.add(investment_approach)
            db_connection.session.add(law)
            db_connection.session.add(type_project)
            db_connection.session.add(proposal)
            db_connection.session.add(category)
            db_connection.session.add(counterpart)
            db_connection.session.flush()

            abginvest_tpproj_lei = AbginvestTpprojLei(
                abordagem_investimento_id=investment_approach.id,
                lei_id=law.id,
                tipo_pojeto_id=type_project.id,
            )

            db_connection.session.add(abginvest_tpproj_lei)
            db_connection.session.flush()

            investment_type_law = PropostaAbginvestTpprojLei(
                id=str(uuid.uuid4().hex),
                abginvest_tpproj_lei_id=abginvest_tpproj_lei.id,
                proposta_id=proposal.id,
            )

            relationship_catg_count = RelacaoCategoriaContrapartida(
                categoria_id=category.id, contrapartida_id=counterpart.id
            )

            db_connection.session.add(relationship_catg_count)
            db_connection.session.add(investment_type_law)
            db_connection.session.flush()

            abginvest_tpproj_lei_contrpart = AbginvestTpprojLeiContrpart(
                ordem=order,
                relacao_contrapartida_categoria_id=relationship_catg_count.id,
                abginvest_tpproj_lei_id=abginvest_tpproj_lei.id,
            )

            db_connection.session.add(abginvest_tpproj_lei_contrpart)
            db_connection.session.flush()
            db_connection.session.commit()

            new_counterpart = proposal_counterpart.insert_proposal_counterpart(
                id=unique_id,
                description=description,
                quantity=quantity,
                expected=expected,
                investment_type_law_counterpart_id=abginvest_tpproj_lei_contrpart.id,
                proposal_investment_type_law_id=investment_type_law.id,
            )

            # Select Proposal Counterpart
            query = select(PropostaContrapartida).where(
                PropostaContrapartida.id == new_counterpart.id
            )

            for query_counterpart in db_connection.session.execute(query):
                assert new_counterpart.id == query_counterpart[0].id
                assert new_counterpart.descricao == query_counterpart[0].descricao
                assert new_counterpart.quantitativo == query_counterpart[0].quantitativo
                assert new_counterpart.previsto == query_counterpart[0].previsto
                assert (
                    new_counterpart.abginvest_tpproj_lei_contrpart_id
                    == query_counterpart[0].abginvest_tpproj_lei_contrpart_id
                )
                assert (
                    new_counterpart.proposta_abginvest_tpproj_lei_id
                    == query_counterpart[0].proposta_abginvest_tpproj_lei_id
                )

            # Deleting Proposal Investment Type Law Inserted
            counterpart_inserted = db_connection.session.get(
                PropostaContrapartida, new_counterpart.id
            )
            db_connection.session.delete(counterpart_inserted)

            abginvest_tpproj_lei_contrpart_inserted = db_connection.session.get(
                AbginvestTpprojLeiContrpart, abginvest_tpproj_lei_contrpart.id
            )
            relationship_catg_count_inserted = db_connection.session.get(
                RelacaoCategoriaContrapartida, relationship_catg_count.id
            )
            investment_type_law_inserted = db_connection.session.get(
                PropostaAbginvestTpprojLei, investment_type_law.id
            )
            db_connection.session.delete(abginvest_tpproj_lei_contrpart_inserted)
            db_connection.session.delete(relationship_catg_count_inserted)
            db_connection.session.delete(investment_type_law_inserted)

            # Deleting Investment Type Law Created
            investment_type_law_base = db_connection.session.get(
                AbginvestTpprojLei, abginvest_tpproj_lei.id
            )
            investment_approach_base = db_connection.session.get(
                AbordagemInvestimento, investment_approach.id
            )
            law_base = db_connection.session.get(Lei, law.id)
            type_project_base = db_connection.session.get(TipoProjeto, type_project.id)
            category_base = db_connection.session.get(
                CategoriaContrapartida, category.id
            )
            counterpart_base = db_connection.session.get(Contrapartida, counterpart.id)
            db_connection.session.delete(investment_type_law_base)
            db_connection.session.delete(investment_approach_base)
            db_connection.session.delete(law_base)
            db_connection.session.delete(type_project_base)
            db_connection.session.delete(category_base)
            db_connection.session.delete(counterpart_base)

            # Deleting Proposal Created
            proposal_inserted = db_connection.session.get(Proposta, proposal.id)
            db_connection.session.delete(proposal_inserted)

            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
