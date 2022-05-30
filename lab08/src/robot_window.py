import dataclasses
from typing import Literal

import moderngl
from pyrr import Matrix44, Vector4, Vector3
from math import pi

from base_window import BaseWindowConfig


@dataclasses.dataclass
class Item:
    type: Literal["sphere", "cube"]
    translation: Vector3 = Vector3((0.0, 0.0, 0.0))
    color: Vector4 = Vector4((0.0, 0.0, 0.0, 0.0))
    scale: Vector3 = Vector3((1.0, 1.0, 1.0))
    rotation: Vector3 = Vector3((0.0, 0.0, 0.0))


class RobotWindow(BaseWindowConfig):

    def __init__(self, **kwargs):
        super(RobotWindow, self).__init__(**kwargs)
        self.items = {
            "head": Item(
                "sphere",
                translation=Vector3((0.0, 0.0, 5.0)),
                color=Vector4((1.0, 0.0, 1.0, 0.0)),
            ),
            "body": Item(
                "cube",
                translation=Vector3((0.0, 0.0, 2.0)),
                color=Vector4((0.0, 1.0, 1.0, 0.0)),
                scale=Vector3((1.0, 1.0, 2.0)),
            ),
            "l_arm": Item(
                "cube",
                translation=Vector3((0.0, -3.0, 3.0)),
                color=Vector4((0.5, 0.5, 1.0, 0.0)),
                scale=Vector3((0.5, 0.5, 1.25)),
                rotation=Vector3((pi/4, 0.0, 0.0)),
            ),
            "r_arm": Item(
                "cube",
                translation=Vector3((0.0, 3.0, 3.0)),
                color=Vector4((1.0, 0.0, 1.0, 0.0)),
                scale=Vector3((0.5, 0.5, 1.25)),
                rotation=Vector3((-pi/4, 0.0, 0.0)),
            ),
            "l_leg": Item(
                "cube",
                translation=Vector3((0.0, -2.0, -1.5)),
                color=Vector4((1.0, 0.5, 1.0, 0.0)),
                scale=Vector3((0.5, 0.5, 1.75)),
                rotation=Vector3((pi/6, 0.0, 0.0)),
            ),
            "r_leg": Item(
                "cube",
                translation=Vector3((0.0, 2.0, -1.5)),
                color=Vector4((0.5, 0.5, 0.5, 0.0)),
                scale=Vector3((0.5, 0.5, 1.75)),
                rotation=Vector3((-pi/6, 0.0, 0.0)),
            ),
        }

    def model_load(self):
        self.objs = {
            "sphere": self.load_scene("sphere.obj"),
            "cube": self.load_scene("cube.obj"),
        }
        self.vaos = {
            name: obj.root_nodes[0].mesh.vao.instance(self.program)
            for name, obj in self.objs.items()
        }

    def init_shaders_variables(self):
        self.obj_color = self.program["obj_color"]
        self.pvm_matrix = self.program["pvm_matrix"]

    def render(self, time: float, frame_time: float):
        self.ctx.clear(0.8, 0.8, 0.8, 0.0)
        self.ctx.enable(moderngl.DEPTH_TEST)

        projection = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        lookat = Matrix44.look_at(
            (-20.0, -10.0, 5.0),
            (0.0, 0.0, 1.0),
            (0.0, 0.0, 1.0),
        )
        # scale_matrix = Matrix44.from_scale((2.0, 1.0, 1.0))
        # Matrix44.from_x_rotation
        # pvm_matrix = projection * lookat * scale_matrix

        for item in self.items.values():
            translation = Matrix44.from_translation(item.translation)
            scale = Matrix44.from_scale(item.scale)

            rotation_x = Matrix44.from_x_rotation(item.rotation[0])
            rotation_y = Matrix44.from_y_rotation(item.rotation[1])
            rotation_z = Matrix44.from_z_rotation(item.rotation[2])
            rotation = rotation_x * rotation_y * rotation_z

            pvm_matrix = projection * lookat * translation * rotation * scale

            self.pvm_matrix.write(pvm_matrix.astype("f4"))
            self.obj_color.write(item.color.astype("f4"))

            self.vaos[item.type].render()
