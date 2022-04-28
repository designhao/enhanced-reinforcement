#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import os, sys, time, inspect, logging

# Constants
PATH        = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
DEFAULT_MAP = "maps/easy.txt"
HIGH_PROB   = 0.7
LOW_PROB    = 0.15
DEBUG       = lambda: logging.getLogger().level == logging.DEBUG
IS_DEBUG    = DEBUG()

MAX_TRAINING_EPISODES = 10000
CONVERGENCE_THRESHOLD = 0.1

# Frames per second (more means faster)
FPS         = 60

# Image files
PLAYER        = "link.bmp"
PLAYER_DEBUG  = "link_debug.bmp"
TILESET       = "link_tiles.bmp"
TILESET_DEBUG = "link_tiles_debug.bmp"

# Map (map values must match the following)
TILE_INIT         = 9
TILE_CLEAR        = 0
TILE_CLOSED       = 1
TILE_CHEST_CLOSED = 2
TILE_CHEST_OPENED = 3
TILE_BLUE_RUPEE   = 4
TERMINAL          = [TILE_CHEST_CLOSED, TILE_CHEST_OPENED]
INTE