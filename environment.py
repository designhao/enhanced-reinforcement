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
      