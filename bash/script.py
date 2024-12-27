import requests


# Função para transformar os dados category
def transform_data(categories):
    transformed = []

    for category in categories:
        new_category = {"name": category["nome"], "description": category["descricao"]}

        # Adiciona subcategory_id apenas se existir subcategoria
        if category["subcategoria_de"]:
            new_category["subcategory_id"] = category["subcategoria_de"]["id"]

        transformed.append(new_category)

    return transformed


def transform_relations_data(relations):
    transformed = []

    for relation in relations:
        new_relation = {
            "category_id": relation["categoria"]["id"],
            "counterpart_id": relation["contrapartida"]["id"],
        }
        transformed.append(new_relation)

    return transformed


def transform_abginvest_data(abginvest_list):
    transformed = []

    for abginvest in abginvest_list:
        new_abginvest = {
            "investment_approach_id": abginvest["abordagem_investimento"],
            "type_project_id": abginvest["tipo_pojeto"],
            "law_id": abginvest["lei"] if abginvest["lei"] else None,
        }
        transformed.append(new_abginvest)

    return transformed


def transform_type_file_data(type_file_list):
    transformed = []

    for type_file in type_file_list:
        new_type_file = {
            "context": type_file["contexto"],
            "description": type_file["descricao"],
            "info": type_file["info"],
        }
        transformed.append(new_type_file)

    return transformed


def transform_thematic_data(thematic_list):
    transformed = []

    for thematic in thematic_list:
        new_thematic = {
            "description": thematic["descricao"],
        }
        transformed.append(new_thematic)

    return transformed


def transform_caracterization_type_data(caracterization_type_list):
    transformed = []

    for caracterization_type in caracterization_type_list:
        new_caracterization_type = {
            "id": caracterization_type["id"],
            "description": caracterization_type["descricao"],
            "info": caracterization_type["info"],
        }
        transformed.append(new_caracterization_type)

    return transformed


def transform_invest_appro_data(invest_appro_list):
    transformed = []

    for invest_appro in invest_appro_list:
        new_invest_appro = {
            "description": invest_appro["descricao"],
            "incentivized": invest_appro["incentivado"],
        }
        transformed.append(new_invest_appro)

    return transformed


def transform_law_data(law_list):
    transformed = []

    for law in law_list:
        new_law = {
            "name": law["nome"],
            "description": law["descricao"],
        }
        transformed.append(new_law)

    return transformed


def transform_type_project_data(type_project_list):
    transformed = []

    for type_project in type_project_list:
        new_type_project = {
            "name": type_project["nome"],
            "description": type_project["descricao"],
        }
        transformed.append(new_type_project)

    return transformed


def transform_counterparts_data(counterparts_list):
    transformed = []

    for counterparts in counterparts_list:
        new_counterparts = {
            "description": counterparts["descricao"],
            "example_aplicability": counterparts["exemplo_aplicabilidade"],
            "required": counterparts["obrigatoria"],
        }
        transformed.append(new_counterparts)

    return transformed


def transform_caracterization_data(caracterization_list):
    transformed = []

    for caracterization in caracterization_list:
        new_caracterization = {
            "value": caracterization["valor"],
            "type_id": caracterization["tipo"],
        }
        transformed.append(new_caracterization)

    return transformed


def transform_abginvest_contrpart_data(abginvest_contrpart_list):
    transformed = []

    for abginvest_contrpart in abginvest_contrpart_list:
        new_abginvest_contrpart = {
            "order": abginvest_contrpart["ordem"],
            "id_relacao_contrapartida": abginvest_contrpart["id_relacao_contrapartida"],
            "id_abginvest_tpproj_lei": abginvest_contrpart["id_abginvest_tpproj_lei"],
        }
        transformed.append(new_abginvest_contrpart)

    return transformed


# Fazer requisição GET
response = requests.get("http://15.229.252.182:8000/bff/cadastro_projeto/")
data = response.json()

