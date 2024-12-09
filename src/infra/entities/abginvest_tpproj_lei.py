from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class AbginvestTpprojLei(Base):
    __tablename__ = f"{REFERENCE_TABLE}_abginvest_tpproj_lei"

    id = Column(Integer, primary_key=True)
    abordagem_investimento_id = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_abordageminvestimento.id")
    )
    lei_id = Column(Integer, ForeignKey(f"{REFERENCE_TABLE}_lei.id"))
    tipo_pojeto_id = Column(Integer, ForeignKey(f"{REFERENCE_TABLE}_tipoprojeto.id"))

    id_proposta_abginvest_tpproj_lei = relationship("PropostaAbginvestTpprojLei")
    id_abginvest_tpproj_lei_contrpart = relationship("AbginvestTpprojLeiContrpart")

    def __rep__(self):
        return f"AbginvestTpprojLei [id={self.id}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.abordagem_investimento_id == other.abordagem_investimento_id
            and self.lei_id == other.lei_id
            and self.tipo_pojeto_id == other.tipo_pojeto_id
        ):
            return True
        return False
