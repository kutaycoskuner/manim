from manimlib import *

class FunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-3, 3),
            y_range=(-1, 5),
        )

        graph = axes.get_graph(lambda x: x**2)

        self.play(ShowCreation(axes))
        self.play(ShowCreation(graph))
        self.wait()
