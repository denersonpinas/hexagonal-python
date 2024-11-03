from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class TipoCategorizacaoBeneficiario(Base):
    __tablename__ = f"{REFERENCE_TABLE}_tipocategorizacaobeneficiario"

    id = Column(String(32), primary_key=True)
    descricao = Column(String(50), nullable=False)
    info = Column(String(150), nullable=False)

    id_caracterizacao_beneficiario = relationship("CategorizacaoBeneficiario")

    def __rep__(self):
        return f"Tipo Categorização Beneficiario [descricao={self.descricao}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.descricao == other.descricao
            and self.info == other.info
        ):
            return True
        return False
