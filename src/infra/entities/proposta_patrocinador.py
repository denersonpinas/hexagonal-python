from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, UUID, BigInteger, ForeignKey

from src.infra.config.db_base import Base
from src.infra.entities import Proposta


@dataclass
class PropostaPatrocinador(Base):
    __tablename__ = "tcc_api_propostapatrocinador"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    formato: Mapped[str] = mapped_column(String(150), nullable=False)
    valor: Mapped[float] = mapped_column(Numeric(16, 2), nullable=False)
    proposta_id: Mapped[str] = mapped_column(
        UUID(), ForeignKey("tcc_api_proposta.id"), nullable=False
    )

    proposta: Mapped[Proposta] = relationship(back_populates="propostas_patrocinadores")
