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