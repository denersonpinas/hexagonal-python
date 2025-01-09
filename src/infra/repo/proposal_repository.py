from typing import Optional
from uuid import UUID
from src.data.interface.proposal_repository_interface import ProposalRepositoryInterface
from src.domain.models import Proposal
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta import Proposta


class ProposalRepository(ProposalRepositoryInterface):
    """Class to manage Proposal Repository"""

    @classmethod
    def insert_proposal(
        cls,
        id: UUID,
        titulo_projeto: str,
        resumo_projeto: str,
        descricao_projeto: str,
        dados_bancario_instituicao: str,
        dados_bancario_agencia_conta_bancaria: str,
        dados_bancario_conta_corrente: str,
        dados_bancario_cnpj_fundo: Optional[str] = None,
        dados_bancario_razao_social_fundo: Optional[str] = None,
        dados_bancario_contato_fundo_nome: Optional[str] = None,
        dados_bancario_contato_fundo_email: Optional[str] = None,
        valor_total_projeto: float = 0.0,
        valor_total_lei_incentivo: float = 0.0,
        valor_total_captado: float = 0.0,
        valor_total_captado_lei_incentivo: float = 0.0,
        valor_total_incentivado_nubank: float = 0.0,
        observacoes: str = "",
        data_inicio_projeto: str = "",
        data_fim_projeto: str = "",
    ) -> Proposal:
        """Insert data in proposal entity
        :param  -   id: project id
                -   titulo_projeto: project title
                -   resumo_projeto: project summary
                -   descricao_projeto: project description
                -   dados_bancario_instituicao: bank institution
                -   dados_bancario_agencia_conta_bancaria: agency and account
                -   dados_bancario_conta_corrente: current account
                -   dados_bancario_cnpj_fundo: fund CNPJ (optional)
                -   dados_bancario_razao_social_fundo: fund legal name (optional)
                -   dados_bancario_contato_fundo_nome: fund contact name (optional)
                -   dados_bancario_contato_fundo_email: fund contact email (optional)
                -   valor_total_projeto: total project value
                -   valor_total_lei_incentivo: total incentive law value
                -   valor_total_captado: total captured value
                -   valor_total_captado_lei_incentivo: total captured incentive value
                -   valor_total_incentivado_nubank: total Nubank incentive value
                -   observacoes: observations
                -   data_inicio_projeto: project start date
                -   data_fim_projeto: project end date
        :return -   tuple with proposal inserted
        """
        with DBConnectionHandler() as db_connection:
            try:
                new_proposal = Proposta(
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
                db_connection.session.add(new_proposal)
                db_connection.session.flush()
                db_connection.session.commit()

                return Proposal(
                    id=new_proposal.id,
                    titulo_projeto=new_proposal.titulo_projeto,
                    resumo_projeto=new_proposal.resumo_projeto,
                    descricao_projeto=new_proposal.descricao_projeto,
                    dados_bancario_instituicao=new_proposal.dados_bancario_instituicao,
                    dados_bancario_agencia_conta_bancaria=new_proposal.dados_bancario_agencia_conta_bancaria,
                    dados_bancario_conta_corrente=new_proposal.dados_bancario_conta_corrente,
                    dados_bancario_cnpj_fundo=new_proposal.dados_bancario_cnpj_fundo,
                    dados_bancario_razao_social_fundo=new_proposal.dados_bancario_razao_social_fundo,
                    dados_bancario_contato_fundo_nome=new_proposal.dados_bancario_contato_fundo_nome,
                    dados_bancario_contato_fundo_email=new_proposal.dados_bancario_contato_fundo_email,
                    valor_total_projeto=new_proposal.valor_total_projeto,
                    valor_total_lei_incentivo=new_proposal.valor_total_lei_incentivo,
                    valor_total_captado=new_proposal.valor_total_captado,
                    valor_total_captado_lei_incentivo=new_proposal.valor_total_captado_lei_incentivo,
                    valor_total_incentivado_nubank=new_proposal.valor_total_incentivado_nubank,
                    observacoes=new_proposal.observacoes,
                    data_inicio_projeto=new_proposal.data_inicio_projeto,
                    data_fim_projeto=new_proposal.data_fim_projeto,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
