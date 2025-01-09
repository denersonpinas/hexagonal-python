from typing import Optional
from src.data.interface import ProponentRepositoryInterface
from src.domain.models import Proponent
from src.domain.test import mock_proponent


class ProponentRepositorySpy(ProponentRepositoryInterface):
    """Spy to Proponent Repository"""

    def __init__(self):
        self.insert_proponent_params = {}

    def insert_proponent(
        self,
        cnpj: str,
        proposal_id: str,
        company_name: str,
        trade_name: Optional[str] = None,
        zip_code: Optional[str] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        neighborhood: Optional[str] = None,
        street: Optional[str] = None,
        number: Optional[int] = None,
        complement: Optional[str] = None,
        website: Optional[str] = None,
        social_media: Optional[str] = None,
        curriculum_summary: Optional[str] = None,
    ) -> Proponent:
        """Spy to all the attributes"""

        self.insert_proponent_params["cnpj"] = cnpj
        self.insert_proponent_params["proposal_id"] = proposal_id
        self.insert_proponent_params["company_name"] = company_name
        self.insert_proponent_params["trade_name"] = trade_name
        self.insert_proponent_params["zip_code"] = zip_code
        self.insert_proponent_params["state"] = state
        self.insert_proponent_params["city"] = city
        self.insert_proponent_params["neighborhood"] = neighborhood
        self.insert_proponent_params["street"] = street
        self.insert_proponent_params["number"] = number
        self.insert_proponent_params["complement"] = complement
        self.insert_proponent_params["website"] = website
        self.insert_proponent_params["social_media"] = social_media
        self.insert_proponent_params["curriculum_summary"] = curriculum_summary

        return mock_proponent()
