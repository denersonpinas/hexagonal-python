from typing import Dict, List, Type
from src.data.interface import CounterpartRepositoryInterface
from src.domain.models import Counterpart
from src.domain.use_cases import FindCounterpartInterface


class FindCounterpart(FindCounterpartInterface):
    '''Class to define use case Find Counterpart'''

    def __init__(self, counterpart_repository: Type[CounterpartRepositoryInterface]):
        self.counterpart_repository = counterpart_repository
    
    def by_id(self, counterpart_id: int) -> Dict[bool, List[Counterpart]]:
        '''Select Counterpart by id
        :param  -   counterpart_id: id of the counterpart
        :return -   Dictionary with informations od the process
        '''

        response = None
        validate_entry = isinstance(counterpart_id, int)

        if validate_entry:
            response = self.counterpart_repository.select_counterpart(counterpart_id=counterpart_id)
        
        return {"Success": validate_entry, "Data": response}
    
    def by_required(self, required: bool) -> Dict[bool, List[Counterpart]]:
        '''Select Counterpart by is required
        :param  -   required: if counterpart is required
        :return -   Dictionary with informations od the process
        '''

        response = None
        validate_entry = isinstance(required, bool)

        if validate_entry:
            response = self.counterpart_repository.select_counterpart(required=required)
        
        return {"Success": validate_entry, "Data": response}

    def by_default(self, default: bool) -> Dict[bool, List[Counterpart]]:
        '''Select Counterpart by is default
        :param  -   default: if counterpart is dafault
        :return -   Dictionary with informations od the process
        '''

        response = None
        validate_entry = isinstance(default, bool)

        if validate_entry:
            response = self.counterpart_repository.select_counterpart(default=default)
        
        return {"Success": validate_entry, "Data": response}

    def by_id_and_required(self, counterpart_id: int, required: bool) -> Dict[bool, List[Counterpart]]:
        '''Select Counterpart by id and if is required
        :param  -   counterpart_id: id of the counterpart
                -   required: if counterpart is required
        :return -   Dictionary with informations od the process
        '''

        response = None
        validate_entry = isinstance(counterpart_id, int) and isinstance(required, bool)

        if validate_entry:
            response = self.counterpart_repository.select_counterpart(counterpart_id=counterpart_id, required=required)
        
        return {"Success": validate_entry, "Data": response}
    
    def by_id_and_default(self, counterpart_id: int, default: bool) -> Dict[bool, List[Counterpart]]:
        '''Select Counterpart by id and if is default
        :param  -   counterpart_id: id of the counterpart
                -   default: if counterpart is default
        :return -   Dictionary with informations od the process
        '''

        response = None
        validate_entry = isinstance(counterpart_id, int) and isinstance(default, bool)

        if validate_entry:
            response = self.counterpart_repository.select_counterpart(counterpart_id=counterpart_id, default=default)
        
        return {"Success": validate_entry, "Data": response}

    def by_required_and_default(self, required: bool, default: bool) -> Dict[bool, List[Counterpart]]:
            '''Select Counterpart by if is required and if is default
            :param  -   required: if counterpart is required
                    -   default: if counterpart is default
            :return -   Dictionary with informations od the process
            '''

            response = None
            validate_entry = isinstance(required, bool) and isinstance(default, bool)

            if validate_entry:
                response = self.counterpart_repository.select_counterpart(required=required, default=default)
            
            return {"Success": validate_entry, "Data": response}

    def by_id_and_required_and_default(self, counterpart_id: int, required: bool, default: bool) -> Dict[bool, List[Counterpart]]:
        '''Select Counterpart by id and if is required if is default
        :param  -   counterpart_id: id of the counterpart
                -   required: if counterpart is required
                -   default: if counterpart is default
        :return -   Dictionary with informations od the process
        '''

        response = None
        validate_entry = isinstance(counterpart_id, int) and isinstance(required, bool) and isinstance(default, bool)

        if validate_entry:
            response = self.counterpart_repository.select_counterpart(counterpart_id=counterpart_id, required=required, default=default)
        
        return {"Success": validate_entry, "Data": response}