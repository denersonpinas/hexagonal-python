import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta import Proposta
from .proposal_repository import ProposalRepository

faker = Faker()
proposal = ProposalRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_proposal():
    """Should insert Proposal"""

    id = str(uuid.uuid4().hex)  # Create id of the TipoArquivo entity
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

    # SQL commands
    new_proposal = proposal.insert_proposal(
        id=id,
        titulo_projeto=titulo_projeto,
        resumo_projeto=resumo_projeto,
        descricao_projeto=descricao_projeto,
        dados_bancario_instituicao=dados_bancario_instituicao,
        dados_bancario_agencia_conta_bancaria=dados_bancario_agencia_conta_bancaria,
        dados_bancario_conta_corrente=dados_bancario_conta_corrente,
        valor_total_projeto=valor_total_projeto,
        valor_total_lei_incentivo=valor_total_lei_incentivo,
        dados_bancario_cnpj_fundo=dados_bancario_cnpj_fundo,
        dados_bancario_razao_social_fundo=dados_bancario_razao_social_fundo,
        dados_bancario_contato_fundo_nome=dados_bancario_contato_fundo_nome,
        dados_bancario_contato_fundo_email=dados_bancario_contato_fundo_email,
        valor_total_captado=valor_total_captado,
        valor_total_captado_lei_incentivo=valor_total_captado_lei_incentivo,
        valor_total_incentivado_nubank=valor_total_incentivado_nubank,
        observacoes=observacoes,
        data_inicio_projeto=data_inicio_projeto,
        data_fim_projeto=data_fim_projeto,
    )

    # Select Proposal
    query = select(Proposta).where(Proposta.id == new_proposal.id)
    with DBConnectionHandler() as db_connection:
        try:
            for query_proposal in db_connection.session.execute(query):
                assert new_proposal.id == query_proposal[0].id
                assert new_proposal.titulo_projeto == query_proposal[0].titulo_projeto
                assert new_proposal.resumo_projeto == query_proposal[0].resumo_projeto
                assert (
                    new_proposal.descricao_projeto
                    == query_proposal[0].descricao_projeto
                )
                assert (
                    new_proposal.dados_bancario_instituicao
                    == query_proposal[0].dados_bancario_instituicao
                )
                assert (
                    new_proposal.dados_bancario_agencia_conta_bancaria
                    == query_proposal[0].dados_bancario_agencia_conta_bancaria
                )
                assert (
                    new_proposal.dados_bancario_conta_corrente
                    == query_proposal[0].dados_bancario_conta_corrente
                )
                assert (
                    new_proposal.valor_total_projeto
                    == query_proposal[0].valor_total_projeto
                )
                assert (
                    new_proposal.valor_total_lei_incentivo
                    == query_proposal[0].valor_total_lei_incentivo
                )
                assert (
                    new_proposal.dados_bancario_cnpj_fundo
                    == query_proposal[0].dados_bancario_cnpj_fundo
                )
                assert (
                    new_proposal.dados_bancario_razao_social_fundo
                    == query_proposal[0].dados_bancario_razao_social_fundo
                )
                assert (
                    new_proposal.dados_bancario_contato_fundo_nome
                    == query_proposal[0].dados_bancario_contato_fundo_nome
                )
                assert (
                    new_proposal.dados_bancario_contato_fundo_email
                    == query_proposal[0].dados_bancario_contato_fundo_email
                )
                assert (
                    new_proposal.valor_total_captado
                    == query_proposal[0].valor_total_captado
                )
                assert (
                    new_proposal.valor_total_captado_lei_incentivo
                    == query_proposal[0].valor_total_captado_lei_incentivo
                )
                assert (
                    new_proposal.valor_total_incentivado_nubank
                    == query_proposal[0].valor_total_incentivado_nubank
                )
                assert new_proposal.observacoes == query_proposal[0].observacoes
                assert (
                    new_proposal.data_inicio_projeto
                    == query_proposal[0].data_inicio_projeto
                )
                assert (
                    new_proposal.data_fim_projeto == query_proposal[0].data_fim_projeto
                )

            # Deleting Proposal Inserted
            proposal_inserted = db_connection.session.get(Proposta, new_proposal.id)
            db_connection.session.delete(proposal_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
