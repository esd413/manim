import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtOpenGL import QGLWidget
import OpenGL.GL as gl
import OpenGL.GL.shaders as shaders

# 定义一个继承自 QGLWidget 的 OpenGL 窗口类
class GLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.width = 800
        self.height = 600

    def initializeGL(self):
        # 初始化 OpenGL 环境
        gl.glClearColor(0.0, 0.0, 0.0, 1.0)  # 设置背景颜色为黑色

        # 创建一个简单的着色器程序
        vertex_shader = """
        #version 330 core
        in vec3 aPos;
        void main() {
            gl_Position = vec4(aPos, 1.0);
        }
        """
        fragment_shader = """
        #version 330 core
        out vec4 FragColor;
        void main() {
            FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
        }
        """
        self.program = shaders.compileProgram(
            shaders.compileShader(vertex_shader, gl.GL_VERTEX_SHADER),
            shaders.compileShader(fragment_shader, gl.GL_FRAGMENT_SHADER)
        )

        # 创建一个简单的三角形
        self.vertices = [-0.5, -0.5, 0.0,
                         0.5, -0.5, 0.0,
                         0.0, 0.5, 0.0]
        self.vao = gl.glGenVertexArrays(1)
        self.vbo = gl.glGenBuffers(1)
        gl.glBindVertexArray(self.vao)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, len(self.vertices) * 4, (gl.GLfloat * len(self.vertices))(*self.vertices), gl.GL_STATIC_DRAW)
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 3 * 4, None)
        gl.glEnableVertexAttribArray(0)

    def paintGL(self):
        # 渲染 OpenGL 内容
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glUseProgram(self.program)
        gl.glBindVertexArray(self.vao)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)

    def resizeGL(self, w, h):
        # 处理窗口大小调整
        self.width = w
        self.height = h
        gl.glViewport(0, 0, w, h)

# 创建主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Modern OpenGL in PyQt5")
        self.resize(800, 600)
        self.gl_widget = GLWidget(self)
        self.setCentralWidget(self.gl_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())