# Transformar dados
abginvest_contrpart_list = [
    {"ordem": 1, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 5},
    {"ordem": 6, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 6},
    {"ordem": 7, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 7},
    {"ordem": 8, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 8},
    {"ordem": 9, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 9},
    {"ordem": 10, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 10},
    {"ordem": 11, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 11},
    {"ordem": 12, "id_abginvest_tpproj_lei": 1, "id_relacao_contrapartida": 12},
    {"ordem": 1, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 13},
    {"ordem": 6, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 14},
    {"ordem": 7, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 15},
    {"ordem": 8, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 16},
    {"ordem": 9, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 17},
    {"ordem": 10, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 18},
    {"ordem": 11, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 19},
    {"ordem": 12, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 20},
    {"ordem": 13, "id_abginvest_tpproj_lei": 2, "id_relacao_contrapartida": 11},
    {"ordem": 1, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 13},
    {"ordem": 6, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 14},
    {"ordem": 7, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 15},
    {"ordem": 8, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 16},
    {"ordem": 9, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 17},
    {"ordem": 10, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 18},
    {"ordem": 11, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 19},
    {"ordem": 12, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 20},
    {"ordem": 13, "id_abginvest_tpproj_lei": 3, "id_relacao_contrapartida": 11},
    {"ordem": 1, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 13},
    {"ordem": 6, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 14},
    {"ordem": 7, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 15},
    {"ordem": 8, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 16},
    {"ordem": 9, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 17},
    {"ordem": 10, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 18},
    {"ordem": 11, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 19},
    {"ordem": 12, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 20},
    {"ordem": 13, "id_abginvest_tpproj_lei": 4, "id_relacao_contrapartida": 11},
    {"ordem": 1, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 13},
    {"ordem": 6, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 14},
    {"ordem": 7, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 15},
    {"ordem": 8, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 16},
    {"ordem": 9, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 21},
    {"ordem": 10, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 22},
    {"ordem": 11, "id_abginvest_tpproj_lei": 30, "id_relacao_contrapartida": 11},
    {"ordem": 1, "id_abginvest_tpproj_lei": 31, "id_relacao_contrapartida": 1},
    {"ordem": 1, "id_abginvest_tpproj_lei": 5, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 5, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 5, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 5, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 5, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 5, "id_relacao_contrapartida": 23},
    {"ordem": 7, "id_abginvest_tpproj_lei": 5, "id_relacao_contrapartida": 24},
    {"ordem": 8, "id_abginvest_tpproj_lei": 5, "id_relacao_contrapartida": 25},
    {"ordem": 9, "id_abginvest_tpproj_lei": 5, "id_relacao_contrapartida": 26},
    {"ordem": 1, "id_abginvest_tpproj_lei": 6, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 6, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 6, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 6, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 6, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 6, "id_relacao_contrapartida": 23},
    {"ordem": 7, "id_abginvest_tpproj_lei": 6, "id_relacao_contrapartida": 24},
    {"ordem": 8, "id_abginvest_tpproj_lei": 6, "id_relacao_contrapartida": 25},
    {"ordem": 9, "id_abginvest_tpproj_lei": 6, "id_relacao_contrapartida": 26},
    {"ordem": 1, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 14},
    {"ordem": 6, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 11},
    {"ordem": 7, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 27},
    {"ordem": 8, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 24},
    {"ordem": 9, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 6},
    {"ordem": 10, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 18},
    {"ordem": 11, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 28},
    {"ordem": 12, "id_abginvest_tpproj_lei": 7, "id_relacao_contrapartida": 29},
    {"ordem": 1, "id_abginvest_tpproj_lei": 8, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 8, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 8, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 8, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 8, "id_relacao_contrapartida": 5},
    {"ordem": 6, "id_abginvest_tpproj_lei": 8, "id_relacao_contrapartida": 13},
    {"ordem": 7, "id_abginvest_tpproj_lei": 8, "id_relacao_contrapartida": 27},
    {"ordem": 8, "id_abginvest_tpproj_lei": 8, "id_relacao_contrapartida": 14},
    {"ordem": 9, "id_abginvest_tpproj_lei": 8, "id_relacao_contrapartida": 28},
    {"ordem": 11, "id_abginvest_tpproj_lei": 8, "id_relacao_contrapartida": 17},
    {"ordem": 1, "id_abginvest_tpproj_lei": 9, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 9, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 9, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 9, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 9, "id_relacao_contrapartida": 14},
    {"ordem": 6, "id_abginvest_tpproj_lei": 9, "id_relacao_contrapartida": 28},
    {"ordem": 6, "id_abginvest_tpproj_lei": 9, "id_relacao_contrapartida": 17},
    {"ordem": 1, "id_abginvest_tpproj_lei": 10, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 10, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 10, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 10, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 10, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 10, "id_relacao_contrapartida": 23},
    {"ordem": 7, "id_abginvest_tpproj_lei": 10, "id_relacao_contrapartida": 30},
    {"ordem": 8, "id_abginvest_tpproj_lei": 10, "id_relacao_contrapartida": 28},
    {"ordem": 1, "id_abginvest_tpproj_lei": 11, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 11, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 11, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 11, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 11, "id_relacao_contrapartida": 28},
    {"ordem": 6, "id_abginvest_tpproj_lei": 11, "id_relacao_contrapartida": 24},
    {"ordem": 7, "id_abginvest_tpproj_lei": 11, "id_relacao_contrapartida": 31},
    {"ordem": 8, "id_abginvest_tpproj_lei": 11, "id_relacao_contrapartida": 11},
    {"ordem": 1, "id_abginvest_tpproj_lei": 12, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 12, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 12, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 12, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 12, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 12, "id_relacao_contrapartida": 28},
    {"ordem": 7, "id_abginvest_tpproj_lei": 12, "id_relacao_contrapartida": 24},
    {"ordem": 8, "id_abginvest_tpproj_lei": 12, "id_relacao_contrapartida": 32},
    {"ordem": 9, "id_abginvest_tpproj_lei": 12, "id_relacao_contrapartida": 33},
    {"ordem": 1, "id_abginvest_tpproj_lei": 13, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 13, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 13, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 13, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 13, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 13, "id_relacao_contrapartida": 28},
    {"ordem": 7, "id_abginvest_tpproj_lei": 13, "id_relacao_contrapartida": 24},
    {"ordem": 8, "id_abginvest_tpproj_lei": 13, "id_relacao_contrapartida": 32},
    {"ordem": 9, "id_abginvest_tpproj_lei": 13, "id_relacao_contrapartida": 33},
    {"ordem": 1, "id_abginvest_tpproj_lei": 14, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 14, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 14, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 14, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 14, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 14, "id_relacao_contrapartida": 18},
    {"ordem": 7, "id_abginvest_tpproj_lei": 14, "id_relacao_contrapartida": 24},
    {"ordem": 8, "id_abginvest_tpproj_lei": 14, "id_relacao_contrapartida": 28},
    {"ordem": 9, "id_abginvest_tpproj_lei": 14, "id_relacao_contrapartida": 30},
    {"ordem": 1, "id_abginvest_tpproj_lei": 15, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 15, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 15, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 15, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 15, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 15, "id_relacao_contrapartida": 18},
    {"ordem": 7, "id_abginvest_tpproj_lei": 15, "id_relacao_contrapartida": 24},
    {"ordem": 8, "id_abginvest_tpproj_lei": 15, "id_relacao_contrapartida": 28},
    {"ordem": 9, "id_abginvest_tpproj_lei": 15, "id_relacao_contrapartida": 30},
    {"ordem": "Null", "id_abginvest_tpproj_lei": 20, "id_relacao_contrapartida": 1},
    {"ordem": "Null", "id_abginvest_tpproj_lei": 21, "id_relacao_contrapartida": 1},
    {"ordem": 1, "id_abginvest_tpproj_lei": 22, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 22, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 22, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 22, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 22, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 22, "id_relacao_contrapartida": 24},
    {"ordem": 7, "id_abginvest_tpproj_lei": 22, "id_relacao_contrapartida": 26},
    {"ordem": 1, "id_abginvest_tpproj_lei": 23, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 23, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 23, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 23, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 23, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 23, "id_relacao_contrapartida": 24},
    {"ordem": 7, "id_abginvest_tpproj_lei": 23, "id_relacao_contrapartida": 26},
    {"ordem": "Null", "id_abginvest_tpproj_lei": 28, "id_relacao_contrapartida": 1},
    {"ordem": "Null", "id_abginvest_tpproj_lei": 29, "id_relacao_contrapartida": 1},
    {"ordem": 1, "id_abginvest_tpproj_lei": 32, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 32, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 32, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 32, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 32, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 32, "id_relacao_contrapartida": 24},
    {"ordem": 7, "id_abginvest_tpproj_lei": 32, "id_relacao_contrapartida": 26},
    {"ordem": 1, "id_abginvest_tpproj_lei": 33, "id_relacao_contrapartida": 1},
    {"ordem": 2, "id_abginvest_tpproj_lei": 33, "id_relacao_contrapartida": 2},
    {"ordem": 3, "id_abginvest_tpproj_lei": 33, "id_relacao_contrapartida": 3},
    {"ordem": 4, "id_abginvest_tpproj_lei": 33, "id_relacao_contrapartida": 4},
    {"ordem": 5, "id_abginvest_tpproj_lei": 33, "id_relacao_contrapartida": 11},
    {"ordem": 6, "id_abginvest_tpproj_lei": 33, "id_relacao_contrapartida": 24},
    {"ordem": 7, "id_abginvest_tpproj_lei": 33, "id_relacao_contrapartida": 26},
    {"ordem": "Null", "id_abginvest_tpproj_lei": 38, "id_relacao_contrapartida": 1},
]
transformed_abginvest_contrpart = transform_abginvest_contrpart_data(
    abginvest_contrpart_list
)

