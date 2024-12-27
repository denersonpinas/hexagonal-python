from dataclasses import dataclass
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base


@dataclass
class AbordagemInvestimento(Base):
    __tablename__ = "tcc_api_abordageminvestimento"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descricao: Mapped[str] = mapped_column(String(80))
    incentivado: Mapped[bool] = mapped_column(Boolean)

    abginvest_tpproj_lei = relationship(
        "AbginvestTpprojLei", back_populates="abordagem_investimento"
    )
