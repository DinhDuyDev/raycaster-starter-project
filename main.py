##### DEMO FOR TEXTURE MAPPING
import pygame
import math

pygame.init()
pygame.font.init()

# GAME STATE
class GameState:
    gameBuff: list[pygame.Surface] = []
    WIDTH = 640
    HEIGHT = 360
    CELL_WIDTH = 32

    # Map geometry
    map_geometry = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]

# GAME SETUP
screen = pygame.display.set_mode((GameState.WIDTH, GameState.HEIGHT), pygame.RESIZABLE|pygame.DOUBLEBUF|pygame.SRCALPHA|pygame.SCALED|pygame.FULLSCREEN, vsync=1)
draw_dest = screen.copy()
debug_font = pygame.sysfont.SysFont("Arial", 10, False)
pygame.mouse.set_visible(False)

# FPS
clock = pygame.Clock()
GAME_FPS = 60

# PLAYER
class Player:
    def __init__(self, x=48, y=48):
        self.x = x
        self.y = y

        self.fov_factor = abs(math.tan(45))
        self.dirX = -1.0
        self.dirY = 0.0
        self.planeX = 0
        self.planeY = self.fov_factor
    
    def rotate(self, deg: float):
        oldDirX = self.dirX
        self.dirX = self.dirX * math.cos(math.radians(deg)) - self.dirY * math.sin(math.radians(deg))
        self.dirY = oldDirX * math.sin(math.radians(deg)) + self.dirY * math.cos(math.radians(deg))

        self.planeX = self.dirY * self.fov_factor
        self.planeY = -self.dirX * self.fov_factor

    def render(self, surf: pygame.Surface, resolution: int):
        # implement the whole thing here
        # files {a -> c}.py will contain all the parts for this project to work.
        # re-order the code correctly, and see the project run!
        pass

    def move_straight(self, dir: int):
        player_obj.x += player_obj.dirX * dir
        player_obj.y += player_obj.dirY * dir

player_obj = Player()


# game
def game():
    running = True
    while running:
        # Game loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Player movement
        player_obj.rotate((keys[pygame.K_a] - keys[pygame.K_d]) * 3)
        player_obj.move_straight(keys[pygame.K_w] - keys[pygame.K_s])

        # Display
        draw_dest.fill((50, 50, 50))

        # Render
        player_obj.render(draw_dest, 320)

        # UI
        pygame.draw.circle(draw_dest, (255, 0, 0), (GameState.WIDTH/2, GameState.HEIGHT/2), radius=5, width=1)

        screen.blit(pygame.transform.scale(draw_dest, (screen.get_width(), screen.get_height())), (0, 0))

        pygame.display.flip()
        clock.tick(GAME_FPS)

if __name__ == "__main__":
    game()