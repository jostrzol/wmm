#version 330

uniform mat4 pvm_matrix;

in vec3 in_position;
out vec3 v_position;

void main() {
    gl_Position = pvm_matrix * vec4(in_position, 1.0);
    v_position = in_position;
}