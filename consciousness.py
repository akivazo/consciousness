from ..concept import concept
from .objects.sensor import sensor
from .objects.intelligence import intelligence
from .objects.resource import resource
from ..external_object import external_object
from typing import List, Mapping


class consciousness:
    sensors: List[sensor]
    others: List[concept]
    intelligence: intelligence
    resources: List[resource]
    object_to_concepts_map: Mapping[external_object, List[concept]]