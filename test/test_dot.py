from manimlib import *

class Minimal(Scene):
    def construct(self):
        dot = Dot()
        self.play(ShowCreation(dot))
        self.wait()