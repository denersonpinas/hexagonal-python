from typing import Type
from src.domain.use_cases import RegisterTypeProjectInterface
from src.infra.repo import TypeProjectRepository


class RegisterTypeProject(RegisterTypeProjectInterface):
    """Class to define type project case: Register Type Project"""

    def __init__(self, type_project_repository: Type[TypeProjectRepository]):
        self._type_project_repository = type_project_repository

    def registry(self, nome: str, descricao: str):
        """Register type project use case
        :param  -   nome: name of the type project
                -   descricao: description of the type project
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(nome, str)
            and isinstance(descricao, str)
            and len(nome) <= 100
            and len(descricao) <= 250
        )

        if validate_entry:
            response = self._type_project_repository.insert_type_project(
                nome=nome, descricao=descricao
            )

        return {"Success": validate_entry, "Data": response}
