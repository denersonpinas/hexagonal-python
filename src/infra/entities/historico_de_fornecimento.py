from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UUID, BigInteger, ForeignKey

from src.infra.entities.proponente import Proponente
from src.infra.config.db_base import Base


@dataclass
class HistoricoDeFornecimento(Base):
    __tablename__ = "tcc_api_historicodefornecimento"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    servico_prestado: Mapped[str] = mapped_column(String(250))
    responsavel_contratacao: Mapped[str] = mapped_column(String(250))
    proposta_id: Mapped[str] = mapped_column(
        UUID(), ForeignKey("tcc_api_proponente.proposta_id"), nullable=False
    )

    proponente: Mapped[Proponente] = relationship(
        back_populates="historico_fornecimento"
    )
