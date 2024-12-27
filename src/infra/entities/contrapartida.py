from dataclasses import dataclass
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base


@dataclass
class Contrapartida(Base):
    __tablename__ = "tcc_api_contrapartida"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descricao: Mapped[str] = mapped_column(String(500))
    exemplo_aplicabilidade: Mapped[str] = mapped_column(String(500))
    obrigatoria: Mapped[bool] = mapped_column(Boolean)
    padrao: Mapped[bool] = mapped_column(Boolean)

    relacao_categoria_contrapartida = relationship(
        "RelacaoCategoriaContrapartida", back_populates="contrapartida"
    )
