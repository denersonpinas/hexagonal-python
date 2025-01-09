from sqlalchemy import UUID
from src.data.interface.proposal_file_repository_interface import (
    ProposalFileRepositoryInterface,
)
from src.domain.models import ProposalFile
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proposta_arquivo import PropostaArquivo


class ProposalFileRepository(ProposalFileRepositoryInterface):
    """Class to manage Proposal File Repository"""

    @classmethod
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
        """Insert data in proposal file entity
        :param  -   id: file unique identifier
                -   name: file name
                -   extension: file extension
                -   size: file size in bytes
                -   uri: file location uri
                -   proposal_id: foreign key to proposal
                -   type_id: foreign key to file type
        :return -   tuple with proposal file inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_file = PropostaArquivo(
                    id=id,
                    nome=name,
                    extensao=extension,
                    tamanho=size,
                    uri=uri,
                    proposta_id=proposal_id,
                    tipo_id=type_id,
                )
                db_connection.session.add(new_file)
                db_connection.session.flush()
                db_connection.session.commit()

                return ProposalFile(
                    id=new_file.id,
                    nome=new_file.nome,
                    extensao=new_file.extensao,
                    tamanho=new_file.tamanho,
                    uri=new_file.uri,
                    proposta_id=new_file.proposta_id,
                    tipo_id=new_file.tipo_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
