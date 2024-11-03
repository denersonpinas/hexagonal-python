from sqlalchemy import UUID, Column, ForeignKey, String, Integer
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class HistoricoDeParcerias(Base):
    __tablename__ = f"{REFERENCE_TABLE}_historicodeparcerias"

    id = Column(Integer, primary_key=True)
    numero_de_patrocinadores = Column(Integer)
    numero_de_renovacao = Column(Integer)
    informacoes_adicionais = Column(String(250))
    id_proposta = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proponente.proposta_id"))

    def __rep__(self):
        return f"Historico Parcerias [numero de patrocinadores={self.numero_de_patrocinadores}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.numero_de_patrocinadores == other.numero_de_patrocinadores
            and self.numero_de_renovacao == other.numero_de_renovacao
        ):
            return True
        return False
