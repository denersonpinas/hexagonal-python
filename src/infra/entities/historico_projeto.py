from sqlalchemy import UUID, Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class HistoricoProjeto(Base):
    __tablename__ = f"{REFERENCE_TABLE}_historicoprojeto"

    id = Column(Integer, primary_key=True)
    ano_investimento = Column(Integer, nullable=False)
    titulo = Column(String(150), nullable=False)
    tipo_investimento = Column(String(16), nullable=False)
    id_proposta = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proponente.proposta_id"))

    id_historico_de_metas = relationship("HistoricoDeMetas")

    def __rep__(self):
        return f"Historico Projeto [titulo={self.titulo}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.titulo == other.titulo
            and self.ano_investimento == other.ano_investimento
            and self.tipo_investimento == other.tipo_investimento
        ):
            return True
        return False
