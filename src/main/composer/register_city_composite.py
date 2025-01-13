from src.data.register_city import RegisterCity
from src.infra.repo import CityRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterCityController


def register_city_composer() -> RouteInterface:
    """Composing Register City Route
    :param  -   None
    :return -   Object with Register City Route
    """

    repository = CityRepository()
    use_case = RegisterCity(repository)
    register_city_route = RegisterCityController(use_case)

    return register_city_route
