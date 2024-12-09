from typing import Dict, List, Type

from src.domain.models import AbginvestTpprojLei


def formatted_abginvest_tpproj_lei(
    data: Type[List[AbginvestTpprojLei]],
) -> List[Dict]:
    """Formated List AbginvestTpprojLei Object in Dict
    :param      -   data: List Object of the AbginvestTpprojLei
    :return     -   Dict with AbginvestTpprojLei formatted
    """

    abginvest_tpproj_lei = []

    for item in data:
        abginvest_tpproj_lei.append(
            {
                "id": item.id,
                "abordagem_investimento_id": item.abordagem_investimento_id,
                "lei_id": item.lei_id,
                "tipo_pojeto_id": item.tipo_pojeto_id,
            }
        )

    return abginvest_tpproj_lei
