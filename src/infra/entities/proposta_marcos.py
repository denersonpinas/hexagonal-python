from sqlalchemy import UUID, Column, Date, String, Integer, ForeignKey
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class PropostaMarcos(Base):
    __tablename__ = f"{REFERENCE_TABLE}_propostamarcos"

    id = Column(Integer, primary_key=True)
    descricao = Column(String(200), nullable=False)
    execucao = Column(Date, nullable=False)
    proposta_id = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proposta.id"))

    def __req__(self):
        return f"Marcos [descricao={self.descricao}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.descricao == other.descricao
            and self.execucao == other.execucao
        ):
            return True
        return False
