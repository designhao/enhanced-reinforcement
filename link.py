
#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import math, copy, random, logging
# import qvalue
# from qvalue import *
from common import *
from util import *
from agent import *

class Link(Agent):

    def __init__(self):

        Agent.__init__(self)
        self.q_values = dict()
        self.frequency = dict()
        self.prev_qtable = dict()
        self.p_state = self.p_action = self.p_reward = self.state = self.action = self.reward = None
        self.gamma = 0.9
        self.env = None

    
    ################-------------------###################

    def train(self, env):
        """
        Execute MAX_TRAINING_EPISODES rounds or until converge.