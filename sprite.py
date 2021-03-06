import pygame
from utilitaries import *

class Sprite():

    def __init__(self, filename: str, cols, rows, scale=1, selection=None, colorkey=True):

        self.sheet = pygame.image.load(filename)
        if colorkey:
            self.sheet = pygame.image.load(filename).convert()
            self.sheet.set_colorkey(self.sheet.get_at((0,0)))

        self.scale = scale
        self.sheet = pygame.transform.scale(self.sheet,
                                            (int(self.sheet.get_rect().width * self.scale),
                                             int(self.sheet.get_rect().height * self.scale ))
                                            )

        self.sheetFlip = pygame.transform.flip(self.sheet, True, False)

        self.cols = cols
        self.rows = rows
        self.totalCells = self.rows * self.cols if not selection else selection[1]

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / self.cols
        h = self.cellHeight = self.rect.height / self.rows
        center_w, center_h = self.centerCell = w/2, h/2

        if selection:
            self.cells = [(i % self.cols * w, selection[1] % self.rows * h, w, h) for i in range(selection[0])]

        else:
            self.cells = [(i % self.cols * w, i % self.rows * h, w, h) for i in range(self.totalCells)]

        self.handle = [
            (0, 0), (-center_w, 0), (-w, 0),
            (0, -center_h), (-center_w, -center_h), (-w, -center_h),
            (0, -h), (-center_w, -h), (-h, -w)
        ]

        self.cellIndex = 0

    def draw(self, surface, x, y, flip=False, handle=7):

        cell = pygame.Rect(self.cells[0]) if self.totalCells > 1 else 1

        if not flip:

            if cell:
                self.cellIndex = (self.cellIndex + 1) % len(self.cells)
                cell = pygame.Rect(self.cells[self.cellIndex])

            surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), cell)

        else:

            if cell:
                self.cellIndex = (self.cellIndex - 1) % len(self.cells)
                cell = pygame.Rect(self.cells[self.cellIndex])

            surface.blit(self.sheetFlip, (x + self.handle[handle][0], y + self.handle[handle][1]), cell)
