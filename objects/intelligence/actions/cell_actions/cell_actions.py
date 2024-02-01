from intelligence.objects import cell, storage_cell, connection, intermediate_cell
from intelligence.actions import cell_environment_actions, storage_cell_actions
from typing import List
from statistics import mean

def search_for_connection(cell: cell, volume: float):
    closest_cell = cell_environment_actions.find_closest_cell(cell)
    if closest_cell is None:
        closest_cell = storage_cell()
        closest_cell.storage = volume
    return closest_cell
    
def add_connection(cell: cell, other_cell: cell, strength: float):
    _connection = connection()
    _connection.other_side = other_cell
    _connection.strength = strength
    cell.connections.append(_connection)

def act(inputs: List[int]):
    # I don't have another idea for how to calculate it
    return mean(inputs)

def cell_input(cell: cell, input: float):
    match cell:
        case storage_cell():
            storage_cell_actions.store_input(cell, input)
        case intermediate_cell():
            pass
    
            
def cell_output(cell: cell):
    outputs = []
    for connection in cell.connections:
        other_cell = connection.other_side
        outputs.append(cell_output(other_cell))
    return act(outputs)

def cell_got_hit(cell: cell, hit: int):
    cell_input(cell, input=-hit)

def cell_got_love(cell: cell, love: int):
    cell_input(cell, input=love)