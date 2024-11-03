from sqlalchemy import UUID, Column, Numeric, String, Date
from sqlalchemy.orm import relationship
from src.constants.reference import REFERENCE_TABLE
from src.infra import Base


class Proposta(Base):
    __tablename__ = f"{REFERENCE_TABLE}_proposta"

    id = Column(UUID, primary_key=True)
    titulo_projeto = Column(String(250), nullable=False)
    resumo_projeto = Column(String(500), nullable=False)
    descricao_projeto = Column(String(1000), nullable=False)
    dados_bancario_instituicao = Column(String(250), nullable=False)
    dados_bancario_agencia_conta_bancaria = Column(String(250), nullable=False)
    dados_bancario_conta_corrente = Column(String(250), nullable=False)
    dados_bancario_cnpj_fundo = Column(String(14))
    dados_bancario_razao_social_fundo = Column(String(250))
    dados_bancario_contato_fundo_nome = Column(String(250))
    dados_bancario_contato_fundo_email = Column(String(150))
    valor_total_projeto = Column(Numeric(16, 2), nullable=False)
    valor_total_lei_incentivo = Column(Numeric(16, 2), nullable=False)
    valor_total_captado = Column(Numeric(16, 2), nullable=False)
    valor_total_captado_lei_incentivo = Column(Numeric(16, 2), nullable=False)
    valor_total_incentivado_nubank = Column(Numeric(16, 2), nullable=False)
    observacoes = Column(String(250), nullable=False)
    data_inicio_projeto = Column(Date, nullable=False)
    data_fim_projeto = Column(Date, nullable=False)

    arquivos = relationship("PropostaArquivo", back_populates="proposta")
    metas = relationship("PropostaMeta", back_populates="proposta")
    gerenciamento = relationship("GerenciamentoProposta", back_populates="proposta")
    proponente = relationship("Proponente", back_populates="proposta")
    beneficiarios = relationship("PropostaBeneficiario", back_populates="proposta")
    marcos = relationship("PropostaMarcos", back_populates="proposta")
    abginvest = relationship("PropostaAbginvestTpprojLei", back_populates="proposta")
    temas = relationship("PropostaTematica", back_populates="proposta")
    patrocinador = relationship("PropostaPatrocinador", back_populates="proposta")
    municipios = relationship("PropostaLocalExecucao", back_populates="proposta")

    def __req__(self):
        return f"Proposta [titulo={self.titulo_projeto}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.titulo_projeto == other.titulo_projeto
            and self.resumo_projeto == other.resumo_projeto
            and self.descricao_projeto == other.descricao_projeto
            and self.data_inicio_projeto == other.data_inicio_projeto
            and self.data_fim_projeto == other.data_fim_projeto
        ):
            return True
        return False
