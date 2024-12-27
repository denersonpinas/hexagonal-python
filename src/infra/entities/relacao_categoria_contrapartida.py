from dataclasses import dataclass
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base
from src.infra.entities.categoria_contrapartida import CategoriaContrapartida
from src.infra.entities.contrapartida import Contrapartida


@dataclass
class RelacaoCategoriaContrapartida(Base):
    __tablename__ = "tcc_api_relacaocategoriacontrapartida"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    categoria_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_categoriacontrapartida.id")
    )
    contrapartida_id: Mapped[int] = mapped_column(
        ForeignKey("tcc_api_contrapartida.id")
    )

    categoria: Mapped[CategoriaContrapartida] = relationship(
        back_populates="relacao_categoria_contrapartida"
    )
    contrapartida: Mapped[Contrapartida] = relationship(
        back_populates="relacao_categoria_contrapartida"
    )

    abginvest_tpproj_lei_contrpart = relationship(
        "AbginvestTpprojLeiContrpart", back_populates="relacao_categoria_contrapartida"
    )
