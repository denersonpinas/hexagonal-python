from sqlalchemy import UUID, Column, String, Date, ForeignKey, Uuid
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class GerenciamentoProposta(Base):
    __tablename__ = f"{REFERENCE_TABLE}_gerenciamentoproposta"

    id = Column(UUID, primary_key=True)
    criado_em = Column(Date, nullable=False)
    trimestre_de_referencia = Column(Date, nullable=False)
    tipo = Column(String, nullable=False)
    proposta_id = Column(Uuid, ForeignKey(f"{REFERENCE_TABLE}_proposta.id"))

    def __rep__(self):
        return f"Gerenciamento [Criado_em={self.criado_em}, Tipo={self.tipo}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.criado_em == other.criado_em
            and self.tipo == other.tipo
            and self.trimestre_de_referencia == other.trimestre_de_referencia
        ):
            return True
        return False
