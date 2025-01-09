from collections import namedtuple

Proposal = namedtuple(
    "Proposal",
    """id, titulo_projeto, resumo_projeto, descricao_projeto,
    dados_bancario_instituicao, dados_bancario_agencia_conta_bancaria,
    dados_bancario_conta_corrente, dados_bancario_cnpj_fundo,
    dados_bancario_razao_social_fundo,
    dados_bancario_contato_fundo_nome,dados_bancario_contato_fundo_email,
    valor_total_projeto, valor_total_lei_incentivo,
    valor_total_captado, valor_total_captado_lei_incentivo, valor_total_incentivado_nubank,
    observacoes, data_inicio_projeto, data_fim_projeto""",
)
