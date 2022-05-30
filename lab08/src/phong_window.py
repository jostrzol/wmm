import moderngl
from pyrr import Matrix44, Vector4

from base_window import BaseWindowConfig


class PhongWindow(BaseWindowConfig):

    def __init__(self, **kwargs):
        super(PhongWindow, self).__init__(**kwargs)

        self.item_color = Vector4((0.5, 0.0, 1.0, 0.0))
        # self.item_shininess = 0.2

    def model_load(self):
        self.obj = self.load_scene("sphere.obj")
        self.vao = self.obj.root_nodes[0].mesh.vao.instance(self.program)

    def init_shaders_variables(self):
        self.obj_color = self.program["obj_color"]
        self.pvm_matrix = self.program["pvm_matrix"]
        # self.shininess = self.program["shininess"]

    def render(self, time: float, frame_time: float):
        self.ctx.clear(1.0, 1.0, 1.0, 0.0)
        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        projection = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        lookat = Matrix44.look_at(
            (3.0, 1.0, -5.0),
            (0.0, 0.0, 1.0),
            (0.0, 0.0, 1.0),
        )

        pvm_matrix = projection * lookat

        self.pvm_matrix.write(pvm_matrix.astype("f4"))
        self.obj_color.write(self.item_color.astype("f4"))
        # self.shininess.write(self.item_shininess.astype("f4"))

        self.vao.render()
