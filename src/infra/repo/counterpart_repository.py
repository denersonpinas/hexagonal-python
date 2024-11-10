from typing import List
from src.infra.config import DBConnectionHandler
from src.infra.entities import Contrapartida
from src.domain.models import Counterpart


class CounterpartRepository:
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
        :param  -   counterpart_id: Id of the registry
                -   required: if required of the counterpart
                -   default: if default of the counterpart
        :return -   List with Counterpart selected
        """

        with DBConnectionHandler() as db_connection:
            try:
                query_data = None

                if (
                    counterpart_id
                    and type(required) is not bool
                    and type(default) is not bool
                ):
                    print("Cai no CID")
                    data = (
                        db_connection.session.query(Contrapartida)
                        .filter_by(id=counterpart_id)
                        .one_or_none()
                    )
                    query_data = [data]

                elif (
                    not counterpart_id
                    and type(required) is bool
                    and type(default) is not bool
                ):
                    print("Cai no REQ")
                    data = (
                        db_connection.session.query(Contrapartida)
                        .filter_by(obrigatoria=required)
                        .all()
                    )

                    query_data = data

                elif (
                    not counterpart_id
                    and type(required) is not bool
                    and type(default) is bool
                ):
                    data = (
                        db_connection.session.query(Contrapartida)
                        .filter_by(padrao=default)
                        .all()
                    )
                    query_data = data

                elif (
                    counterpart_id
                    and type(required) is bool
                    and type(default) is not bool
                ):
                    data = (
                        db_connection.session.query(Contrapartida)
                        .filter_by(id=counterpart_id, obrigatoria=required)
                        .one_or_none()
                    )
                    query_data = [data]

                elif (
                    not counterpart_id
                    and type(required) is bool
                    and type(default) is bool
                ):
                    data = (
                        db_connection.session.query(Contrapartida)
                        .filter_by(padrao=default, obrigatoria=required)
                        .all()
                    )
                    query_data = data

                elif (
                    counterpart_id
                    and type(required) is not bool
                    and type(default) is bool
                ):
                    data = (
                        db_connection.session.query(Contrapartida)
                        .filter_by(id=counterpart_id, padrao=default)
                        .one_or_none()
                    )
                    query_data = [data]

                elif (
                    counterpart_id and type(required) is bool and type(default) is bool
                ):
                    data = (
                        db_connection.session.query(Contrapartida)
                        .filter_by(
                            id=counterpart_id, obrigatoria=required, padrao=default
                        )
                        .one_or_none()
                    )
                    query_data = [data]
                return query_data
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None
