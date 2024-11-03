from sqlalchemy import text
from src.constants.reference import REFERENCE_TABLE
from src.infra.config.db_config import DBConnectionHandler

db_connection_handler = DBConnectionHandler()


class FakerRepo:
    """A simple Repository"""

    @classmethod
    def insert_contrapartida(cls):
        """something"""

        texto = """Aplicação da logomarca da PATROCINADORA em todos os materiais de divulgação,
        comunicação e mídia do Projeto Patrocinado (incluindo postagens em redes sociais, releases
        oficiais, materiais gráficos, cenografia, entre outros"""

        # SQL COmmands
        engine = db_connection_handler.get_engine()
        with engine.begin() as conn:
            conn.execute(
                text(
                    """INSERT INTO {}_contrapartida (descricao, exemplo_aplicabilidade, obrigatoria, padrao)
                    VALUES ( {}, 'True', 'True');""".format(
                        texto, REFERENCE_TABLE
                    )
                )
            )
            conn.commit()
