from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class RelacaoCategoriaContrapartida(Base):
    __tablename__ = f"{REFERENCE_TABLE}_relacaocategoriacontrapartida"

    id = Column(Integer, primary_key=True)
    categoria_id = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_categoriacontrapartida.id")
    )
    contrapartida_id = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_contrapartida.id")
    )

    id_abginvest_tpproj_lei_contrpart = relationship("AbginvestTpprojLeiContrpart")
