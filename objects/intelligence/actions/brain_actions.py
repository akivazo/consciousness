from intelligence.objects import brain, external_object, storage_cell
from intelligence.actions import cell_actions

def create_new_external_input_cell(brain: brain):
    return storage_cell()

def init(brain: brain):
    brain.external_object_to_input_cells = {}

def brain_got_hit(brain: brain, external_object: external_object, hit: int):
    try:
        for input_cell in brain.external_object_to_input_cells[external_object]:
            cell_actions.cell_got_hit(input_cell, hit)
    except KeyError:
        brain.external_object_to_input_cells[external_object] = create_new_external_input_cell()

def brain_got_love(brain: brain, external_object: external_object, love: int):
    try:
        for cell in brain.external_object_to_input_cells[external_object]:
            cell_actions.cell_got_love(cell, love)
    except KeyError:
        brain.external_object_to_input_cells[external_object] = create_new_external_input_cell()
