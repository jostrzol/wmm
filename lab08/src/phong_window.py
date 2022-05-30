import moderngl
from pyrr import Matrix44, Vector4

from base_window import BaseWindowConfig
from shaders.shader_uniform import ShaderUniformArray, ShaderUniformFloat


class PhongWindow(BaseWindowConfig):
    pvm_matrix: ShaderUniformArray
    obj_color: ShaderUniformArray
    diffuse_light_color: ShaderUniformArray
    specular_light_color: ShaderUniformArray
    shininess: ShaderUniformFloat

    def __init__(self, **kwargs):
        super(PhongWindow, self).__init__(**kwargs)

    def init_shaders_variables(self):
        self.pvm_matrix = ShaderUniformArray(
            self.program, "pvm_matrix")

        self.obj_color = ShaderUniformArray(
            self.program, "obj_color",
            default=Vector4((0.5, 0.0, 1.0, 0.0)))
        self.diffuse_light_color = ShaderUniformArray(
            self.program, "diffuse_light_color",
            default=Vector4((0.5, 0.7, 0.4, 0.8)))
        self.specular_light_color = ShaderUniformArray(
            self.program, "specular_light_color",
            default=Vector4((1, 1, 1, 1)))

        self.shininess = ShaderUniformFloat(
            self.program, "shininess", default=5)

    def render(self, time: float, frame_time: float):
        self.ctx.clear(1.0, 1.0, 1.0, 0.0)
        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        projection = Matrix44.perspective_projection(
            45.0, self.aspect_ratio, 0.1, 1000.0)
        lookat = Matrix44.look_at(
            (3.0, 1.0, -5.0),
            (0.0, 0.0, 1.0),
            (0.0, 0.0, 1.0),
        )

        pvm_matrix = projection * lookat

        self.pvm_matrix.set(pvm_matrix)

        self.vao.render()
