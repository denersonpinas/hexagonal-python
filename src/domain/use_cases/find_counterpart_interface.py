from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import Counterpart


class FindCounterpartInterface(ABC):
    '''Interface to Find Counterpart use case'''

    @abstractmethod
    def by_id(cls, counterpart_id: int) -> Dict[bool, List[Counterpart]]:
        '''Specific Case'''

        raise Exception('Should implement method: by_id')

    @abstractmethod
    def by_required(cls, required: bool) -> Dict[bool, List[Counterpart]]:
        '''Specific Case'''

        raise Exception('Should implement method: by_required')

    @abstractmethod
    def by_default(cls, default: bool) -> Dict[bool, List[Counterpart]]:
        '''Specific Case'''

        raise Exception('Should implement method: by_default')

    @abstractmethod
    def by_id_and_required(cls, counterpart_id: int, required: bool) -> Dict[bool, List[Counterpart]]:
        '''Specific Case'''

        raise Exception('Should implement method: by_id_and_required')

    @abstractmethod
    def by_id_and_default(cls, counterpart_id: int, default: bool) -> Dict[bool, List[Counterpart]]:
        '''Specific Case'''

        raise Exception('Should implement method: by_id_and_default')

    @abstractmethod
    def by_required_and_default(cls, required: bool, default: bool) -> Dict[bool, List[Counterpart]]:
        '''Specific Case'''

        raise Exception('Should implement method: by_required_and_default')
    
    @abstractmethod
    def by_id_and_required_and_default(cls, counterpart_id: int, required: bool, default: bool) -> Dict[bool, List[Counterpart]]:
        '''Specific Case'''

        raise Exception('Should implement method: by_id_and_required_and_default')