from dataclasses import dataclass
from sqlalchemy import String, SmallInteger, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base
from src.infra.entities.proponente import Proponente


@dataclass
class HistoricoProjeto(Base):
    __tablename__ = "tcc_api_historicoprojeto"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ano_investimento: Mapped[int] = mapped_column(SmallInteger)
    titulo: Mapped[str] = mapped_column(String(150))
    tipo_investimento: Mapped[str] = mapped_column(String(16))
    proposta_id: Mapped[UUID] = mapped_column(
        ForeignKey("tcc_api_proponente.proposta_id")
    )

    proponente: Mapped[Proponente] = relationship(back_populates="historico_projeto")

    historico_metas = relationship(
        "HistoricoDeMetas", back_populates="historico_projeto"
    )
