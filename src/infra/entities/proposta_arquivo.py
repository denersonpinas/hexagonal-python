from dataclasses import dataclass
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

from src.infra.config.db_base import Base
from src.infra.entities.proposta import Proposta
from src.infra.entities.tipo_arquivo import TipoArquivo


@dataclass
class PropostaArquivo(Base):
    __tablename__ = "tcc_api_propostaarquivo"

    id: Mapped[UUID] = mapped_column(primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(255), nullable=False)
    extensao: Mapped[str] = mapped_column(String(4), nullable=False)
    tamanho: Mapped[int] = mapped_column(
        Integer, nullable=False, comment="Tamanho do arquivo em bytes"
    )
    uri: Mapped[str] = mapped_column(String(200), nullable=False)
    proposta_id: Mapped[UUID] = mapped_column(
        ForeignKey("tcc_api_proposta.id"), nullable=False
    )
    tipo_id: Mapped[str] = mapped_column(
        ForeignKey("tcc_api_tipoarquivo.id"), nullable=False
    )

    proposta: Mapped[Proposta] = relationship(back_populates="proposta_arquivo")
    tipo: Mapped[TipoArquivo] = relationship(back_populates="proposta_arquivo")
