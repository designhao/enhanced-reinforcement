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
        if self.terminal(self.state):
            self.reset()
        else:
            self.state = self.compute_action_result(self.state, action)

        return (self.state, self.state_reward(self.state))

    def reset(self):
        """
        Reset the agent to the initial state.
        """
        self.state = self.init
        for rupee in self.rupees:
            self.map_data[rupee[0]][rupee[1]] = TILE_BLUE_RUPEE
        self.rupees = []
        
    def compute_action_result(self, state, action):
        """
        Compute the resulting state given the action probabilities.
        """
        successors = self.successor_states(state, action)
        total = sum(w for c, w in successors)
        r = random.uniform(0, total)
        upto = 0
        for c, w in successors:
            if upto + w > r:
                return c
            upto += w
        raise Exception("Fail action")

    def successor_states(self, state, action):
        """
        Return a list with states and probs: [((x, y), prob), ...]
        """
        succ_states = []
        failprob = 0
        available_states = self.available_actions(state)

        for a in ACTIONS:
            
            if action == a:
                if action in available_states:
                    succ_states.append(( newstate(state, a), HIGH_PROB ))
                else:
                    failprob += HIGH_PROB
            elif orthogonal(action, a):
                if a in available_states:                
                    succ_states.append(( newstate(state, a), LOW_PROB ))
                else:
                 