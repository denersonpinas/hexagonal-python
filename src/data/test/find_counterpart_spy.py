from typing import Dict, List, Type
from src.data.interface import CounterpartRepositoryInterface
from src.domain.models import Counterpart
from src.domain.test import mock_counterpart
from src.domain.use_cases import FindCounterpartInterface


class FindCounterpartSpy(FindCounterpartInterface):
    """Class to define use case: Select Counterpart Spy"""

    def __init__(self, counterpart_repository: Type[CounterpartRepositoryInterface]):
        self.counterpart_repository = counterpart_repository
        self.by_id_param = {}
        self.by_required_param = {}
        self.by_default_param = {}
        self.by_id_and_required_param = {}
        self.by_id_and_default_param = {}
        self.by_required_and_default_param = {}
        self.by_id_and_required_and_default_param = {}

    def by_id(self, counterpart_id: int) -> Dict[bool, List[Counterpart]]:
        """Select Counterpart by id spy"""

        self.by_id_param["counterpart_id"] = counterpart_id
        response = None
        validate_entry = isinstance(counterpart_id, int)

        if validate_entry:
            response = [mock_counterpart()]

        return {"Success": validate_entry, "Data": response}

    def by_required(self, required: bool) -> Dict[bool, List[Counterpart]]:
        """Select Counterpart by is required spy"""

        self.by_required_param["required"] = required
        response = None
        validate_entry = isinstance(required, bool)

        if validate_entry:
            response = [mock_counterpart()]

        return {"Success": validate_entry, "Data": response}

    def by_default(self, default: bool) -> Dict[bool, List[Counterpart]]:
        """Select Counterpart by is default spy"""

        self.by_default_param["default"] = default
        response = None
        validate_entry = isinstance(default, bool)

        if validate_entry:
            response = [mock_counterpart()]

        return {"Success": validate_entry, "Data": response}

    def by_id_and_required(
        self, counterpart_id: int, required: bool
    ) -> Dict[bool, List[Counterpart]]:
        """Select Counterpart by id and if is required spy"""

        self.by_id_and_required_param["counterpart_id"] = counterpart_id
        self.by_id_and_required_param["required"] = required
        response = None
        validate_entry = isinstance(counterpart_id, int) and isinstance(required, bool)

        if validate_entry:
            response = [mock_counterpart()]

        return {"Success": validate_entry, "Data": response}

    def by_id_and_default(
        self, counterpart_id: int, default: bool
    ) -> Dict[bool, List[Counterpart]]:
        """Select Counterpart by id and if is default spy"""

        self.by_id_and_default_param["counterpart_id"] = counterpart_id
        self.by_id_and_default_param["default"] = default
        response = None
        validate_entry = isinstance(counterpart_id, int) and isinstance(default, bool)

        if validate_entry:
            response = [mock_counterpart()]

        return {"Success": validate_entry, "Data": response}

    def by_required_and_default(
        self, required: bool, default: bool
    ) -> Dict[bool, List[Counterpart]]:
        """Select Counterpart by if is required and if is default spy"""

        self.by_required_and_default_param["required"] = required
        self.by_required_and_default_param["default"] = default
        response = None
        validate_entry = isinstance(required, bool) and isinstance(default, bool)

        if validate_entry:
            response = [mock_counterpart()]

        return {"Success": validate_entry, "Data": response}

    def by_id_and_required_and_default(
        self, counterpart_id: int, required: bool, default: bool
    ) -> Dict[bool, List[Counterpart]]:
        """Select Counterpart by id and if is required if is default spy"""

        self.by_id_and_required_and_default_param["counterpart_id"] = counterpart_id
        self.by_id_and_required_and_default_param["required"] = required
        self.by_id_and_required_and_default_param["default"] = default
        response = None
        validate_entry = (
            isinstance(counterpart_id, int)
            and isinstance(required, bool)
            and isinstance(default, bool)
        )

        if validate_entry:
            response = [mock_counterpart()]

        return {"Success": validate_entry, "Data": response}
