import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_local_execucao import PropostaLocalExecucao
from src.infra.entities.municipio import Municipio
from src.infra.entities.proposta import Proposta
from .proposal_execution_location_repository import ProposalExecutionLocationRepository

faker = Faker()
proposal_location = ProposalExecutionLocationRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_proposal_execution_location():
    """Should insert Proposal Execution Location"""

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

    with DBConnectionHandler() as db_connection:
        try:
            city = Municipio(nome=faker.city(), uf=faker.state_abbr())
            db_connection.session.add(city)
            db_connection.session.flush()

            db_connection.session.add(proposal)
            db_connection.session.flush()
            db_connection.session.commit()

            new_location = proposal_location.insert_proposal_execution_location(
                city_id=city.id, proposal_id=proposal.id
            )

            # Select Proposal Execution Location
            query = select(PropostaLocalExecucao).where(
                PropostaLocalExecucao.id == new_location.id
            )

            for query_location in db_connection.session.execute(query):
                assert new_location.id == query_location[0].id
                assert new_location.municipio_id == query_location[0].municipio_id
                assert new_location.proposta_id == query_location[0].proposta_id

            # Deleting Location Inserted
            location_inserted = db_connection.session.get(
                PropostaLocalExecucao, new_location.id
            )
            db_connection.session.delete(location_inserted)

            # Deleting Proposal Created
            proposal_inserted = db_connection.session.get(Proposta, proposal.id)
            db_connection.session.delete(proposal_inserted)

            # Deleting City Created
            city_inserted = db_connection.session.get(Municipio, city.id)
            db_connection.session.delete(city_inserted)

            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
