from dataclasses import dataclass
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base
from src.infra.entities.historico_projeto import HistoricoProjeto


@dataclass
class HistoricoDeMetas(Base):
    __tablename__ = "tcc_api_historicodemetas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    previsto: Mapped[str] = mapped_column(String(144))
    alcancado: Mapped[str] = mapped_column(String(144))
    historico_projetos_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_historicoprojeto.id")
    )

    historico_projeto: Mapped[HistoricoProjeto] = relationship(
        back_populates="historico_metas"
    )
