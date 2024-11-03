from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class Lei(Base):
    __tablename__ = f"{REFERENCE_TABLE}_lei"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(250), nullable=False)

    id_abginvest_tpproj_lei = relationship("AbginvestTpprojLei")

    def __rep__(self):
        return f"Lei [nome={self.nome}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.nome == other.nome
            and self.descricao == other.descricao
        ):
            return True
        return False
