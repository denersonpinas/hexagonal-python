import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta import Proposta
from src.infra.entities.proposta_patrocinador import PropostaPatrocinador
from .proposal_sponsor_repository import ProposalSponsorRepository

faker = Faker()
proposal_sponsor = ProposalSponsorRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_proposal_sponsor():
    """Should insert Proposal Sponsor"""

    name = faker.text(max_nb_chars=100)
    format = faker.text(max_nb_chars=50)
    value = round(
        faker.pyfloat(right_digits=2, positive=True, min_value=100, max_value=10000), 2
    )

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
            db_connection.session.add(proposal)
            db_connection.session.flush()
            db_connection.session.commit()

            new_proposal_sponsor = proposal_sponsor.insert_proposal_sponsor(
                nome=name, formato=format, valor=value, proposta_id=proposal.id
            )

            # Select Proposal Sponsor
            query = select(PropostaPatrocinador).where(
                PropostaPatrocinador.id == new_proposal_sponsor.id
            )

            for query_sponsor in db_connection.session.execute(query):
                assert new_proposal_sponsor.id == query_sponsor[0].id
                assert new_proposal_sponsor.nome == query_sponsor[0].nome
                assert new_proposal_sponsor.formato == query_sponsor[0].formato
                assert new_proposal_sponsor.valor == query_sponsor[0].valor
                assert new_proposal_sponsor.proposta_id == query_sponsor[0].proposta_id

            # Deleting Proposal Sponsor Inserted
            proposal_sponsor_inserted = db_connection.session.get(
                PropostaPatrocinador, new_proposal_sponsor.id
            )
            proposal_inserted = db_connection.session.get(Proposta, proposal.id)
            db_connection.session.delete(proposal_sponsor_inserted)
            db_connection.session.delete(proposal_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
