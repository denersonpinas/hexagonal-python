from dataclasses import dataclass
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.infra.config.db_base import Base
from src.infra.entities.tipo_categorizacao_beneficiario import (
    TipoCategorizacaoBeneficiario,
)


@dataclass
class CategorizacaoBeneficiario(Base):
    __tablename__ = "tcc_api_categorizacaobeneficiario"

    id: Mapped[int] = mapped_column(primary_key=True)
    valor: Mapped[str] = mapped_column(String(64))
    tipo_id: Mapped[str] = mapped_column(
        ForeignKey("tcc_api_tipocategorizacaobeneficiario.id")
    )

    tipo_categorizacao_beneficiario: Mapped[TipoCategorizacaoBeneficiario] = (
        relationship(back_populates="categorizacao_beneficiario")
    )

    proposta_beneficiario_categorizacao = relationship(
        "PropostaBeneficiarioCategorizacao", back_populates="categorizacao_beneficiario"
    )
