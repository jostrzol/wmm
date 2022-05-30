#version 330

uniform vec4 obj_color;
uniform vec4 diffuse_light_color;
uniform vec4 specular_light_color;
uniform float shininess;

in vec3 v_position;
in vec3 v_normal;
out vec4 f_color;

const vec3 light_position = vec3(10.0, 25.0, 0.0);

const vec4 ambient_light_color = vec4(0.5, 0.1, 0.2, 0.4);

const float ambient_strength = 0.4;
const float diffuse_strength = 0.5;
const float specular_strength = 0.4;

vec4 diffuse(vec3 normal, vec3 light_direction)
{
    // how much of the light is diffused (fraction)
    float light_fraction = max(dot(normal, -light_direction), 0.0);

    return diffuse_strength * light_fraction * diffuse_light_color;
}

vec4 specular(vec3 normal, vec3 light_direction)
{
    // unit vector pointing in the direction of reflected rays at the
    // current position
    vec3 reflected_light_direction = reflect(light_direction, normal);

    // how much of the light is reflected (fraction)
    float light_fraction = max(dot(reflected_light_direction, normal), 0);

    return specular_strength * pow(light_fraction, shininess) * specular_light_color;
}

void main()
{
    // due to interpolation normal has to be normalized once more
    vec3 normal = normalize(v_normal);
    // unit vector pointing from the light source to the current position
    vec3 light_direction = normalize(v_position - light_position);

    // calculate each light factor
    vec4 ambient_factor = ambient_strength * ambient_light_color;
    vec4 diffuse_factor = diffuse(normal, light_direction);
    vec4 specular_factor = specular(normal, light_direction);

    // sum of each factor multiplied by the object's color gives the final output
    f_color = (ambient_factor + diffuse_factor + specular_factor) * obj_color;
}
