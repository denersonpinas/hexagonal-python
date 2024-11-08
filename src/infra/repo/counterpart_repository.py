from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Contrapartida

class CounterpartRepository:
    '''Class to manage Counterpart Repository'''

    @classmethod
    def insert_counterparts(cls, descricao: str, exemplo_aplicabilidade: str, obrigatoria: bool) -> Contrapartida:
        '''Insert data in counterpart entity
        :param  -   descricao: counterpart description
                -   exemplo_aplicabilidade: counterpart example
                -   obrigatoria:    if requirement
                -   padrao: if default
        :return -   tuple with counterparts inserted
        '''

        InsertDataOutput = namedtuple('Counterparts', 'id, descricao, exemplo_aplicabilidade, obrigatoria, padrao')

        with DBConnectionHandler() as db_connection:
            try:
                new_counterpart = Contrapartida(descricao=descricao, exemplo_aplicabilidade=exemplo_aplicabilidade, obrigatoria=obrigatoria, padrao=True)
                db_connection.session.add(new_counterpart)
                db_connection.session.commit()

                return InsertDataOutput(id=new_counterpart.id, descricao=new_counterpart.descricao, exemplo_aplicabilidade=new_counterpart.exemplo_aplicabilidade, obrigatoria=new_counterpart.obrigatoria, padrao=new_counterpart.padrao)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        
        return None
