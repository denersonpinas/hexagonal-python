import uuid
from faker import Faker
from sqlalchemy import select

from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.categorizacao_beneficiario import CategorizacaoBeneficiario
from src.infra.entities.proposta import Proposta
from src.infra.entities.proposta_beneficiario import PropostaBeneficiario
from src.infra.entities.proposta_beneficiario_categorizacao import (
    PropostaBeneficiarioCategorizacao,
)
from src.infra.entities.tipo_categorizacao_beneficiario import (
    TipoCategorizacaoBeneficiario,
)
from .proposal_beneficiary_categorization_repository import (
    ProposalBeneficiaryCategorizationRepository,
)

faker = Faker()
proposal_beneficiary_catego = ProposalBeneficiaryCategorizationRepository()
db_connection_handler = DBConnectionHandler()
engine = db_connection_handler.get_engine()


def test_insert_proposal_beneficiary_categorization():
    """Should insert Proposal Beneficiary"""

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

    id_type_caracterization = str(uuid.uuid4().hex)
    description = faker.text(max_nb_chars=50)
    info = faker.text(max_nb_chars=150)
    type_caracterization = TipoCategorizacaoBeneficiario(
        id=id_type_caracterization, info=info, descricao=description
    )

    valor = faker.text(max_nb_chars=64)

    quantidade_proposal = faker.random_int(min=1, max=100)
    id_proposal_ben = str(uuid.uuid4().hex)

    with DBConnectionHandler() as db_connection:
        try:
            # Add Proposal for test
            db_connection.session.add(proposal)
            db_connection.session.add(type_caracterization)

            caracterization = CategorizacaoBeneficiario(
                valor=valor, tipo_id=type_caracterization.id
            )

            proposal_beneficiary = PropostaBeneficiario(
                id=id_proposal_ben,
                quantidade=quantidade_proposal,
                proposta_id=proposal.id,
            )

            db_connection.session.add(caracterization)
            db_connection.session.add(proposal_beneficiary)
            db_connection.session.flush()
            db_connection.session.commit()

            new_proposal_beneficiary_categorization = (
                proposal_beneficiary_catego.insert_proposal_beneficiary_categorization(
                    categorizacao_id=caracterization.id,
                    proposta_beneficiario_id=proposal_beneficiary.id,
                )
            )

            # Select Proposal Beneficiary Categorization
            query = select(PropostaBeneficiarioCategorizacao).where(
                PropostaBeneficiarioCategorizacao.id
                == new_proposal_beneficiary_categorization.id
            )

            for (
                query_proposal_beneficiary_categorization
            ) in db_connection.session.execute(query):
                assert (
                    new_proposal_beneficiary_categorization.id
                    == query_proposal_beneficiary_categorization[0].id
                )
                assert (
                    new_proposal_beneficiary_categorization.categorizacao_id
                    == query_proposal_beneficiary_categorization[0].categorizacao_id
                )
                assert (
                    new_proposal_beneficiary_categorization.proposta_beneficiario_id
                    == query_proposal_beneficiary_categorization[
                        0
                    ].proposta_beneficiario_id
                )

            # Deleting Inserted Data
            categorization_inserted = db_connection.session.get(
                PropostaBeneficiarioCategorizacao,
                new_proposal_beneficiary_categorization.id,
            )
            proposal_beneficiario_inserted = db_connection.session.get(
                PropostaBeneficiario, proposal_beneficiary.id
            )
            caracterization_inserted = db_connection.session.get(
                CategorizacaoBeneficiario, caracterization.id
            )
            caracterization_type_inserted = db_connection.session.get(
                TipoCategorizacaoBeneficiario, type_caracterization.id
            )
            proposal_inserted = db_connection.session.get(Proposta, proposal.id)
            db_connection.session.delete(categorization_inserted)
            db_connection.session.delete(proposal_beneficiario_inserted)
            db_connection.session.delete(caracterization_inserted)
            db_connection.session.delete(caracterization_type_inserted)
            db_connection.session.delete(proposal_inserted)
            db_connection.session.flush()
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
