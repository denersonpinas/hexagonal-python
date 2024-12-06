from faker import Faker
from src.data.test import FindBenefitCategorizationTypeSpy
from src.infra.test import BenefitCategorizationTypeRepositorySpy
from src.presenters.helpers import HttpRequest
from src.presenters.controllers import FindBenefitCategorizationTypeController

faker = Faker()


def test_route_by_id():
    """Testing Route by id method"""

    find_categorization_type_use_case = FindBenefitCategorizationTypeSpy(
        BenefitCategorizationTypeRepositorySpy()
    )
    find_categorization_type_controller = FindBenefitCategorizationTypeController(
        find_categorization_type_use_case=find_categorization_type_use_case
    )
    http_request = HttpRequest(
        query={
            "id": faker.text(max_nb_chars=32),
        }
    )

    response = find_categorization_type_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_categorization_type_use_case.by_id_param["id"] == http_request.query["id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_all():
    """Testing Route by id and default method"""

    find_categorization_type_use_case = FindBenefitCategorizationTypeSpy(
        BenefitCategorizationTypeRepositorySpy()
    )
    find_categorization_type_controller = FindBenefitCategorizationTypeController(
        find_categorization_type_use_case=find_categorization_type_use_case
    )
    http_request = HttpRequest(query={})

    response = find_categorization_type_controller.route(http_request=http_request)

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing Route method fail"""

    find_categorization_type_use_case = FindBenefitCategorizationTypeSpy(
        BenefitCategorizationTypeRepositorySpy()
    )
    find_categorization_type_controller = FindBenefitCategorizationTypeController(
        find_categorization_type_use_case=find_categorization_type_use_case
    )
    http_request = HttpRequest(query={"other_query": faker.word()})

    response = find_categorization_type_controller.route(http_request=http_request)

    # Testing Inputs
    assert find_categorization_type_use_case.by_id_param == {}

    # Testing Output
    assert response.status_code == 422
    assert response.body
