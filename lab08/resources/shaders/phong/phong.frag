#version 330

uniform vec4 obj_color;

in vec3 v_position;
out vec4 f_color;

void main()
{
    f_color = obj_color;

//    f_color = vec4(v_position, 1.0);
}
