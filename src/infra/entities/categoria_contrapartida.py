from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra.config import Base


class CategoriaContrapartida(Base):
    __tablename__ = f"{REFERENCE_TABLE}_categoriacontrapartida"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    descricao = Column(String(500), nullable=False)
    subcategoria_de_id = Column(
        Integer, ForeignKey(f"{REFERENCE_TABLE}_categoriacontrapartida.id")
    )

    id_relacao_contrapartida_categoria = relationship("RelacaoCategoriaContrapartida")

    def __rep__(self):
        return f"Categoria Contrapartida [nome={self.nome}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.descricao == other.descricao
            and self.nome == other.nome
            and self.subcategoria_de_id == other.subcategoria_de_id
        ):
            return True
        return False
