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