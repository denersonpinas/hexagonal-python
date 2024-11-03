from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class Bairro(Base):
    __tablename__ = f"{REFERENCE_TABLE}_bairro"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    municipio_id = Column(Integer, ForeignKey(f"{REFERENCE_TABLE}_municipio.id"))

    id_logradouro = relationship("Logradouro")

    def __rep__(self):
        return f"Bairro [nome={self.nome}]"

    def __eq__(self, other):
        if self.id == other.id and self.nome == other.nome:
            return True
        return False
