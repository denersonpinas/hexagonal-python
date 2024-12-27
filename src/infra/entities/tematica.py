from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, SmallInteger

from src.infra.config.db_base import Base


@dataclass
class Tematica(Base):
    __tablename__ = "tcc_api_tematica"

    id: Mapped[int] = mapped_column(SmallInteger(), primary_key=True)
    descricao: Mapped[str] = mapped_column(String(50), nullable=False)

    propostas_tematica = relationship("PropostaTematica", back_populates="tematica")
