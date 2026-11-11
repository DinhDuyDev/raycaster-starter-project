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

    def render(self, surf: pygame.Surface, resolution):
        column_width = GameState.WIDTH / resolution
        height_scale = 3

        posX = self.x / GameState.CELL_WIDTH
        posY = self.y / GameState.CELL_WIDTH

        for i in range(resolution):
            mapPosX = int(self.x / GameState.CELL_WIDTH)
            mapPosY = int(self.y / GameState.CELL_WIDTH)
            cameraX = 2 * (i / resolution) - 1
            rayDirX = self.dirX + self.planeX * cameraX
            rayDirY = self.dirY + self.planeY * cameraX

            deltaDistX = 1e30 if rayDirX == 0 else abs(1/rayDirX)
            deltaDistY = 1e30 if rayDirY == 0 else abs(1/rayDirY)

            perpWallDist = -1
            sideDistX = -1
            sideDistY = -1

            stepX = -1
            stepY = -1

            hit = False
            side = 0

            if rayDirX < 0:
                stepX = -1
                sideDistX = (posX - mapPosX) * deltaDistX
            else:
                stepX = 1
                sideDistX = (mapPosX + 1.0 - posX) * deltaDistX


            if rayDirY < 0:
                stepY = -1
                sideDistY = (posY - mapPosY) * deltaDistY
            else:
                stepY = 1
                sideDistY = (mapPosY + 1.0 - posY) * deltaDistY

            while not hit:
                if sideDistX < sideDistY:
                    sideDistX += deltaDistX
                    mapPosX += stepX
                    side = 0
                else:
                    sideDistY += deltaDistY
                    mapPosY += stepY
                    side = 1
                
                if GameState.map_geometry[mapPosY][mapPosX] != 0:
                    hit = True

                    # side determination
            if side == 0: 
                perpWallDist = abs(sideDistX - deltaDistX)
            else: 
                perpWallDist = abs(sideDistY - deltaDistY)

            height = min(GameState.HEIGHT / (perpWallDist * height_scale), 1280)
            pygame.draw.rect(surf, (255, 0, 0) if side else (100, 0, 0), (
                i * column_width, GameState.HEIGHT / 2 - height/2, column_width, height
            ))

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