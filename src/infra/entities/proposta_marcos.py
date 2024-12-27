from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, UUID, BigInteger, ForeignKey

from src.infra.config.db_base import Base
from .proposta import Proposta


@dataclass
class PropostaMarcos(Base):
    __tablename__ = "tcc_api_propostamarcos"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    descricao: Mapped[str] = mapped_column(String(200), nullable=False)
    execucao: Mapped[str] = mapped_column(Date(), nullable=False)
    proposta_id: Mapped[str] = mapped_column(
        UUID(), ForeignKey("tcc_api_proposta.id"), nullable=False
    )

    proposta: Mapped[Proposta] = relationship(back_populates="propostas_marcos")
