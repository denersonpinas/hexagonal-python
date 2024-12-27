from dataclasses import dataclass
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.config.db_base import Base


@dataclass
class TipoCategorizacaoBeneficiario(Base):
    __tablename__ = "tcc_api_tipocategorizacaobeneficiario"

    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    descricao: Mapped[str] = mapped_column(String(50))
    info: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)

    categorizacao_beneficiario = relationship(
        "CategorizacaoBeneficiario", back_populates="tipo_categorizacao_beneficiario"
    )
