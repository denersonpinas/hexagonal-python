from dataclasses import dataclass
from sqlalchemy import BigInteger, SmallInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid

from src.infra.config.db_base import Base
from src.infra.entities.municipio import Municipio
from src.infra.entities.proposta import Proposta


@dataclass
class PropostaLocalExecucao(Base):
    __tablename__ = "tcc_api_propostalocalexececao"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    municipio_id: Mapped[int] = mapped_column(
        SmallInteger, ForeignKey("tcc_api_municipio.id"), nullable=False
    )
    proposta_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tcc_api_proposta.id"), nullable=False
    )

    municipio: Mapped[Municipio] = relationship(
        back_populates="proposta_local_exececao"
    )
    proposta: Mapped[Proposta] = relationship(back_populates="proposta_local_exececao")
