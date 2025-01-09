from typing import Type
from src.domain.use_cases.register_goal_history_interface import (
    RegisterGoalHistoryInterface,
)
from src.main.interface.route_interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RegisterGoalHistoryController(RouteInterface):
    """Class to define route to register_goal_history use case"""

    def __init__(
        self,
        register_goal_history_use_case: Type[RegisterGoalHistoryInterface],
    ):
        self.register_goal_history_use_case = register_goal_history_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            body_params = http_request.body.keys()
            required_params = ["expected", "achieved", "project_history_id"]

            if all(param in body_params for param in required_params):
                try:
                    expected = http_request.body["expected"]
                    achieved = http_request.body["achieved"]
                    project_history_id = int(http_request.body["project_history_id"])

                    response = self.register_goal_history_use_case.register(
                        expected=expected,
                        achieved=achieved,
                        project_history_id=project_history_id,
                    )
                except (ValueError, TypeError):
                    response = {"Success": False, "Data": None}
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
