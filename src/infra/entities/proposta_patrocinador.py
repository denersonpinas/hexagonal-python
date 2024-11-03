from sqlalchemy import UUID, Column, Numeric, String, Integer, ForeignKey
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class PropostaPatrocinador(Base):
    __tablename__ = f"{REFERENCE_TABLE}_propostapatrocinador"

    id = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    formato = Column(String(150), nullable=False)
    valor = Column(Numeric(16, 2), nullable=False)
    proposta_id = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proposta.id"))

    def __req__(self):
        return f"Patrocinador [nome={self.nome}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.nome == other.nome
            and self.formato == other.formato
            and self.valor == other.valor
        ):
            return True
        return False
