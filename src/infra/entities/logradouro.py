from dataclasses import dataclass
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base
from src.infra.entities.bairro import Bairro


@dataclass
class Logradouro(Base):
    __tablename__ = "tcc_api_logradouro"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    bairro_id_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_bairro.id"), nullable=False
    )

    bairro: Mapped[Bairro] = relationship(back_populates="logradouro")
