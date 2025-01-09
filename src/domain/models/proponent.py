from collections import namedtuple

Proponent = namedtuple(
    "Proponent",
    """cnpj, proposta_id, razao_social, nome_fantasia, endereco_cep, endereco_uf,
    endereco_municipio, endereco_bairro, endereco_logradouro, endereco_numero,
    endereco_complemento, site, rede_social, resumo_curriculo""",
)
