from src.data.register_legal_representative import RegisterLegalRepresentative
from src.infra.repo import LegalRepresentativeRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterLegalRepresentativeController


def register_legal_representative_composer() -> RouteInterface:
    """Composing Register LegalRepresentative Route
    :param  -   None
    :return -   Object with Register LegalRepresentative Route
    """

    repository = LegalRepresentativeRepository()
    use_case = RegisterLegalRepresentative(repository)
    register_legal_representative_route = RegisterLegalRepresentativeController(
        use_case
    )

    return register_legal_representative_route
