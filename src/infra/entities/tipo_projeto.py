from dataclasses import dataclass
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base


@dataclass
class TipoProjeto(Base):
    __tablename__ = "tcc_api_tipoprojeto"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    descricao: Mapped[str] = mapped_column(String(250))

    abginvest_tpproj_lei = relationship(
        "AbginvestTpprojLei", back_populates="tipo_projeto"
    )
