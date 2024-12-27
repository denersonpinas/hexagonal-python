from typing import Optional
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UUID, BigInteger, ForeignKey

from src.infra.config.db_base import Base
from src.infra.entities.proponente import Proponente


@dataclass
class RepresentanteLegal(Base):
    __tablename__ = "tcc_api_representantelegal"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    cargo: Mapped[str] = mapped_column(String(150), nullable=False)
    resumo: Mapped[Optional[str]] = mapped_column(String(1000))
    proposta_id: Mapped[str] = mapped_column(
        UUID(), ForeignKey("tcc_api_proponente.proposta_id"), nullable=False
    )

    proponente: Mapped[Proponente] = relationship(
        back_populates="representantes_legais"
    )
