from dataclasses import dataclass
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

from src.infra.config.db_base import Base
from src.infra.entities.abginvest_tpproj_lei import AbginvestTpprojLei
from src.infra.entities.proposta import Proposta


@dataclass
class PropostaAbginvestTpprojLei(Base):
    __tablename__ = "tcc_api_proposta_abginvest_tpproj_lei"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    abginvest_tpproj_lei_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_abginvest_tpproj_lei.id")
    )
    proposta_id: Mapped[UUID] = mapped_column(ForeignKey("tcc_api_proposta.id"))

    abginvest_tpproj_lei: Mapped[AbginvestTpprojLei] = relationship(
        back_populates="proposta_abginvest_tpproj_lei"
    )
    proposta: Mapped[Proposta] = relationship(
        back_populates="proposta_abginvest_tpproj_lei"
    )

    proposta_contrapartida = relationship(
        "PropostaContrapartida", back_populates="proposta_abginvest_tpproj_lei"
    )
