varying vec3 vertex_light_position;
varying vec3 vertex_light_half_vector;
varying vec3 vertex_normal;

void main() {
	vec4 mat_ambient = vec4(0.1, 0.1, 0.1, 1.0);
	vec4 mat_specular = vec4(1.0, 1.0, 1.0, 1.0);	
	vec4 ambient_color = mat_ambient * gl_LightSource[0].ambient;

	vec3 diffuse_color = gl_Color.rgb * gl_LightSource[0].diffuse.rgb;
	float diffuse_value = max(dot(vertex_normal, vertex_light_position), 0.0);
	
	gl_FragColor.rgb = diffuse_color * diffuse_value;
	gl_FragColor.a = gl_Color.a;
}