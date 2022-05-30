#version 330

uniform vec4 obj_color;

in vec3 v_position;
in vec3 v_normal;
out vec4 f_color;

const vec3 light_position = vec3(10.0, 25.0, 0.0);

const vec4 light_ambient_color = vec4(0.5, 0.1, 0.2, 0.4);
const float ambient_strength = 0.4;

const vec4 light_diffuse_color = vec4(0.5, 0.7, 0.4, 0.8);
const float diffuse_coefficient = 0.5;

const float shininess = 0.2;
const float shine_coefficient = 0.4;

void main()
{
    vec3 normal = normalize(v_normal);

    vec3 position_to_light_source = vec3(light_position - v_position);
    vec3 light_direction = normalize(position_to_light_source);

    vec4 diffuse_factor = max(dot(normal, light_direction), 0.0) * light_diffuse_color;
    vec4 ambient_factor = ambient_strength * light_ambient_color;

    f_color = (ambient_factor + diffuse_factor) * obj_color;
}
