from abc import abstractmethod
from typing import Generic, TypeVar

import numpy as np
from moderngl import Program, Uniform

T = TypeVar("T")


class ShaderUniform(Generic[T]):
    _name: str
    _uniform: Uniform

    def __init__(self, program: Program, name: str, *, default: T = None):
        self._name = name
        self._uniform = program[name]
        if default is not None:
            self.set(default)

    @abstractmethod
    def set(self, value: T):
        pass


class ShaderUniformFloat(ShaderUniform[float]):
    def set(self, value: float):
        self._uniform.value = value


class ShaderUniformArray(ShaderUniform[np.ndarray]):
    def set(self, value: np.ndarray):
        self._uniform.write(value.astype("f4"))
