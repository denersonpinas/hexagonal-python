from faker import Faker
from src.data.test import FindCounterpartSpy
from src.infra.test import CounterpartRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_counterpart_controller import FindCounterpartController

faker = Faker()


def test_handle_by_id_and_required_and_default():
    """Testing Handle by id and required and default method"""

    find_counterpart_use_case = FindCounterpartSpy(CounterpartRepositorySpy())
    find_counterpart_controller = FindCounterpartController(
        find_counterpart_use_case=find_counterpart_use_case
    )
    http_request = HttpRequest(
        query={
            "counterpart_id": faker.random_number(),
            "required": faker.boolean(),
            "default": faker.boolean(),
        }
    )

    response = find_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_counterpart_use_case.by_id_and_required_and_default_param["counterpart_id"]
        == http_request.query["counterpart_id"]
    )
    assert (
        find_counterpart_use_case.by_id_and_required_and_default_param["required"]
        == http_request.query["required"]
    )
    assert (
        find_counterpart_use_case.by_id_and_required_and_default_param["default"]
        == http_request.query["default"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_handle_by_id_and_required():
    """Testing Handle by id and required method"""

    find_counterpart_use_case = FindCounterpartSpy(CounterpartRepositorySpy())
    find_counterpart_controller = FindCounterpartController(
        find_counterpart_use_case=find_counterpart_use_case
    )
    http_request = HttpRequest(
        query={"counterpart_id": faker.random_number(), "required": faker.boolean()}
    )

    response = find_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_counterpart_use_case.by_id_and_required_param["counterpart_id"]
        == http_request.query["counterpart_id"]
    )
    assert (
        find_counterpart_use_case.by_id_and_required_param["required"]
        == http_request.query["required"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_handle_by_id_and_default():
    """Testing Handle by id and default method"""

    find_counterpart_use_case = FindCounterpartSpy(CounterpartRepositorySpy())
    find_counterpart_controller = FindCounterpartController(
        find_counterpart_use_case=find_counterpart_use_case
    )
    http_request = HttpRequest(
        query={"counterpart_id": faker.random_number(), "default": faker.boolean()}
    )

    response = find_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_counterpart_use_case.by_id_and_default_param["counterpart_id"]
        == http_request.query["counterpart_id"]
    )
    assert (
        find_counterpart_use_case.by_id_and_default_param["default"]
        == http_request.query["default"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_handle_by_required_and_default():
    """Testing Handle by required and default method"""

    find_counterpart_use_case = FindCounterpartSpy(CounterpartRepositorySpy())
    find_counterpart_controller = FindCounterpartController(
        find_counterpart_use_case=find_counterpart_use_case
    )
    http_request = HttpRequest(
        query={"required": faker.boolean(), "default": faker.boolean()}
    )

    response = find_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_counterpart_use_case.by_required_and_default_param["required"]
        == http_request.query["required"]
    )
    assert (
        find_counterpart_use_case.by_required_and_default_param["default"]
        == http_request.query["default"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_handle_by_id():
    """Testing Handle by id method"""

    find_counterpart_use_case = FindCounterpartSpy(CounterpartRepositorySpy())
    find_counterpart_controller = FindCounterpartController(
        find_counterpart_use_case=find_counterpart_use_case
    )
    http_request = HttpRequest(query={"counterpart_id": faker.random_number()})

    response = find_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_counterpart_use_case.by_id_param["counterpart_id"]
        == http_request.query["counterpart_id"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_handle_by_required():
    """Testing Handle by required method"""

    find_counterpart_use_case = FindCounterpartSpy(CounterpartRepositorySpy())
    find_counterpart_controller = FindCounterpartController(
        find_counterpart_use_case=find_counterpart_use_case
    )
    http_request = HttpRequest(query={"required": faker.boolean()})

    response = find_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_counterpart_use_case.by_required_param["required"]
        == http_request.query["required"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_handle_by_default():
    """Testing Handle by default method"""

    find_counterpart_use_case = FindCounterpartSpy(CounterpartRepositorySpy())
    find_counterpart_controller = FindCounterpartController(
        find_counterpart_use_case=find_counterpart_use_case
    )
    http_request = HttpRequest(query={"default": faker.boolean()})

    response = find_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert (
        find_counterpart_use_case.by_default_param["default"]
        == http_request.query["default"]
    )

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_handle_no_query_param():
    """Testing Handle no query param method"""

    find_counterpart_use_case = FindCounterpartSpy(CounterpartRepositorySpy())
    find_counterpart_controller = FindCounterpartController(
        find_counterpart_use_case=find_counterpart_use_case
    )
    http_request = HttpRequest(query={})

    response = find_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert find_counterpart_use_case.by_id_and_required_and_default_param == {}
    assert find_counterpart_use_case.by_id_and_required_param == {}
    assert find_counterpart_use_case.by_id_and_default_param == {}
    assert find_counterpart_use_case.by_required_and_default_param == {}
    assert find_counterpart_use_case.by_id_param == {}
    assert find_counterpart_use_case.by_required_param == {}
    assert find_counterpart_use_case.by_default_param == {}

    # Testing Output
    assert response.status_code == 400
    assert response.body is None


def test_handle_fail():
    """Testing Handle method fail"""

    find_counterpart_use_case = FindCounterpartSpy(CounterpartRepositorySpy())
    find_counterpart_controller = FindCounterpartController(
        find_counterpart_use_case=find_counterpart_use_case
    )
    http_request = HttpRequest(query={"other_query": faker.word()})

    response = find_counterpart_controller.route(http_request=http_request)

    # Testing Inputs
    assert find_counterpart_use_case.by_id_and_required_and_default_param == {}
    assert find_counterpart_use_case.by_id_and_required_param == {}
    assert find_counterpart_use_case.by_id_and_default_param == {}
    assert find_counterpart_use_case.by_required_and_default_param == {}
    assert find_counterpart_use_case.by_id_param == {}
    assert find_counterpart_use_case.by_required_param == {}
    assert find_counterpart_use_case.by_default_param == {}

    # Testing Output
    assert response.status_code == 422
    assert response.body is None
