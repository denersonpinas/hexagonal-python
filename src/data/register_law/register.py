from typing import Type
from src.domain.use_cases.register_law_interface import RegisterLawInterface
from src.infra.repo.law_repository import LawRepository


class RegisterLaw(RegisterLawInterface):
    """Class to define law case: Register Law"""

    def __init__(self, law_repository: Type[LawRepository]):
        self._law_repository = law_repository

    def register(self, nome: str, descricao: str):
        """Register law use case
        :param  -   nome: name of the law
                -   descricao: description of the law
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
            response = self._law_repository.insert_law(nome=nome, descricao=descricao)

        return {"Success": validate_entry, "Data": response}
