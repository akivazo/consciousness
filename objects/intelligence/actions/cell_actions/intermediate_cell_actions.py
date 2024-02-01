from intelligence.objects import intermediate_cell
from intelligence.actions.cell_actions import add_connection, search_for_connection

def forward_input(cell: intermediate_cell, input: float):
    if len(cell.connections) == 0:
        add_connection(cell, search_for_connection(cell, input), strength=input)
    strongest_connection = max(cell.connections, key=lambda connection: connection.strength)
    next_cell = strongest_connection.other_side

    