from sqlalchemy import UUID, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class PropostaBeneficiario(Base):
    __tablename__ = f"{REFERENCE_TABLE}_propostabeneficiario"

    id = Column(UUID, primary_key=True)
    quantidade = Column(Integer, nullable=False)
    proposta_id = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proposta.id"))

    id_proposta_beneficiario_categorizacao = relationship(
        "PropostaBeneficiarioCategorizacao"
    )

    def __rep__(self):
        return f"Proposta Beneficiario [quantidade={self.quantidade}]"

    def __eq__(self, other):
        if self.id == other.id and self.quantidade == other.quantidade:
            return True
        return False
