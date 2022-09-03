
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

        screen = pygame.display.set_mode((TILE_WIDTH * self.env.map_width + TILE_WIDTH * 2, TILE_HEIGHT * self.env.map_height + TILE_HEIGHT * 2))
        pygame.display.set_caption("[T2] Link's Learning")

        prev_x, prev_y = self.env.init
        sx, sy = self.env.init

        self.setup_tiles()
        self.setup_agent()
        self.setup_agent_pos(prev_x, prev_y)
        self.compute_range()

        around, background, interactive = self.draw_changes()
        contour = self.draw_contour()

        # Loop
        clock = pygame.time.Clock()
        game_over = False
        while not game_over:

            screen.blit(around, (0, 0))
            screen.blit(background, (TILE_WIDTH, TILE_HEIGHT))
            screen.blit(interactive, (TILE_WIDTH, TILE_HEIGHT))
            DEBUG() and screen.blit(contour, (TILE_WIDTH, TILE_HEIGHT))
