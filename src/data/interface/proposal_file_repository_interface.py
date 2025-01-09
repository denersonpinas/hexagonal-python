from abc import ABC, abstractmethod

from sqlalchemy import UUID

from src.domain.models import ProposalFile


class ProposalFileRepositoryInterface(ABC):
    """Interface to ProposalFile Repository"""

    @abstractmethod
    def insert_proposal_file(
        cls,
        id: UUID,
        name: str,
        extension: str,
        size: int,
        uri: str,
        proposal_id: UUID,
        type_id: str,
    ) -> ProposalFile:
        """abstractmethod"""
        raise Exception("Method not implemented")
