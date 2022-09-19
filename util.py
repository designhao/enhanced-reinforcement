
import os, sys, time, inspect
from common import *

def read_map(filename):
    """
    Read map file, check its consistency, etc.
    """
    with open(os.path.join(PATH, filename)) as map_file:
        map_data = [[int(cell) for cell in row.rstrip()] for row in map_file]
        map_data = [list(x) for x in zip(*map_data)]
        map_width = len(map_data)
        map_height = len(map_data[0])
        for row in map_data:
            if len(row) != map_height:
                raise Exception("Map width does not match", map_height, len(row))
        for x in range(map_width):
            for y in range(map_height):
                cell = map_data[x][y]
                if cell not in ALL:
                    raise Exception("Unknown tile", cell)
                if cell == TILE_INIT:
                    map_data[x][y] = TILE_CLEAR
                    sx, sy = x, y