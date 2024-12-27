from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from uuid import UUID

from src.infra.config.db_base import Base
from src.infra.entities.categorizacao_beneficiario import CategorizacaoBeneficiario
from src.infra.entities.proposta_beneficiario import PropostaBeneficiario


@dataclass
class PropostaBeneficiarioCategorizacao(Base):
    __tablename__ = "tcc_api_propostabeneficiariocategorizacao"

    id: Mapped[int] = mapped_column(primary_key=True)
    categorizacao_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_categorizacaobeneficiario.id")
    )
    proposta_beneficiario_id: Mapped[UUID] = mapped_column(
        ForeignKey("tcc_api_propostabeneficiario.id")
    )

    categorizacao_beneficiario: Mapped[CategorizacaoBeneficiario] = relationship(
        back_populates="proposta_beneficiario_categorizacao"
    )
    proposta_beneficiario: Mapped[PropostaBeneficiario] = relationship(
        back_populates="proposta_beneficiario_categorizacao"
    )
