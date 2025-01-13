from dataclasses import dataclass
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base
from src.infra.entities.abordagem_investimento import AbordagemInvestimento
from src.infra.entities.lei import Lei
from src.infra.entities.tipo_projeto import TipoProjeto


@dataclass
class AbginvestTpprojLei(Base):
    __tablename__ = "tcc_api_abginvest_tpproj_lei"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    abordagem_investimento_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_abordageminvestimento.id")
    )
    lei_id: Mapped[int] = mapped_column(ForeignKey("tcc_api_lei.id"), nullable=True)
    tipo_pojeto_id: Mapped[int] = mapped_column(ForeignKey("tcc_api_tipoprojeto.id"))

    tipo_projeto: Mapped[TipoProjeto] = relationship(
        back_populates="abginvest_tpproj_lei"
    )
    abordagem_investimento: Mapped[AbordagemInvestimento] = relationship(
        back_populates="abginvest_tpproj_lei"
    )
    lei: Mapped[Lei] = relationship(back_populates="abginvest_tpproj_lei")

    abginvest_tpproj_lei_contrpart = relationship(
        "AbginvestTpprojLeiContrpart", back_populates="abginvest_tpproj_lei"
    )
    proposta_abginvest_tpproj_lei = relationship(
        "PropostaAbginvestTpprojLei", back_populates="abginvest_tpproj_lei"
    )
