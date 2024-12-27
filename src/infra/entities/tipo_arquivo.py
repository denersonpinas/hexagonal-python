from dataclasses import dataclass
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base


@dataclass
class TipoArquivo(Base):
    __tablename__ = "tcc_api_tipoarquivo"

    id: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    contexto: Mapped[str] = mapped_column(String(32), nullable=False)
    descricao: Mapped[str] = mapped_column(String(120), nullable=False)
    info: Mapped[str] = mapped_column(String(1000), nullable=False)

    proposta_arquivo = relationship("PropostaArquivo", back_populates="tipo")
