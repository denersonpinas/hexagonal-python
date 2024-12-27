from dataclasses import dataclass
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from src.infra.config.db_base import Base


@dataclass
class CategoriaContrapartida(Base):
    __tablename__ = "tcc_api_categoriacontrapartida"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(120))
    descricao: Mapped[str] = mapped_column(String(500))
    subcategoria_de_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("tcc_api_categoriacontrapartida.id")
    )

    subcategoria_de: Mapped["CategoriaContrapartida"] = relationship(
        "CategoriaContrapartida", remote_side=[id]
    )

    relacao_categoria_contrapartida = relationship(
        "RelacaoCategoriaContrapartida", back_populates="categoria"
    )
