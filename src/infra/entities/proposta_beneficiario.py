from dataclasses import dataclass
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

from src.infra.config.db_base import Base
from src.infra.entities.proposta import Proposta


@dataclass
class PropostaBeneficiario(Base):
    __tablename__ = "tcc_api_propostabeneficiario"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    quantidade: Mapped[int] = mapped_column(Integer)
    proposta_id: Mapped[UUID] = mapped_column(ForeignKey("tcc_api_proposta.id"))

    proposta: Mapped[Proposta] = relationship(back_populates="proposta_beneficiario")

    proposta_beneficiario_categorizacao = relationship(
        "PropostaBeneficiarioCategorizacao", back_populates="proposta_beneficiario"
    )
