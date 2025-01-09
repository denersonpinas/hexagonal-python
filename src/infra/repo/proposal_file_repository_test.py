import uuid
from faker import Faker
from sqlalchemy import select
from uuid import uuid4

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_arquivo import PropostaArquivo
from src.infra.entities.proposta import Proposta
from src.infra.entities.tipo_arquivo import TipoArquivo  # Assuming this exists
from .proposal_file_repository import ProposalFileRepository

faker = Faker()
proposal_file = ProposalFileRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def generate_valid_extension():
    """Gera uma extensão de arquivo válida"""
    extensions = ["pdf", "doc", "txt", "png", "jpg", "xls", "csv"]
    return faker.random_element(elements=extensions)


def test_insert_proposal_file():
    """Should insert Proposal File"""

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

    id_type_project = str(uuid.uuid4().hex)
    constext = faker.text(max_nb_chars=32)
    description = faker.text(max_nb_chars=120)
    info = faker.text(max_nb_chars=1000)

    type_file = TipoArquivo(
        id=id_type_project,
        contexto=constext,
        descricao=description,
        info=info,
    )

    # Test data
    file_id = uuid4()
    name = faker.file_name()
    extension = generate_valid_extension()
    size = faker.random_int(min=1000, max=10000000)
    uri = faker.uri()

    with DBConnectionHandler() as db_connection:
        try:

            db_connection.session.add(proposal)
            db_connection.session.add(type_file)
            db_connection.session.flush()
            db_connection.session.commit()

            new_file = proposal_file.insert_proposal_file(
                id=file_id,
                name=name,
                extension=extension,
                size=size,
                uri=uri,
                proposal_id=proposal.id,
                type_id=str(type_file.id),
            )

            # Select Proposal File
            query = select(PropostaArquivo).where(PropostaArquivo.id == new_file.id)

            for query_file in db_connection.session.execute(query):
                assert new_file.id == query_file[0].id
                assert new_file.nome == query_file[0].nome
                assert new_file.extensao == query_file[0].extensao
                assert new_file.tamanho == query_file[0].tamanho
                assert new_file.uri == query_file[0].uri
                assert new_file.proposta_id == query_file[0].proposta_id
                assert new_file.tipo_id == query_file[0].tipo_id

            # Deleting Proposal File Inserted
            file_inserted = db_connection.session.get(PropostaArquivo, new_file.id)
            db_connection.session.delete(file_inserted)

            # Deleting File Type Created
            file_type_inserted = db_connection.session.get(TipoArquivo, type_file.id)
            db_connection.session.delete(file_type_inserted)

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
