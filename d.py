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