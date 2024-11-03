from sqlalchemy import UUID, Column, ForeignKey, String, Integer
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class PropostaContrapartida(Base):
    __tablename__ = f"{REFERENCE_TABLE}_propostacontrapartida"

    id = Column(UUID, primary_key=True)
    descricao = Column(String(250), nullable=False)
    quantitativo = Column(Integer, nullable=False)

    id_abginvest_tpproj_lei_contrpart = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_abginvest_tpproj_lei_contrpart.id")
    )
    id_proposta_abginvest_tpproj_lei = Column(
        UUID, ForeignKey(f"{REFERENCE_TABLE}_proposta_abginvest_tpproj_lei.id")
    )

    def __rep__(self):
        return f"Proposta contrapartida [descricao={self.descricao}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.descricao == other.descricao
            and self.quantitativo == other.quantitativo
        ):
            return True
        return False
