from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class AbginvestTpprojLeiContrpart(Base):
    __tablename__ = f"{REFERENCE_TABLE}_abginvest_tpproj_lei_contrpart"

    id = Column(Integer, primary_key=True)
    ordem = Column(Integer, nullable=False)
    id_relacao_contrapartida_categoria = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_relacaocategoriacontrapartida.id")
    )
    id_abginvest_tpproj_lei = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_abginvest_tpproj_lei.id")
    )

    id_proposta_contrapartida = relationship("PropostaContrapartida")

    def __rep__(self):
        return f"AbginvestTpprojLeiContrpart [id={self.id}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.ordem == other.ordem
            and self.id_relacao_contrapartida_categoria
            == other.id_relacao_contrapartida_categoria
            and self.id_abginvest_tpproj_lei == other.id_abginvest_tpproj_lei
        ):
            return True
        return False
