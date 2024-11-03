from sqlalchemy import UUID, Column, String, Integer, Float, ForeignKey
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class PropostaMeta(Base):
    __tablename__ = f"{REFERENCE_TABLE}_propostameta"

    id = Column(Integer, primary_key=True)
    ordem = Column(Integer)
    meta = Column(String, nullable=False)
    quantitativo = Column(Float, nullable=False)
    proposta_id = Column(UUID, ForeignKey(f"{REFERENCE_TABLE}_proposta.id"))

    def __req__(self):
        return f"Meta [meta={self.meta}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.meta == other.meta
            and self.ordem == other.ordem
            and self.quantitativo == other.quantitativo
        ):
            return True
        return False
