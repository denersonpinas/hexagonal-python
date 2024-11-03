from sqlalchemy import UUID, Column, ForeignKey, Integer
from src.constants.reference import REFERENCE_TABLE
from src.infra import Base


class PropostaTematica(Base):
    __tablename__ = f"{REFERENCE_TABLE}_propostatematica"

    id = Column(Integer, primary_key=True)
    tematica_id = Column(Integer, ForeignKey(f"{REFERENCE_TABLE}_tematica.id"))
    proposta_id = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proposta.id"))
