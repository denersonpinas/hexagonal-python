from typing import Optional
from src.data.interface.proponent_repository_interface import (
    ProponentRepositoryInterface,
)
from src.domain.models import Proponent
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.proponente import Proponente


class ProponentRepository(ProponentRepositoryInterface):
    """Class to manage Proponent Repository"""

    @classmethod
    def insert_proponent(
        cls,
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
        """Insert data in proponent entity
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
        :return -   tuple with proponent inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_proponent = Proponente(
                    cnpj=cnpj,
                    proposta_id=proposal_id,
                    razao_social=company_name,
                    nome_fantasia=trade_name,
                    endereco_cep=zip_code,
                    endereco_uf=state,
                    endereco_municipio=city,
                    endereco_bairro=neighborhood,
                    endereco_logradouro=street,
                    endereco_numero=number,
                    endereco_complemento=complement,
                    site=website,
                    rede_social=social_media,
                    resumo_curriculo=curriculum_summary,
                )
                db_connection.session.add(new_proponent)
                db_connection.session.flush()
                db_connection.session.commit()

                return Proponent(
                    cnpj=new_proponent.cnpj,
                    proposta_id=new_proponent.proposta_id,
                    razao_social=new_proponent.razao_social,
                    nome_fantasia=new_proponent.nome_fantasia,
                    endereco_cep=new_proponent.endereco_cep,
                    endereco_uf=new_proponent.endereco_uf,
                    endereco_municipio=new_proponent.endereco_municipio,
                    endereco_bairro=new_proponent.endereco_bairro,
                    endereco_logradouro=new_proponent.endereco_logradouro,
                    endereco_numero=new_proponent.endereco_numero,
                    endereco_complemento=new_proponent.endereco_complemento,
                    site=new_proponent.site,
                    rede_social=new_proponent.rede_social,
                    resumo_curriculo=new_proponent.resumo_curriculo,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
