#version 460 


in vec3 in_position; //координаты вершин экранной плоскости(передаются из буфера вершин)


void main(){
    gl_Position = vec4(in_position, 1);

}
