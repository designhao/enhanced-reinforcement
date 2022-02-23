#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import math, copy, random, logging
from common import *
from util import *

class Agent:

    def __init__(self):
        self.s = self.a = self.r = None
        self.utility_table = {}
        self.prev_utility_table = {}

    def reset(self, env):
        self.s = env.init

    def train(self, env):
        """
        Execute MAX_TRAINING_EP