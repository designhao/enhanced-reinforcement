
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
        TODO: you can change this method to log executions
        """

        logging.getLogger().debug("It will converge at %f", CONVERGENCE_THRESHOLD)

        self.reset(env)
        self.env = env
        executions = 0
        while executions < MAX_TRAINING_EPISODES:
            action = self.run_train(self.env)
            self.env.execute(action)
            if env.terminal(self.state):
                executions += 1
                
                self.reset(env)

                if self.converged():
                    break
                else:
                    self.prev_qtable = copy.deepcopy(self.q_values)

                logging.getLogger().debug("Episode %d: convergence %f", executions, self.convergence)

        logging.getLogger().info("Episode %d: converged at %f", executions, self.convergence)

    def alpha(self, qv):
        """
        Learning rate
        TODO: set a learning rate function or a fixed number
        """
        raise NotImplementedError
        
    
    def reset(self, game):
        self.p_state = self.p_action = self.p_reward = self.state = self.action = self.reward = None

    def f(self, qv):
        """
        Exploration function
        TODO: implement a exploration function
        """
        raise NotImplementedError 

        