from sqlite3 import IntegrityError
from typing import Type

from src.main.interface import RouteInterface
from src.presenters.errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


def flask_adapter(request: any, api_route: Type[RouteInterface]) -> any:
    """Adapter pattern to Flask
    :param      - request: Flask Request
                - api_route: RouteInterface
    :return     - HttpResponse
    """

    http_request = HttpRequest(body=request.json)

    try:
        response = api_route.route(http_request=http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()

        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
