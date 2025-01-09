import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta import Proposta
from src.infra.entities.proposta_meta import PropostaMeta
from .proposal_meta_repository import ProposalMetaRepository

faker = Faker()
proposal_meta = ProposalMetaRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_proposal_meta():
    """Should insert Proposal Meta"""

    order = faker.random_int(min=1, max=10)
    goal = faker.text(max_nb_chars=120)
    quantity = faker.random_int(min=1, max=1000)

    id = str(uuid.uuid4().hex)
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
        id=id,
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

    with DBConnectionHandler() as db_connection:
        try:
            # Add Proposal for test
            db_connection.session.add(proposal)
            db_connection.session.flush()
            db_connection.session.commit()

            new_proposal_meta = proposal_meta.insert_proposal_meta(
                order=order, goal=goal, quantity=quantity, proposal_id=proposal.id
            )

            # Select Proposal Meta
            query = select(PropostaMeta).where(PropostaMeta.id == new_proposal_meta.id)

            for query_meta in db_connection.session.execute(query):
                assert new_proposal_meta.id == query_meta[0].id
                assert new_proposal_meta.ordem == query_meta[0].ordem
                assert new_proposal_meta.meta == query_meta[0].meta
                assert new_proposal_meta.quantitativo == query_meta[0].quantitativo
                assert new_proposal_meta.proposta_id == query_meta[0].proposta_id

            # Deleting Proposal Meta Inserted
            proposal_meta_inserted = db_connection.session.get(
                PropostaMeta, new_proposal_meta.id
            )
            proposal_inserted = db_connection.session.get(Proposta, proposal.id)
            db_connection.session.delete(proposal_meta_inserted)
            db_connection.session.delete(proposal_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
