from sqlalchemy import UUID, Column, ForeignKey, String, Integer
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class HistoricoDeFornecimento(Base):
    __tablename__ = f"{REFERENCE_TABLE}_historicodefornecimento"

    id = Column(Integer, primary_key=True)
    servico_prestado = Column(String(250), nullable=False)
    responsavel_contratacao = Column(String(250), nullable=False)
    id_proposta = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proponente.proposta_id"))

    def __rep__(self):
        return f"Historico de Fornecimento [servico prestado={self.servico_prestado}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.servico_prestado == other.servico_prestado
            and self.responsavel_contratacao == other.responsavel_contratacao
        ):
            return True
        return False
