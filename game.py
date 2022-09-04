
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
                        if DEBUG():
                            logging.getLogger().setLevel(logging.INFO)
                        else:
                            logging.getLogger().setLevel(logging.DEBUG)
                        around, background, interactive = self.draw_changes()

    def draw_changes(self):
        """
        Draw changes in scenario.
        """
        around = self.draw_around()
        background = self.draw_map()
        interactive = self.draw_interactive()
        return around, background, interactive

    def draw_contour(self):
        """
        Draw map contour.
        """
        contour = pygame.Surface((TILE_WIDTH * self.env.map_width, TILE_HEIGHT * self.env.map_height), pygame.SRCALPHA, 32).convert_alpha()
        for x in xrange(self.env.map_width):
            for y in xrange(self.env.map_height):
                tile = self.env.map_data[x][y]

                x0, y0 = TILE_WIDTH * x, TILE_HEIGHT * y
                x1, y1 = x0 + TILE_WIDTH, y0 + TILE_HEIGHT
                border = 1

                if tile not in VALID:
                    lines = {
                        MOVE_RIGHT: ((x1, y0), (x1, y1)),
                        MOVE_LEFT: ((x0, y0), (x0, y1)),
                        MOVE_DOWN: ((x0, y1), (x1, y1)),
                        MOVE_UP: ((x0, y0), (x1, y0)),
                    }
                    for s in successors((x, y), self.env.map_data, self.env.map_width, self.env.map_height):
                        xn, yn = s
                        d = direction(x, y, xn, yn)
                        line_from, line_to = lines[d]
                        pygame.draw.line(contour, (255, 255, 255), line_from, line_to, border)

        pygame.draw.rect(contour, (255, 255, 255), [0, 0, TILE_WIDTH * self.env.map_width, TILE_HEIGHT * self.env.map_height], 1)
        return contour

    def draw_map(self):
        """
        Draw map and, if on debug, q-states.
        """
        background = pygame.Surface((TILE_WIDTH * self.env.map_width, TILE_HEIGHT * self.env.map_height)).convert()
        for x in xrange(self.env.map_width):
            for y in xrange(self.env.map_height):
                tile = self.env.map_data[x][y]
                if not DEBUG():
                    if tile == TILE_BLUE_RUPEE:
                        background.blit(self.tileset[0][TILE_CLEAR], (TILE_WIDTH * x, TILE_HEIGHT * y))
                    background.blit(self.tileset[0][tile], (TILE_WIDTH * x, TILE_HEIGHT * y))
                    continue

                x0, y0 = TILE_WIDTH * x, TILE_HEIGHT * y
                x1, y1 = x0 + TILE_WIDTH, y0 + TILE_HEIGHT
                xh, yh = x0 + math.floor(TILE_WIDTH / 2), y0 + math.floor(TILE_HEIGHT / 2)
                border = 1

                if tile not in VALID:
                    pygame.draw.rect(background, (0, 0, 0), [TILE_WIDTH * x, TILE_HEIGHT * y, TILE_WIDTH, TILE_HEIGHT], 0)
                else:
                    pass                    
                    #triangs = [
                    #    ( MOVE_LEFT, [[x0, y0], [x0, y1], [xh, yh]] ),
                    #    ( MOVE_RIGHT, [[x1, y0], [x1, y1], [xh, yh]] ),
                    #    ( MOVE_DOWN, [[x0, y1], [x1, y1], [xh, yh]] ),
                    #    ( MOVE_UP, [[x0, y0], [x1, y0], [xh, yh]] ),
                    #]
                    #action = self.agt.argmaxAPrime((x,y))
                    #act, poly = triangs[action]
                    #c = 120
                    #pygame.draw.polygon(background, (c,c,c), poly, 0)


                    #for t in triangs:
                        #act, poly = t
                        #v = self.agt.return_qvalue(QValue((x,y), act))
                        #c = self.scale_range(v, 1, self.max_expl, 0, 255)
                        #print 'C: ', c