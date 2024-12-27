from dataclasses import dataclass
from sqlalchemy import SmallInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base
from src.infra.entities.abginvest_tpproj_lei import AbginvestTpprojLei
from src.infra.entities.relacao_categoria_contrapartida import (
    RelacaoCategoriaContrapartida,
)


@dataclass
class AbginvestTpprojLeiContrpart(Base):
    __tablename__ = "tcc_api_abginvest_tpproj_lei_contrpart"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ordem: Mapped[int] = mapped_column(SmallInteger)
    abginvest_tpproj_lei_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_abginvest_tpproj_lei.id")
    )
    relacao_contrapartida_categoria_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_relacaocategoriacontrapartida.id")
    )

    relacao_categoria_contrapartida: Mapped[RelacaoCategoriaContrapartida] = (
        relationship(back_populates="abginvest_tpproj_lei_contrpart")
    )
    abginvest_tpproj_lei: Mapped[AbginvestTpprojLei] = relationship(
        back_populates="abginvest_tpproj_lei_contrpart"
    )

    proposta_contrapartida = relationship(
        "PropostaContrapartida", back_populates="abginvest_tpproj_lei_contrpart"
    )
