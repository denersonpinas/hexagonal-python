from sqlalchemy import Boolean, Column, String, Integer
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class Contrapartida(Base):
    __tablename__ = f"{REFERENCE_TABLE}_contrapartida"

    id = Column(Integer, primary_key=True)
    descricao = Column(String(500), nullable=False)
    exemplo_aplicabilidade = Column(String(500), nullable=False)
    obrigatoria = Column(Boolean, nullable=False)
    padrao = Column(Boolean, nullable=False)

    id_relacao_contrapartida_categoria = relationship("RelacaoCategoriaContrapartida")

    def __rep__(self):
        return f"Contrapartida [descricao={self.descricao}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.descricao == other.descricao
            and self.exemplo_aplicabilidade == other.exemplo_aplicabilidade
            and self.obrigatoria == other.obrigatoria
            and self.padrao == other.padrao
        ):
            return True
        return False
