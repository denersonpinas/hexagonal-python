from dataclasses import dataclass
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base
from src.infra.entities.municipio import Municipio


@dataclass
class Bairro(Base):
    __tablename__ = "tcc_api_bairro"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    cidade_id_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_municipio.id"), nullable=False
    )

    logradouro = relationship("Logradouro", back_populates="bairro")

    municipio: Mapped[Municipio] = relationship(back_populates="bairro")
