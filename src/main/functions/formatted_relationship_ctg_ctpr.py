from typing import Dict, List, Type

from src.domain.models import RelationshipCategoryCounterparts


def formatted_relationship_ctg_ctpr(
    data: Type[List[RelationshipCategoryCounterparts]],
) -> List[Dict]:
    """Formated List RelationshipCategoryCounterparts Object in Dict
    :param      -   data: List Object of the RelationshipCategoryCounterparts
    :return     -   Dict with RelationshipCategoryCounterparts formatted
    """

    relationship_category_counterparts = []

    for item in data:
        relationship_category_counterparts.append(
            {
                "id": item.id,
                "categoria_id": item.categoria_id,
                "contrapartida_id": item.contrapartida_id,
            }
        )

    return relationship_category_counterparts
