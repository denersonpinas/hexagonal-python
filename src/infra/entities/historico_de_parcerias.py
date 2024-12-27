from typing import Optional
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UUID, BigInteger, ForeignKey, Integer

from src.infra.config.db_base import Base
from src.infra.entities.proponente import Proponente


@dataclass
class HistoricoDeParcerias(Base):
    __tablename__ = "tcc_api_historicodeparcerias"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    numero_de_patrocinadores: Mapped[int] = mapped_column(Integer())
    numero_de_renovacao: Mapped[int] = mapped_column(Integer())
    informacoes_adicionais: Mapped[Optional[str]] = mapped_column(String(250))
    proposta_id: Mapped[str] = mapped_column(
        UUID(), ForeignKey("tcc_api_proponente.proposta_id"), nullable=False
    )

    proponente: Mapped[Proponente] = relationship(back_populates="historico_parcerias")
