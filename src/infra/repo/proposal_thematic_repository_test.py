import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_tematica import PropostaTematica
from src.infra.entities.proposta import Proposta
from src.infra.entities.tematica import Tematica  # Assuming this exists
from .proposal_thematic_repository import ProposalThematicRepository

faker = Faker()
proposal_thematic = ProposalThematicRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_proposal_thematic():
    """Should insert Proposal Thematic"""

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

    description = faker.text(max_nb_chars=50)
    thematic = Tematica(descricao=description)

    with DBConnectionHandler() as db_connection:
        try:
            db_connection.session.add(proposal)
            db_connection.session.add(thematic)
            db_connection.session.flush()
            db_connection.session.commit()

            new_thematic = proposal_thematic.insert_proposal_thematic(
                proposal_id=str(proposal.id), thematic_id=thematic.id
            )

            # Select Proposal Thematic
            query = select(PropostaTematica).where(
                PropostaTematica.id == new_thematic.id
            )

            for query_thematic in db_connection.session.execute(query):
                assert new_thematic.id == query_thematic[0].id
                assert new_thematic.proposta_id == query_thematic[0].proposta_id
                assert new_thematic.tematica_id == query_thematic[0].tematica_id

            # Deleting Proposal Thematic Inserted
            thematic_inserted = db_connection.session.get(
                PropostaTematica, new_thematic.id
            )
            db_connection.session.delete(thematic_inserted)

            # Deleting Thematic Created
            thematic_base = db_connection.session.get(Tematica, thematic.id)
            db_connection.session.delete(thematic_base)

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
