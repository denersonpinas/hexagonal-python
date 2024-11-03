from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class AbginvestTpprojLeiContrpart(Base):
    __tablename__ = f"{REFERENCE_TABLE}_abginvest_tpproj_lei_contrpart"

    id = Column(Integer, primary_key=True)
    ordem = Column(Integer, nullable=False)
    id_relacao_contrapartida_categoria = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_relacaocategoriacontrapartida.id")
    )
    id_abginvest_tpproj_lei = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_abginvest_tpproj_lei.id")
    )

    id_proposta_contrapartida = relationship("PropostaContrapartida")
