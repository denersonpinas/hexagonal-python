from typing import Optional
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, Date, UUID

from src.infra.config.db_base import Base


@dataclass
class Proposta(Base):
    __tablename__ = "tcc_api_proposta"

    id: Mapped[str] = mapped_column(UUID(), primary_key=True)
    titulo_projeto: Mapped[str] = mapped_column(String(250), nullable=False)
    resumo_projeto: Mapped[str] = mapped_column(String(500), nullable=False)
    descricao_projeto: Mapped[str] = mapped_column(String(1000), nullable=False)
    dados_bancario_instituicao: Mapped[str] = mapped_column(String(250), nullable=False)
    dados_bancario_agencia_conta_bancaria: Mapped[str] = mapped_column(
        String(250), nullable=False
    )
    dados_bancario_conta_corrente: Mapped[str] = mapped_column(
        String(250), nullable=False
    )
    dados_bancario_cnpj_fundo: Mapped[Optional[str]] = mapped_column(String(14))
    dados_bancario_razao_social_fundo: Mapped[Optional[str]] = mapped_column(
        String(250)
    )
    dados_bancario_contato_fundo_nome: Mapped[Optional[str]] = mapped_column(
        String(250)
    )
    dados_bancario_contato_fundo_email: Mapped[Optional[str]] = mapped_column(
        String(150)
    )
    valor_total_projeto: Mapped[float] = mapped_column(Numeric(16, 2), nullable=False)
    valor_total_lei_incentivo: Mapped[float] = mapped_column(
        Numeric(16, 2), nullable=False
    )
    valor_total_captado: Mapped[float] = mapped_column(Numeric(16, 2), nullable=False)
    valor_total_captado_lei_incentivo: Mapped[float] = mapped_column(
        Numeric(16, 2), nullable=False
    )
    valor_total_incentivado_nubank: Mapped[float] = mapped_column(
        Numeric(16, 2), nullable=False
    )
    observacoes: Mapped[str] = mapped_column(String(250), nullable=False)
    data_inicio_projeto: Mapped[str] = mapped_column(Date(), nullable=False)
    data_fim_projeto: Mapped[str] = mapped_column(Date(), nullable=False)

    propostas_marcos = relationship("PropostaMarcos", back_populates="proposta")
    propostas_tematica = relationship("PropostaTematica", back_populates="proposta")
    propostas_patrocinadores = relationship(
        "PropostaPatrocinador", back_populates="proposta"
    )
    proponentes = relationship("Proponente", back_populates="proposta")
    proposta_abginvest_tpproj_lei = relationship(
        "PropostaAbginvestTpprojLei", back_populates="proposta"
    )
    proposta_beneficiario = relationship(
        "PropostaBeneficiario", back_populates="proposta"
    )
    proposta_arquivo = relationship("PropostaArquivo", back_populates="proposta")
    proposta_meta = relationship("PropostaMeta", back_populates="proposta")
    proposta_local_exececao = relationship(
        "PropostaLocalExecucao", back_populates="proposta"
    )
