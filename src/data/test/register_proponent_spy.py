from typing import Dict, Optional, Type

from src.data.interface import ProponentRepositoryInterface
from src.domain.models import Proponent
from src.domain.test import mock_proponent
from src.domain.use_cases import RegisterProponentInterface


class RegisterProponentSpy(RegisterProponentInterface):
    "Class te define use case: Register Proponent"

    def __init__(self, proponent_repository: Type[ProponentRepositoryInterface]):
        self._proponent_repository = proponent_repository
        self.register_param = {}

    def register(
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
    ) -> Dict[bool, Proponent]:
        """Register proponent use case
        :param  -   cnpj: company registration number
                -   proposal_id: foreign key to proposal
                -   company_name: company official name
                -   trade_name: company trading name
                -   zip_code: address zip code
                -   state: address state
                -   city: address city
                -   neighborhood: address neighborhood
                -   street: address street
                -   number: address number
                -   complement: address complement
                -   website: company website
                -   social_media: company social media
                -   curriculum_summary: company curriculum summary
        :return -   Dictionary with informations of the process
        """

        response = None
        validate_entry = (
            isinstance(cnpj, str)
            and isinstance(proposal_id, str)
            and isinstance(company_name, str)
            and len(cnpj) == 14
            and len(company_name) <= 200
            and (trade_name is None or len(trade_name) <= 200)
            and (zip_code is None or len(zip_code) == 8)
            and (state is None or len(state) == 2)
            and (city is None or len(city) <= 100)
            and (neighborhood is None or len(neighborhood) <= 100)
            and (street is None or len(street) <= 100)
            and (number is None or isinstance(number, int))
            and (complement is None or len(complement) <= 100)
            and (website is None or len(website) <= 100)
            and (social_media is None or len(social_media) <= 100)
            and (curriculum_summary is None or len(curriculum_summary) <= 500)
        )

        if validate_entry:
            self.register_param["cnpj"] = cnpj
            self.register_param["proposal_id"] = proposal_id
            self.register_param["company_name"] = company_name
            self.register_param["trade_name"] = trade_name
            self.register_param["zip_code"] = zip_code
            self.register_param["state"] = state
            self.register_param["city"] = city
            self.register_param["neighborhood"] = neighborhood
            self.register_param["street"] = street
            self.register_param["number"] = number
            self.register_param["complement"] = complement
            self.register_param["website"] = website
            self.register_param["social_media"] = social_media
            self.register_param["curriculum_summary"] = curriculum_summary

            response = mock_proponent()

        return {"Success": validate_entry, "Data": response}
