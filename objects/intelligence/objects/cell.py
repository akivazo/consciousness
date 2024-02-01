from intelligence.objects import connection
from intelligence.objects import cell_environment
from typing import List


class cell:
    connections: List[connection]
    environment: cell_environment

class intermediate_cell(cell):
    pass

class storage_cell(cell):
    storage: float
    storage_limit: float

