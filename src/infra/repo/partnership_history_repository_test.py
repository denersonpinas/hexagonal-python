import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.historico_de_parcerias import HistoricoDeParcerias
from src.infra.entities.proponente import Proponente
from src.infra.entities.proposta import Proposta
from .partnership_history_repository import PartnershipHistoryRepository

faker = Faker("pt_BR")
partnership_history = PartnershipHistoryRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_partnership_history():
    """Should insert Partnership History"""

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

    # Proponent test data
    cnpj = faker.cnpj().replace(".", "").replace("/", "").replace("-", "")[:14]
    company_name = faker.company()[:120]
    trade_name = faker.company_suffix()[:120]
    zip_code = faker.postcode()[:8]
    state = faker.state_abbr()[:2]
    city = faker.city()[:120]
    neighborhood = faker.city_suffix()[:120]
    street = faker.street_name()[:120]
    number = str(faker.building_number())[:4]  # Convertendo para string e limitando
    complement = faker.street_suffix()[:100]
    website = faker.url()[:250]
    social_media = faker.url()[:250]
    curriculum_summary = faker.text()

    # Test data
    sponsors_number = faker.random_int(min=1, max=100)
    renewal_number = faker.random_int(min=0, max=10)
    additional_info = faker.text()

    with DBConnectionHandler() as db_connection:
        try:

            db_connection.session.add(proposal)
            db_connection.session.flush()

            proponent = Proponente(
                cnpj=cnpj,
                proposta_id=proposal.id,
                razao_social=company_name,
                nome_fantasia=trade_name,
                endereco_cep=zip_code,
                endereco_uf=state,
                endereco_municipio=city,
                endereco_bairro=neighborhood,
                endereco_logradouro=street,
                endereco_numero=number,
                endereco_complemento=complement,
                site=website,
                rede_social=social_media,
                resumo_curriculo=curriculum_summary,
            )

            db_connection.session.add(proponent)
            db_connection.session.flush()
            db_connection.session.commit()

            new_history = partnership_history.insert_partnership_history(
                sponsors_number=sponsors_number,
                renewal_number=renewal_number,
                proposal_id=proponent.proposta_id,
                additional_info=additional_info,
            )

            # Select Partnership History
            query = select(HistoricoDeParcerias).where(
                HistoricoDeParcerias.id == new_history.id
            )

            for query_history in db_connection.session.execute(query):
                assert new_history.id == query_history[0].id
                assert (
                    new_history.numero_de_patrocinadores
                    == query_history[0].numero_de_patrocinadores
                )
                assert (
                    new_history.numero_de_renovacao
                    == query_history[0].numero_de_renovacao
                )
                assert new_history.proposta_id == query_history[0].proposta_id
                assert (
                    new_history.informacoes_adicionais
                    == query_history[0].informacoes_adicionais
                )

            # Deleting Partnership History Inserted
            history_inserted = db_connection.session.get(
                HistoricoDeParcerias, new_history.id
            )
            db_connection.session.delete(history_inserted)

            # Deleting Proponent Created
            proponent_inserted = db_connection.session.get(
                Proponente, proponent.proposta_id
            )
            db_connection.session.delete(proponent_inserted)

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
