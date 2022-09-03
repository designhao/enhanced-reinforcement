
#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import sys, time, math, pygame, logging
from pygame.locals import (QUIT, KEYDOWN, K_SPACE, K_ESCAPE)
from common import *
from util import *
from environment import *

class Game:

    def __init__(self, env, agt):
        self.env = env
        self.agt = agt

        pygame.init()