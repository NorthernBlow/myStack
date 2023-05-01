import moderngl_window as mdglw


class App(mdglw.WindowConfig):
    window_size = 2560, 1080
    resource_dir = 'shaders'
    
    #конструктор родительского класса
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        #экран для отображения
        self.quad = mdglw.geometry.quad_fs()
        #загрузка шейдеров
        self.prog = self.load_program(vertex_shader='vertex_shader.glsl', fragment_shader='fragment_shader.glsl')

        self.set_uniform('resolution', self.window_size)


    def set_uniform(self, u_name, u_value):
        try:
            self.prog[u_name] = u_value

        except KeyError:
            print(f'unform: {u_name} - not used in shader')

    def render(self, time, frame_time):
        self.ctx.clear()
        self.set_uniform('time', time)
        self.quad.render(self.prog)


if __name__=='__main__':
    mdglw.run_window_config(App)

