import moderngl
from pyrr import Matrix44

from base_window import BaseWindowConfig


class PhongWindow(BaseWindowConfig):

    def __init__(self, **kwargs):
        super(PhongWindow, self).__init__(**kwargs)

    def model_load(self):
        self.obj = self.load_scene("cube.obj")
        self.vao = self.obj.root_nodes[0].mesh.vao.instance(self.program)

    def init_shaders_variables(self):
        self.obj_color = self.program["obj_color"]
        self.pvm_matrix = self.program["pvm_matrix"]

    def render(self, time: float, frame_time: float):
        self.ctx.clear(1.0, 1.0, 1.0, 0.0)
        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        proj = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        lookat = Matrix44.look_at(
            (3.0, 1.0, -5.0),
            (0.0, 0.0, 1.0),
            (0.0, 0.0, 1.0),
        )
        # TODO: Write variables to shader
        self.vao.render()
