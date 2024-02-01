from intelligence.objects import storage_cell

def store_input(cell: storage_cell, input: float):
    if cell.storage_limit >= input:
        cell.storage =+ input