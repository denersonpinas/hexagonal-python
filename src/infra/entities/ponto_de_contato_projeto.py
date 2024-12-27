from dataclasses import dataclass
from sqlalchemy import String, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base
from src.infra.entities.proponente import Proponente


@dataclass
class PontoDeContatoProjeto(Base):
    __tablename__ = "tcc_api_pontodecontatoprojeto"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(150))
    cargo: Mapped[str] = mapped_column(String(150))
    proposta_id: Mapped[UUID] = mapped_column(
        ForeignKey("tcc_api_proponente.proposta_id")
    )

    proponente: Mapped[Proponente] = relationship(
        back_populates="ponto_de_contato_projeto"
    )
