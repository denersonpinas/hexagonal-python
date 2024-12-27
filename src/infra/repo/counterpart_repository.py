from typing import List
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound
from src.data.interface import CounterpartRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.infra.entities import Contrapartida
from src.domain.models import Counterpart


class CounterpartRepository(CounterpartRepositoryInterface):
    """Class to manage Counterpart Repository"""

    @classmethod
    def insert_counterpart(
        cls, descricao: str, exemplo_aplicabilidade: str, obrigatoria: bool
    ) -> Counterpart:
        """Insert data in counterpart entity
        :param  -   descricao: counterpart description
                -   exemplo_aplicabilidade: counterpart example
                -   obrigatoria:    if requirement
                -   padrao: if default
        :return -   tuple with counterparts inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_counterpart = Contrapartida(
                    descricao=descricao,
                    exemplo_aplicabilidade=exemplo_aplicabilidade,
                    obrigatoria=obrigatoria,
                    padrao=True,
                )
                db_connection.session.add(new_counterpart)
                db_connection.session.flush()
                db_connection.session.commit()

                return Counterpart(
                    id=new_counterpart.id,
                    descricao=new_counterpart.descricao,
                    exemplo_aplicabilidade=new_counterpart.exemplo_aplicabilidade,
                    obrigatoria=new_counterpart.obrigatoria,
                    padrao=new_counterpart.padrao,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_counterpart(
        cls, counterpart_id: int = None, required: bool = None, default: bool = None
    ) -> List[Counterpart]:
        """Select data in counterpart entity by id and/or required and/or defeult
        :param  -   counterpart_id: Id of the register
                -   required: if required of the counterpart
                -   default: if default of the counterpart
        :return -   List with Counterpart selected
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = None

                if (
                    counterpart_id
                    and type(required) is not bool
                    and type(default) is not bool
                ):
                    query = select(Contrapartida).where(
                        Contrapartida.id == counterpart_id
                    )

                elif (
                    not counterpart_id
                    and type(required) is bool
                    and type(default) is not bool
                ):
                    query = select(Contrapartida).where(
                        Contrapartida.obrigatoria == required
                    )

                elif (
                    not counterpart_id
                    and type(required) is not bool
                    and type(default) is bool
                ):
                    query = select(Contrapartida).where(Contrapartida.padrao == default)

                elif (
                    counterpart_id
                    and type(required) is bool
                    and type(default) is not bool
                ):
                    query = (
                        select(Contrapartida)
                        .where(Contrapartida.id == counterpart_id)
                        .where(Contrapartida.obrigatoria == required)
                    )

                elif (
                    not counterpart_id
                    and type(required) is bool
                    and type(default) is bool
                ):
                    query = (
                        select(Contrapartida)
                        .where(Contrapartida.padrao == default)
                        .where(Contrapartida.obrigatoria == required)
                    )

                elif (
                    counterpart_id
                    and type(required) is not bool
                    and type(default) is bool
                ):
                    query = (
                        select(Contrapartida)
                        .where(Contrapartida.id == counterpart_id)
                        .where(Contrapartida.padrao == default)
                    )

                elif (
                    counterpart_id and type(required) is bool and type(default) is bool
                ):
                    query = (
                        select(Contrapartida)
                        .where(Contrapartida.id == counterpart_id)
                        .where(Contrapartida.obrigatoria == required)
                        .where(Contrapartida.padrao == default)
                    )

                response: List[Counterpart] = []
                for row in db_connection.session.execute(query).all():
                    response.append(row[0])
                return response

            except NoResultFound:
                return []
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return []

    @classmethod
    def select_all_counterpart(cls) -> List[Counterpart]:
        """Select all data in counterpart entity
        :param  -   is None
        :return -   List with Counterpart selected
        """

        with DBConnectionHandler() as db_connection:
            try:
                query = select(Contrapartida)
                response: List[Counterpart] = []
                for row in db_connection.session.execute(query).all():
                    response.append(row[0])
                return response
            except NoResultFound:
                return []
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return []
