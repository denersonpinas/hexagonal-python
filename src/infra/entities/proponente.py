from sqlalchemy import Column, ForeignKey, Integer, String, UUID
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra import Base


class Proponente(Base):
    __tablename__ = f"{REFERENCE_TABLE}_proponente"

    proposta_id = Column(
        UUID, ForeignKey(f"{REFERENCE_TABLE}_proposta.id"), primary_key=True
    )
    cnpj = Column(String(14), nullable=False)
    razao_social = Column(String(120), nullable=False)
    nome_fantasia = Column(String(120), nullable=False)
    endereco_cep = Column(String(8), nullable=False)
    endereco_uf = Column(String(2), nullable=False)
    endereco_municipio = Column(String(120), nullable=False)
    endereco_bairro = Column(String(120), nullable=False)
    endereco_logradouro = Column(String(120), nullable=False)
    endereco_numero = Column(Integer, nullable=False)
    endereco_complemento = Column(String(100))
    site = Column(String(250))
    rede_social = Column(String(250))
    resumo_curriculo = Column(String(1000))

    id_proposta = relationship("Proposta")
    id_ponto_contato = relationship("PontoDeContatoProjeto")
    id_historico_parcerias = relationship("HistoricoDeParcerias")
    id_historico_projeto = relationship("HistoricoProjeto")
    id_representante_legal = relationship("RepresentanteLegal")
    id_historico_de_fornecimento = relationship("HistoricoDeFornecimento")

    def __rep__(self):
        return f"Proponente [nome={self.nome_fantasia}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.cnpj == other.cnpj
            and self.razao_social == other.razao_social
            and self.nome_fantasia == other.nome_fantasia
            and self.endereco_cep == other.endereco_cep
            and self.endereco_uf == other.endereco_uf
            and self.endereco_municipio == other.endereco_municipio
            and self.endereco_bairro == other.endereco_bairro
            and self.endereco_logradouro == other.endereco_logradouro
            and self.endereco_numero == other.endereco_numero
        ):
            return True
        return False
