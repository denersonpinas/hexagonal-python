from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import SmallInteger, String

from src.infra.config.db_base import Base


@dataclass
class Lei(Base):
    __tablename__ = "tcc_api_lei"

    id: Mapped[int] = mapped_column(SmallInteger(), primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(250), nullable=False)

    abginvest_tpproj_lei = relationship("AbginvestTpprojLei", back_populates="lei")
