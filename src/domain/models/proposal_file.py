from collections import namedtuple

ProposalFile = namedtuple(
    "ProposalFile", "id, nome, extensao, tamanho, uri, proposta_id, tipo_id"
)