categories = data["categoriasContrapartida"]
transformed_categories = transform_data(categories)

relations = data["relacao_contrapartidas_categoria"]
transformed_relations = transform_relations_data(relations)

abginvest_list = data["abginvest_tpproj_lei"]
transformed_abginvest = transform_abginvest_data(abginvest_list)

type_file_list = data["tipos_arquivos"]
transformed_type_file = transform_type_file_data(type_file_list)

thematic_list = data["tematicas"]
transformed_thematic = transform_thematic_data(thematic_list)

caracterization_type_list = data["tipos_categorizacoes_beneficiarios"]
transformed_caracterization_type = transform_caracterization_type_data(
    caracterization_type_list
)

invest_appro_list = data["abordagens_investimento"]
transformed_invest_appro = transform_invest_appro_data(invest_appro_list)

law_list = data["leis"]
transformed_law = transform_law_data(law_list)

type_project_list = data["tipos_projetos"]
transformed_type_project = transform_type_project_data(type_project_list)

counterparts_list = data["contrapartidas"]
transformed_counterparts = transform_counterparts_data(counterparts_list)

caracterization_list = data["categorizacoes_beneficiarios"]
transformed_caracterization = transform_caracterization_data(caracterization_list)

print("TR: ", transformed_abginvest_contrpart)

