from collections import namedtuple

LegalRepresentative = namedtuple(
    "LegalRepresentative", "id, nome, cpf, email, cargo, proposta_id, resumo"
)
