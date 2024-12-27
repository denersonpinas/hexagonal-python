from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UUID, SmallInteger, BigInteger, ForeignKey

from src.infra.config.db_base import Base
from src.infra.entities import Proposta, Tematica


@dataclass
class PropostaTematica(Base):
    __tablename__ = "tcc_api_propostatematica"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    proposta_id: Mapped[str] = mapped_column(
        UUID(), ForeignKey("tcc_api_proposta.id"), nullable=False
    )
    tematica_id: Mapped[int] = mapped_column(
        SmallInteger(), ForeignKey("tcc_api_tematica.id"), nullable=False
    )

    proposta: Mapped[Proposta] = relationship(back_populates="propostas_tematica")
    tematica: Mapped[Tematica] = relationship(back_populates="propostas_tematica")
