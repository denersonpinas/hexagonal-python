from sqlalchemy import UUID, Column, Integer, ForeignKey
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class PropostaBeneficiarioCategorizacao(Base):
    __tablename__ = f"{REFERENCE_TABLE}_propostabeneficiariocategorizacao"

    id = Column(Integer, primary_key=True)
    categorizacao_id = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_categorizacaobeneficiario.id")
    )
    proposta_beneficiario_id = Column(
        UUID, ForeignKey(f"{REFERENCE_TABLE}_propostabeneficiario.id")
    )
