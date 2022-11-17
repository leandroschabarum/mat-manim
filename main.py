from manim import *
import numpy as np

class StretchingTransformation(LinearTransformationScene):
    def construct(self):
        matrix = [[3, 1], [-1, 2]]

        self.setup()
        self.add_title("Alongando o espaço vetorial")

        grid = NumberPlane((-100, 100), (-100, 100))

        b_brace = Brace(self.i_hat, DOWN)
        l_brace = Brace(self.j_hat, LEFT)

        width = Tex('1')
        height = Tex('1')
        width.next_to(b_brace, DOWN)
        height.next_to(l_brace, LEFT)

        Create(grid)

        for mob in b_brace, width, l_brace, height:
            self.play(Write(mob, run_time = 0.3))

        self.wait()

        grid.add_background_rectangle()
        self.play(
            grid.animate.apply_matrix(np.array(matrix).transpose()),
            run_time=3
        )
        self.wait()

class SquishingTransformation(LinearTransformationScene):
    def construct(self):
        matrix = [[0.5, -0.3], [0.8, 0.25]]

        self.setup()
        self.add_title("Espremendo o espaço vetorial")

        grid = NumberPlane((-100, 100), (-100, 100))

        b_brace = Brace(self.i_hat, DOWN)
        l_brace = Brace(self.j_hat, LEFT)

        width = Tex('1')
        height = Tex('1')
        width.next_to(b_brace, DOWN)
        height.next_to(l_brace, LEFT)

        Create(grid)

        for mob in b_brace, width, l_brace, height:
            self.play(Write(mob, run_time = 0.3))

        self.wait()

        grid.add_background_rectangle()
        self.play(
            grid.animate.apply_matrix(np.array(matrix).transpose()),
            run_time=3
        )
        self.wait()

class ApplyingDeterminantTransformation(LinearTransformationScene):
    def getData(self):
        raise Exception('You MUST implement getData on your class.')

    def construct(self):
        self.setup()
        self.getData()

        if not hasattr(self, 'data'):
            raise Exception('Missing data!')

        grid = NumberPlane((-100, 100), (-100, 100))

        matrix = Matrix(np.array(self.data).transpose())
        matrix.next_to(ORIGIN, LEFT).to_edge(UP)
        matrix_background = BackgroundRectangle(matrix)

        b_brace = Brace(self.i_hat, DOWN)
        l_brace = Brace(self.j_hat, LEFT)

        width = Tex('1')
        height = Tex('1')
        width.next_to(b_brace, DOWN)
        height.next_to(l_brace, LEFT)

        Create(grid)
        sq_vert = [[0,0,0], [0,1,0], [1,1,0], [1,0,0]]
        unit_square = Polygon(*sq_vert, color=BLUE_E).set_fill(BLUE_E, opacity=0.5)
        self.add(unit_square, Text('A').move_to(unit_square.get_center()))

        self.play(
            Create(matrix_background),
            Write(matrix)
        )

        for mob in b_brace, width, l_brace, height:
            self.play(Write(mob, run_time = 0.5))

        self.wait()

        tdata = np.array(self.data).transpose()
        grid.add_background_rectangle()

        det_area = Polygon(*sq_vert, color=GREEN_E).set_fill(GREEN_E, opacity=0.5)
        det_val = Text("%.3f A" % np.linalg.det(self.data)).next_to(det_area.get_center(), RIGHT)

        self.play(
            grid.animate.apply_matrix(tdata),
            ApplyMatrix(tdata, det_area),
            run_time=3
        )
        self.add(det_val)
        self.wait()

class ExampleOne(ApplyingDeterminantTransformation):
    def getData(self):
        self.data = [[0.7, 0.8], [0.5, 1.2]]

class ExampleTwo(ApplyingDeterminantTransformation):
    def getData(self):
        self.data = [[1, 1], [1, 1]]

class ExampleThree(ApplyingDeterminantTransformation):
    def getData(self):
        self.data = [[1, 0.5], [0.3, 1]]

class ExampleFour(ApplyingDeterminantTransformation):
    def getData(self):
        self.data = [[-0.7, 0.8], [-0.5, 1.2]]

class ExampleFive(ApplyingDeterminantTransformation):
    def getData(self):
        self.data = [[0.7, -0.8], [0.5, -1.2]]
