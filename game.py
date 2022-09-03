
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

            if not self.update_agent(screen):

                _, new_state = self.agt.run(self.env)
                sx, sy = new_state

                if self.env.terminal((prev_x, prev_y)):
                    # Setup Link to the initial state
                    prev_x, prev_y = sx, sy = self.env.init
                    self.setup_agent_pos(sx, sy)
                else:
                    # Get the action based on the Link new coordinates
                    action = direction(prev_x, prev_y, sx, sy)
                    if action is not None:
                        self.agent_action = action
                        prev_x, prev_y = sx, sy

                around, background, interactive = self.draw_changes()

            pygame.display.flip()
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_over = True
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE: