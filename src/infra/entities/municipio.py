from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class Municipio(Base):
    __tablename__ = f"{REFERENCE_TABLE}_municipio"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    uf = Column(String(2), nullable=False)

    id_bairro = relationship("Bairro")
    id_proposta_local_execucao = relationship("PropostaLocalExecucao")

    def __rep__(self):
        return f"Municipio [nome={self.nome}]"

    def __eq__(self, other):
        if self.id == other.id and self.nome == other.nome and self.uf == other.uf:
            return True
        return False
