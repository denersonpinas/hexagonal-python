from dataclasses import dataclass
from sqlalchemy import ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

from src.infra.config.db_base import Base
from src.infra.entities.proposta import Proposta


@dataclass
class PropostaMeta(Base):
    __tablename__ = "tcc_api_propostameta"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    ordem: Mapped[int] = mapped_column(SmallInteger)
    meta: Mapped[str] = mapped_column(String(120), nullable=False)
    quantitativo: Mapped[int] = mapped_column(Integer, nullable=False)
    proposta_id: Mapped[UUID] = mapped_column(
        ForeignKey("tcc_api_proposta.id"), nullable=False
    )

    proposta: Mapped[Proposta] = relationship(back_populates="proposta_meta")
