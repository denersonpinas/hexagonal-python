from sqlalchemy import UUID, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class PropostaAbginvestTpprojLei(Base):
    __tablename__ = f"{REFERENCE_TABLE}_proposta_abginvest_tpproj_lei"

    id = Column(UUID, primary_key=True)
    abginvest_tpproj_lei = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_abginvest_tpproj_lei.id")
    )
    proposta_id = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proposta.id"))

    id_proposta_contrapartida = relationship("PropostaContrapartida")
