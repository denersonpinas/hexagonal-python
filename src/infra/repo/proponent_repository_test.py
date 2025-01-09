import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proponente import Proponente
from src.infra.entities.proposta import Proposta
from .proponent_repository import ProponentRepository

faker = Faker("pt_BR")
proponent = ProponentRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_proponent():
    """Should insert Proponent"""

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

    with DBConnectionHandler() as db_connection:
        try:
            db_connection.session.add(proposal)
            db_connection.session.flush()
            db_connection.session.commit()

            new_proponent = proponent.insert_proponent(
                cnpj=cnpj,
                proposal_id=proposal.id,
                company_name=company_name,
                trade_name=trade_name,
                zip_code=zip_code,
                state=state,
                city=city,
                neighborhood=neighborhood,
                street=street,
                number=number,
                complement=complement,
                website=website,
                social_media=social_media,
                curriculum_summary=curriculum_summary,
            )

            # Select Proponent
            query = select(Proponente).where(
                Proponente.proposta_id == new_proponent.proposta_id
            )

            for query_proponent in db_connection.session.execute(query):
                assert new_proponent.cnpj == query_proponent[0].cnpj
                assert new_proponent.proposta_id == query_proponent[0].proposta_id
                assert new_proponent.razao_social == query_proponent[0].razao_social
                assert new_proponent.nome_fantasia == query_proponent[0].nome_fantasia
                assert new_proponent.endereco_cep == query_proponent[0].endereco_cep
                assert new_proponent.endereco_uf == query_proponent[0].endereco_uf
                assert (
                    new_proponent.endereco_municipio
                    == query_proponent[0].endereco_municipio
                )
                assert (
                    new_proponent.endereco_bairro == query_proponent[0].endereco_bairro
                )
                assert (
                    new_proponent.endereco_logradouro
                    == query_proponent[0].endereco_logradouro
                )
                assert (
                    new_proponent.endereco_numero == query_proponent[0].endereco_numero
                )
                assert (
                    new_proponent.endereco_complemento
                    == query_proponent[0].endereco_complemento
                )
                assert new_proponent.site == query_proponent[0].site
                assert new_proponent.rede_social == query_proponent[0].rede_social
                assert (
                    new_proponent.resumo_curriculo
                    == query_proponent[0].resumo_curriculo
                )

            # Deleting Proponent Inserted
            proponent_inserted = db_connection.session.get(
                Proponente, new_proponent.proposta_id
            )
            db_connection.session.delete(proponent_inserted)

            # Deleting Proposal Created
            proposal_inserted = db_connection.session.get(Proposta, proposal.id)
            db_connection.session.delete(proposal_inserted)

            db_connection.session.flush()
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
