from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class TipoArquivo(Base):
    __tablename__ = f"{REFERENCE_TABLE}_tipoarquivo"

    id = Column(String(32), primary_key=True)
    contexto = Column(String(32), nullable=False)
    descricao = Column(String(120), nullable=False)
    info = Column(String(1000), nullable=False)

    id_proposta_arquivo = relationship("PropostaArquivo")

    def __rep__(self):
        return f"TP Arquivo [contexto={self.contexto}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.contexto == other.contexto
            and self.descricao == other.descricao
            and self.info == other.info
        ):
            return True
        return False
