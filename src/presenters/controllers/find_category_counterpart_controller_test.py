from faker import Faker
from src.data.test import FindCategoryCounterpartSpy
from src.infra.test import CategoryCounterpartRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_category_counterpart_controller import FindCategoryCounterpartController

faker = Faker()


def test_route_by_id():
    """Testing Handle by id method"""

    find_category_counterpart_use_case = FindCategoryCounterpartSpy(
        CategoryCounterpartRepositorySpy()
    )
    find_category_counterpart_controller = FindCategoryCounterpartController(
        find_category_counterpart_use_case=find_category_counterpart_use_case
    )
    http_request = HttpRequest(
        query={
            "category_counterpart_id": faker.random_number(digits=5),
        }
    )

    response = find_category_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_category_counterpart_use_case.by_id_param["category_counterpart_id"]
        == http_request.query["category_counterpart_id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_by_subcategory():
    """Testing Handle by id and required method"""

    find_category_counterpart_use_case = FindCategoryCounterpartSpy(
        CategoryCounterpartRepositorySpy()
    )
    find_category_counterpart_controller = FindCategoryCounterpartController(
        find_category_counterpart_use_case=find_category_counterpart_use_case
    )
    http_request = HttpRequest(
        query={
            "subcategory_id": faker.random_number(digits=5),
        }
    )

    response = find_category_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_category_counterpart_use_case.by_subcategory_param["subcategory_id"]
        == http_request.query["subcategory_id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_all():
    """Testing Handle by id and default method"""

    find_category_counterpart_use_case = FindCategoryCounterpartSpy(
        CategoryCounterpartRepositorySpy()
    )
    find_category_counterpart_controller = FindCategoryCounterpartController(
        find_category_counterpart_use_case=find_category_counterpart_use_case
    )
    http_request = HttpRequest(query={})

    response = find_category_counterpart_controller.route(http_request=http_request)

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_route_fail():
    """Testing Handle method fail"""

    find_category_counterpart_use_case = FindCategoryCounterpartSpy(
        CategoryCounterpartRepositorySpy()
    )
    find_category_counterpart_controller = FindCategoryCounterpartController(
        find_category_counterpart_use_case=find_category_counterpart_use_case
    )
    http_request = HttpRequest(query={"other_query": faker.word()})

    response = find_category_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert find_category_counterpart_use_case.by_id_param == {}
    assert find_category_counterpart_use_case.by_subcategory_param == {}

    # Testing Output
    assert response.status_code == 422
    assert response.body
