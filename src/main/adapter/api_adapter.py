from sqlite3 import IntegrityError
from typing import Type
from flask import Request

from src.main.interface import RouteInterface
from src.presenters.errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


def flask_adapter_get(request: Type[Request], api_route: Type[RouteInterface]) -> any:
    """Adapter pattern to Flask Get method
    :param      - request: Flask Request
                - api_route: RouteInterface
    :return     - HttpResponse
    """

    query_string_params = {}

    try:
        query_string_params = request.args.to_dict()

        if "counterpart_id" in query_string_params.keys():
            query_string_params["counterpart_id"] = int(
                query_string_params["counterpart_id"]
            )
        if "required" in query_string_params.keys():
            query_string_params["required"] = bool(query_string_params["required"])
        if "default" in query_string_params.keys():
            query_string_params["default"] = bool(query_string_params["default"])

    except Exception as exc:  # noqa: E722
        print("Error encontrado: ", exc)
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    http_request = HttpRequest(header=request.headers, query=query_string_params)

    try:
        response = api_route.route(http_request=http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
    except Exception as exc:
        print("Error encontrado: ", exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response


def flask_adapter_post(request: Type[Request], api_route: Type[RouteInterface]) -> any:
    """Adapter pattern to Flask Post method
    :param      - request: Flask Request
                - api_route: RouteInterface
    :return     - HttpResponse
    """

    http_request = HttpRequest(header=request.headers, body=request.json)

    try:
        response = api_route.route(http_request=http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
    except Exception as exc:
        print("Error encontrado: ", exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
