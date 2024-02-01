
from .consciousness import consciousness
from .objects.sensor import sensor_actions
from .objects.intelligence import intelligence_actions
from .objects.resource import resource_actions
from ..concept import concept


def get_aware(consciousness: consciousness):
    detected_objects = map(sensor_actions.detect, consciousness.sensors)
    related_concepts = []
    for object in detected_objects:
        related_concept = None
        try:
            related_concept = consciousness.object_to_concepts_map[object]
        except KeyError:
            related_concept = related_concept
            

    conclusions = map(detected_objects, intelligence_actions.think)
    for conclusion in conclusions:
        for resource, pulse in conclusion.actions:
            resource_actions.activate(resource, pulse)
        
def get_afraid(consciousness: consciousness):
    pass

def get_happy(consciousness: consciousness):
    pass

def think(consciousness: consciousness):
    pass
