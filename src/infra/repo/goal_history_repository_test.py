import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.historico_de_metas import HistoricoDeMetas
from src.infra.entities.historico_projeto import HistoricoProjeto
from src.infra.entities.proponente import Proponente
from src.infra.entities.proposta import Proposta
from .goal_history_repository import GoalHistoryRepository

faker = Faker("pt_BR")
goal_history = GoalHistoryRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_goal_history():
    """Should insert Goal History"""

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

    # History Project data test
    investment_year = faker.random_int(min=2000, max=2023)
    title = faker.sentence()
    investment_type = faker.random_element(
        elements=("Patrocínio", "Investimento", "Doação")
    )

    # Test data
    expected = faker.text(max_nb_chars=144)
    achieved = faker.text(max_nb_chars=144)

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

            history = HistoricoProjeto(
                ano_investimento=investment_year,
                titulo=title,
                tipo_investimento=investment_type,
                proposta_id=proponent.proposta_id,
            )

            db_connection.session.add(history)
            db_connection.session.flush()
            db_connection.session.commit()

            new_goal = goal_history.insert_goal_history(
                expected=expected, achieved=achieved, project_history_id=history.id
            )

            # Select Goal History
            query = select(HistoricoDeMetas).where(HistoricoDeMetas.id == new_goal.id)

            for query_goal in db_connection.session.execute(query):
                assert new_goal.id == query_goal[0].id
                assert new_goal.previsto == query_goal[0].previsto
                assert new_goal.alcancado == query_goal[0].alcancado
                assert (
                    new_goal.historico_projetos_id
                    == query_goal[0].historico_projetos_id
                )

            # Deleting Goal History Inserted
            goal_inserted = db_connection.session.get(HistoricoDeMetas, new_goal.id)
            db_connection.session.delete(goal_inserted)

            # Deleting Project History Created
            project_history_inserted = db_connection.session.get(
                HistoricoProjeto, history.id
            )
            db_connection.session.delete(project_history_inserted)

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
