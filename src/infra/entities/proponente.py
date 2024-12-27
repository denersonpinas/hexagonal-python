from typing import Optional
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UUID, ForeignKey, Integer

from src.infra.config.db_base import Base
from src.infra.entities import Proposta


@dataclass
class Proponente(Base):
    __tablename__ = "tcc_api_proponente"

    cnpj: Mapped[str] = mapped_column(String(14), nullable=False)
    proposta_id: Mapped[str] = mapped_column(
        UUID(), ForeignKey("tcc_api_proposta.id"), primary_key=True, nullable=False
    )
    razao_social: Mapped[str] = mapped_column(String(144), nullable=False)
    nome_fantasia: Mapped[Optional[str]] = mapped_column(String(55))
    endereco_cep: Mapped[Optional[str]] = mapped_column(String(8))
    endereco_uf: Mapped[Optional[str]] = mapped_column(String(2))
    endereco_municipio: Mapped[Optional[str]] = mapped_column(String(120))
    endereco_bairro: Mapped[Optional[str]] = mapped_column(String(30))
    endereco_logradouro: Mapped[Optional[str]] = mapped_column(String(100))
    endereco_numero: Mapped[Optional[int]] = mapped_column(Integer())
    endereco_complemento: Mapped[Optional[str]] = mapped_column(String(30))
    site: Mapped[Optional[str]] = mapped_column(String(250))
    rede_social: Mapped[Optional[str]] = mapped_column(String(250))
    resumo_curriculo: Mapped[Optional[str]] = mapped_column(String(1000))

    proposta: Mapped[Proposta] = relationship(back_populates="proponentes")

    historico_fornecimento = relationship(
        "HistoricoDeFornecimento", back_populates="proponente"
    )
    historico_parcerias = relationship(
        "HistoricoDeParcerias", back_populates="proponente"
    )
    representantes_legais = relationship(
        "RepresentanteLegal", back_populates="proponente"
    )
    ponto_de_contato_projeto = relationship(
        "PontoDeContatoProjeto", back_populates="proponente"
    )
    historico_projeto = relationship("HistoricoProjeto", back_populates="proponente")
