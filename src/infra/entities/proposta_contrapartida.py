from dataclasses import dataclass
from typing import Optional
from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

from src.infra.config.db_base import Base
from src.infra.entities.abginvest_tpproj_lei_contrpart import (
    AbginvestTpprojLeiContrpart,
)
from src.infra.entities.proposta_abginvest_tpproj_lei import PropostaAbginvestTpprojLei


@dataclass
class PropostaContrapartida(Base):
    __tablename__ = "tcc_api_propostacontrapartida"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(String(250))
    quantitativo: Mapped[int] = mapped_column(Integer)
    previsto: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    abginvest_tpproj_lei_contrpart_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_abginvest_tpproj_lei_contrpart.id")
    )
    proposta_abginvest_tpproj_lei_id: Mapped[UUID] = mapped_column(
        ForeignKey("tcc_api_proposta_abginvest_tpproj_lei.id")
    )

    proposta_abginvest_tpproj_lei: Mapped[PropostaAbginvestTpprojLei] = relationship(
        back_populates="proposta_contrapartida"
    )
    abginvest_tpproj_lei_contrpart: Mapped[AbginvestTpprojLeiContrpart] = relationship(
        back_populates="proposta_contrapartida"
    )
