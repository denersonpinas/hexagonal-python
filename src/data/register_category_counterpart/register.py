from typing import Dict, Type
from src.data.interface import CategoryCounterpartRepositoryInterface
from src.domain.models import CategoryCounterpart
from src.domain.use_cases import RegisterCategoryCounterpartInterface


class RegisterCategoryCounterpart(RegisterCategoryCounterpartInterface):
    """Class to define category counterpart case: Register Category Counterpart"""

    def __init__(
        self, category_counterpart_repo: Type[CategoryCounterpartRepositoryInterface]
    ):
        self.__category_counterpart_repo = category_counterpart_repo

    def register(
        self, nome: str, descricao: str, subcategoria_id: int = None
    ) -> Dict[bool, CategoryCounterpart]:
        """Register category counterpart use case
        :param  -   nome: description of the category counterpart
                -   descricao: description of the category counterpart
                -   subcategoria_id: id subcategory of the category counterpart
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(nome, str)
            and isinstance(descricao, str)
            and len(descricao) <= 500
            and len(nome) <= 120
        )

        if validate_entry:
            response = self.__category_counterpart_repo.insert_category_counterpart(
                nome=nome, descricao=descricao, subcategoria_id=subcategoria_id
            )

        return {"Success": validate_entry, "Data": response}
