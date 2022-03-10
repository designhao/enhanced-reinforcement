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
        Execute MAX_TRAINING_EPISODES rounds or until converge.
        """

        logging.getLogger().debug("It will converge at %f", CONVERGENCE_THRESHOLD)

        self.reset(env)

        executions = 0
        while executions < MAX_TRAINING_EPISODES:

            self.prev_s, self.prev_a, self.prev_r = self.s, self.a, self.r

            self.run_train(env)

            if env.terminal(self.s):

                executions += 1
                
                self.prev_s = self.prev_a = self.prev_r = self.s = self.a = self.r = None
                self.reset(env)

                if self.converged():
                    break
                else:
                    self.prev_utility_table = copy.deepcopy(self.utility_table)

                logging.getLogger().debug("Episode %d: convergence %f", 