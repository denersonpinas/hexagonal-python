from sqlalchemy import UUID, Column, ForeignKey, Integer
from src.constants.reference import REFERENCE_TABLE
from src.infra import Base


class PropostaLocalExecucao(Base):
    __tablename__ = f"{REFERENCE_TABLE}_propostalocalexececao"

    id = Column(Integer, primary_key=True)
    municipio_id = Column(Integer, ForeignKey(f"{REFERENCE_TABLE}_municipio.id"))
    proposta_id = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proposta.id"))
