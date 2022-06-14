#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import sys, random, time, logging
from common import *
from util import *
from link import *

class Environment:

    def __init__(self, x, y, map_data, map_width, map_height, debug=False):

        self.init = self.state = (x, y)
        
        self.map_data   = map_data
        self.map_width  = map_width
        self.map_height = map_height

        self.rupees     = []
        
        self.debug      = debug
        
        self.rewards    = {
            TILE_CLEAR        : -1,
            TILE_CLOSED       : -0.1,
            TILE_CHEST_CLOSED : 50,
            TILE_BLUE_RUPEE   : 40
        }

    def execute(self, action):
        """
        Execute an agent's action and compute current state
        """
        # If the agent is in a state with a ruppe, it turns into a TILE_CLEAR
        if self.map_data[self.state[0]][self.state[1]] == TILE_BLUE_RUPEE:
            self.rupees.append(self.state)
            self.map_data[self.state[0]][self.state[1]] = TILE_CLEAR

        # If agent is in a terminal state, teleport him
        if self.te