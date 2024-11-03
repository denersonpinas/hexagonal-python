from sqlalchemy import Column, ForeignKey, String, Integer
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class HistoricoDeMetas(Base):
    __tablename__ = f"{REFERENCE_TABLE}_historicodemetas"

    id = Column(Integer, primary_key=True)
    previsto = Column(String(144), nullable=False)
    alcancado = Column(String(144), nullable=False)
    id_historico_projeto = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_historicoprojeto.id")
    )

    def __rep__(self):
        return f"Historico Metas [previsto={self.previsto}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.previsto == other.previsto
            and self.alcancado == other.alcancado
        ):
            return True
        return False
