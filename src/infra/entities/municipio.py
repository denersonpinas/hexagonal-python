from dataclasses import dataclass
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base


@dataclass
class Municipio(Base):
    __tablename__ = "tcc_api_municipio"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    uf: Mapped[str] = mapped_column(String(2), nullable=False)

    bairro = relationship("Bairro", back_populates="municipio")
    proposta_local_exececao = relationship(
        "PropostaLocalExecucao", back_populates="municipio"
    )
