from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class CategorizacaoBeneficiario(Base):
    __tablename__ = f"{REFERENCE_TABLE}_categorizacaobeneficiario"

    id = Column(Integer, primary_key=True)
    valor = Column(String(64), nullable=False)
    tipo_id = Column(
        String(32), ForeignKey(f"{REFERENCE_TABLE}_tipocategorizacaobeneficiario.id")
    )

    id_proposta_beneficiario_caracterizacao = relationship(
        "PropostaBeneficiarioCategorizacao"
    )

    def __rep__(self):
        return f"Categorização Beneficiario [valor={self.valor}]"

    def __eq__(self, other):
        if self.id == other.id and self.valor == other.valor:
            return True
        return False
