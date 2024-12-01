from typing import Dict, Type

from src.data.interface import CategoryCounterpartRepositoryInterface
from src.domain.models import CategoryCounterpart
from src.domain.test import mock_category_counterpart
from src.domain.use_cases import RegisterCategoryCounterpartInterface


class RegisterCategoryCounterpartSpy(RegisterCategoryCounterpartInterface):
    "Class te define use case: Register Category Counterpart"

    def __init__(
        self, category_counterpart_repo: Type[CategoryCounterpartRepositoryInterface]
    ):
        self._category_counterpart_repo = category_counterpart_repo
        self.registry_param = {}

    def registry(
        self, nome: str, descricao: str, subcategoria_id: int = None
    ) -> Dict[bool, CategoryCounterpart]:
        """Register category counterpart use case"""

        response = None
        validate_entry = (
            isinstance(nome, str)
            and isinstance(descricao, str)
            and len(nome) <= 120
            and len(descricao) <= 500
        )

        if validate_entry:
            self.registry_param["nome"] = nome
            self.registry_param["descricao"] = descricao
            self.registry_param["subcategoria_id"] = subcategoria_id

            response = mock_category_counterpart()

        return {"Success": validate_entry, "Data": response}
