from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class Tematica(Base):
    __tablename__ = f"{REFERENCE_TABLE}_tematica"

    id = Column(Integer, primary_key=True)
    descricao = Column(String(50), nullable=False)

    id_proposta_tematica = relationship("PropostaTematica")

    def __rep__(self):
        return f"Tematica [descricao={self.descricao}]"

    def __eq__(self, other):
        if self.id == other.id and self.descricao == other.descricao:
            return True
        return False