# Enviar via POST
for counterparts in transformed_counterparts:
    response = requests.post(
        "http://127.0.0.1:8001/api/counterpart/", json=counterparts
    )

    if response.status_code == 200:
        print(f"Relação {counterparts} enviada com sucesso")
    else:
        print(f"Erro ao enviar relação {counterparts}")

for type_project in transformed_type_project:
    response = requests.post(
        "http://127.0.0.1:8001/api/type-project/", json=type_project
    )

    if response.status_code == 200:
        print(f"Relação {type_project} enviada com sucesso")
    else:
        print(f"Erro ao enviar relação {type_project}")

for law in transformed_law:
    response = requests.post("http://127.0.0.1:8001/api/law/", json=law)

    if response.status_code == 200:
        print(f"Relação {law} enviada com sucesso")
    else:
        print(f"Erro ao enviar relação {law}")

for invest_appro in transformed_invest_appro:
    response = requests.post(
        "http://127.0.0.1:8001/api/investment-approach/", json=invest_appro
    )

    if response.status_code == 200:
        print(f"Relação {invest_appro} enviada com sucesso")
    else:
        print(f"Erro ao enviar relação {invest_appro}")

for caracterization_type in transformed_caracterization_type:
    response = requests.post(
        "http://127.0.0.1:8001/api/caracterization-type/", json=caracterization_type
    )

    if response.status_code == 200:
        print(f"Relação {caracterization_type} enviada com sucesso")
    else:
        print(f"Erro ao enviar relação {caracterization_type}")

for thematic in transformed_thematic:
    response = requests.post("http://127.0.0.1:8001/api/thematic/", json=thematic)

    if response.status_code == 200:
        print(f"Relação {thematic} enviada com sucesso")
    else:
        print(f"Erro ao enviar relação {thematic}")

for typeFile in transformed_type_file:
    response = requests.post("http://127.0.0.1:8001/api/type-file/", json=typeFile)

    if response.status_code == 200:
        print(f"Relação {typeFile} enviada com sucesso")
    else:
        print(f"Erro ao enviar relação {typeFile}")

for category in transformed_categories:
    response = requests.post(
        "http://127.0.0.1:8001/api/category-counterpart/", json=category
    )

    if response.status_code == 200:
        print(f"Categoria {category['name']} enviada com sucesso")
    else:
        print(f"Erro ao enviar categoria {category['name']}")

for caracterization in transformed_caracterization:
    response = requests.post(
        "http://127.0.0.1:8001/api/caracterization/", json=caracterization
    )

    if response.status_code == 200:
        print(f"Relação {caracterization} enviada com sucesso")
    else:
        print(f"Erro ao enviar relação {caracterization}")

for relation in transformed_relations:
    response = requests.post(
        "http://127.0.0.1:8001/api/relationship-category-counterpart/", json=relation
    )

    if response.status_code == 200:
        print(f"Relação categoria {relation['category_id']} enviada com sucesso")
    else:
        print(
            f"Erro ao enviar relação categoria {relation['category_id']} e contrapartida {relation['counterpart_id']}"
        )

for abginvest in transformed_abginvest:
    response = requests.post(
        "http://127.0.0.1:8001/api/abginvest-tpproj-lei/", json=abginvest
    )

    if response.status_code == 200:
        print(f"Relação {abginvest} enviada com sucesso")
    else:
        print(f"Erro ao enviar relação {abginvest}")

for abginvest_contrpart in transformed_abginvest_contrpart:
    response = requests.post(
        "http://127.0.0.1:8001/api/abginvest-tpproj-lei-contrpart/",
        json=abginvest_contrpart,
    )

    if response.status_code == 200:
        print(f"Relação {abginvest_contrpart} enviada com sucesso")
    else:
        print(f"Erro ao enviar relação {abginvest_contrpart}")
