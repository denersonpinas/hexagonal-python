from sqlalchemy import UUID, Column, String, Integer, ForeignKey
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class PropostaArquivo(Base):
    __tablename__ = f"{REFERENCE_TABLE}_propostaarquivo"

    id = Column(UUID, primary_key=True)
    nome = Column(String(255))
    extensao = Column(String(4))
    tamanho = Column(Integer)
    url = Column(String(200))
    tipo_id = Column(String(32), ForeignKey(f"{REFERENCE_TABLE}_tipoarquivo.id"))
    proposta_id = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proposta.id"))

    def __req__(self):
        return f"Arquivo [nome={self.nome}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.nome == other.nome
            and self.extensao == other.extensao
            and self.tamanho == other.tamanho
            and self.url == other.url
        ):
            return True
        return False
