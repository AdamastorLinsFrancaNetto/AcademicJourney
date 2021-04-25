from obj import Obj

class Game:

    def __init__(self):

        self.bg = Obj("assets/espaco.png",0,0)
        self.bg2 = Obj("assets/espaco.png", 0, -960)
        self.nave = Obj("assets/nave1.png",640,800)
        self.change_scene = False

    def draw(self,window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.nave.drawing((window))

    def update(self):
        self.move_bg()
        self.nave.amin()

    def move_bg(self):
        self.bg.sprite.rect[1] += 1
        self.bg2.sprite.rect[1] += 1

        if self.bg.sprite.rect[1] >= 960:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -960
