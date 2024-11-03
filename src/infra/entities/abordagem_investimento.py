from sqlalchemy import Boolean, Column, String, Integer
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class AbordagemInvestimento(Base):
    __tablename__ = f"{REFERENCE_TABLE}_abordageminvestimento"

    id = Column(Integer, primary_key=True)
    descricao = Column(String(80), nullable=False)
    incetivado = Column(Boolean, nullable=False)

    id_abginvest_tpproj_lei = relationship("AbginvestTpprojLei")

    def __rep__(self):
        return f"Abordagem Investimento [descricao={self.descricao}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.descricao == other.descricao
            and self.incetivado == other.incetivado
        ):
            return True
        return False
