#version 330

uniform vec4 obj_color;

in vec3 v_position;
out vec4 f_color;

void main()
{
    f_color = obj_color;
}
