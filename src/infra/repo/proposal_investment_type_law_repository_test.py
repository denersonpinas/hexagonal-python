import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.abordagem_investimento import AbordagemInvestimento
from src.infra.entities.lei import Lei
from src.infra.entities.proposta_abginvest_tpproj_lei import PropostaAbginvestTpprojLei
from src.infra.entities.proposta import Proposta
from src.infra.entities.abginvest_tpproj_lei import AbginvestTpprojLei
from src.infra.entities.tipo_projeto import TipoProjeto  # Assuming this exists
from .proposal_investment_type_law_repository import ProposalInvestmentTypeLawRepository

faker = Faker()
proposal_investment_type_law = ProposalInvestmentTypeLawRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_proposal_investment_type_law():
    """Should insert Proposal Investment Type Law"""

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

    # Test data
    unique_id = str(uuid.uuid4().hex)

    with DBConnectionHandler() as db_connection:
        try:
            db_connection.session.add(investment_approach)
            db_connection.session.add(law)
            db_connection.session.add(type_project)
            db_connection.session.add(proposal)
            db_connection.session.flush()

            abginvest_tpproj_lei = AbginvestTpprojLei(
                abordagem_investimento_id=investment_approach.id,
                lei_id=law.id,
                tipo_pojeto_id=type_project.id,
            )

            db_connection.session.add(abginvest_tpproj_lei)
            db_connection.session.flush()
            db_connection.session.commit()

            new_investment_type_law = (
                proposal_investment_type_law.insert_proposal_investment_type_law(
                    id=unique_id,
                    investment_type_law_id=abginvest_tpproj_lei.id,
                    proposal_id=proposal.id,
                )
            )

            # Select Proposal Investment Type Law
            query = select(PropostaAbginvestTpprojLei).where(
                PropostaAbginvestTpprojLei.id == new_investment_type_law.id
            )

            for query_investment_type_law in db_connection.session.execute(query):
                assert new_investment_type_law.id == query_investment_type_law[0].id
                assert (
                    new_investment_type_law.abginvest_tpproj_lei_id
                    == query_investment_type_law[0].abginvest_tpproj_lei_id
                )
                assert (
                    new_investment_type_law.proposta_id
                    == query_investment_type_law[0].proposta_id
                )

            # Deleting Proposal Investment Type Law Inserted
            investment_type_law_inserted = db_connection.session.get(
                PropostaAbginvestTpprojLei, new_investment_type_law.id
            )
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
            db_connection.session.delete(investment_type_law_base)
            db_connection.session.delete(investment_approach_base)
            db_connection.session.delete(law_base)
            db_connection.session.delete(type_project_base)

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
