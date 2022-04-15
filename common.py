#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import os, sys, time, inspect, logging

# Constants
PATH        = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
DEFAULT_MAP = "maps/easy.txt"
HIGH_PROB   = 0.7
LOW_PROB    = 0.15
DEBUG       = lambda: