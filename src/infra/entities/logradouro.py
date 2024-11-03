from sqlalchemy import Column, ForeignKey, String, Integer
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class Logradouro(Base):
    __tablename__ = f"{REFERENCE_TABLE}_logradouro"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    bairro_id = Column(Integer, ForeignKey(f"{REFERENCE_TABLE}_bairro.id"))

    def __rep__(self):
        return f"Lodradouro [nome={self.nome}]"

    def __eq__(self, other):
        if self.id == other.id and self.nome == other.nome:
            return True
        return False
