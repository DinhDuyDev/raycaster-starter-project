            # side determination
            if side == 0: 
                perpWallDist = abs(sideDistX - deltaDistX)
            else: 
                perpWallDist = abs(sideDistY - deltaDistY)

            height = min(GameState.HEIGHT / (perpWallDist * height_scale), 1280)
            pygame.draw.rect(surf, (255, 0, 0) if side else (100, 0, 0), (
                i * column_width, GameState.HEIGHT / 2 - height/2, column_width, height
            ))