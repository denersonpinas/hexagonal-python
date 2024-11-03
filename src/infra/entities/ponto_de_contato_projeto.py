from sqlalchemy import UUID, Column, ForeignKey, String, Integer
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class PontoDeContatoProjeto(Base):
    __tablename__ = f"{REFERENCE_TABLE}_pontodecontatoprojeto"

    id = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    cargo = Column(String(150), nullable=False)
    id_proposta = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proponente.proposta_id"))

    def __rep__(self):
        return f"Ponto de Contato [nome={self.nome}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.nome == other.nome
            and self.email == other.email
            and self.cargo == other.cargo
        ):
            return True
        return False
