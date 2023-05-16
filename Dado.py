from OpenGL import GL
import glm
import math
from glApp import *

VERTEX_SHADER = """
#version 400

layout (location=0) in vec3 attr_position;
layout (location=1) in vec2 attr_textureCoord;

out vec2 textureCoord;
uniform mat4 mvp;

void main(void) 
{
    gl_Position = mvp*vec4(attr_position,1.0);
    textureCoord = attr_textureCoord;
}
"""

FRAGMENT_SHADER = """
#version 400

in vec2 textureCoord;
out vec4 color;
uniform sampler2D textureSlot;

void main(void) 
{
    color = texture(textureSlot,textureCoord);
}
"""

class Quadrado:

    def __init__(self):
        position = array('f',[
            -1.0, -1.0,  1.0,   #A
            1.0, -1.0,  1.0,    #B
            1.0,  1.0,  1.0,    #C
            -1.0,  1.0,  1.0,   #D

            -1.0, 1.0, 1.0,    #E
            1.0, 1.0, 1.0,   #F
            1.0,  1.0, -1.0,   #G
            -1.0,  1.0, -1.0 ,   #H

            1.0, -1.0,  -1.0,   #I
            -1.0, -1.0,  -1.0,    #J
            -1.0,  1.0,  -1.0,    #K
            1.0,  1.0,  -1.0,   #L

            -1.0, -1.0, -1.0,    #M
            1.0, -1.0, -1.0,   #N
            1.0,  -1.0, 1.0,   #O
            -1.0,  -1.0, 1.0 ,   #P

            -1.0, -1.0,  -1.0,   #Q
            -1.0, -1.0,  1.0,    #R
            -1.0,  1.0,  1.0,    #S
            -1.0,  1.0,  -1.0,   #T

            1.0, -1.0, 1.0,    #U
            1.0, -1.0, -1.0,   #V
            1.0,  1.0, -1.0,   #X
            1.0,  1.0, 1.0     #Y
        ])

        textcoord = array('f',[
            0.0, 1.0,
            1/3, 1.0,
            0.0, 1/2,
            1/3, 1/2,

            1/3, 1.0,
            2/3, 1.0,
            1/3, 1/2,
            2/3, 1/2,

            2/3, 1.0,
            1.0, 1.0,
            2/3, 1.0,
            1/3, 0.0, #

            1/3, 1/2, #
            1/3, 1/2,
            0.0, 0.0,
            2/3, 1.0, #

            1/3, 1/2,
            2/3, 1/2,
            2/3, 1/2, #
            0.0, 1/2, #

            2/3, 1.0, 
            0.0, 1/2, #
            2/3, 1.0, #
            1.0, 1.0
        ])

        index = array('H',[
            0, 1, 2,
            2, 3, 0,

            4, 5, 6,
            6, 7, 4,

            8, 9, 10,
            10, 11, 8,

            12, 13, 14,
            14, 15, 12,

            16, 17, 18,
            18, 19, 16,

            20, 21, 22,
            22, 23, 20

        ])

        self.VAO = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.VAO)

        GL.glEnableVertexAttribArray(0)
        GL.glEnableVertexAttribArray(1)

        VBO = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
        GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

        VBO = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, len(textcoord)*textcoord.itemsize, ctypes.c_void_p(textcoord.buffer_info()[0]), GL.GL_STATIC_DRAW)
        GL.glVertexAttribPointer(1,2,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

        VBO = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, VBO)
        GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, len(index)*index.itemsize, ctypes.c_void_p(index.buffer_info()[0]), GL.GL_STATIC_DRAW)
        self.indexLength = len(index)

    def draw(self):
        GL.glBindVertexArray(self.VAO)
        GL.glDrawElements(GL.GL_TRIANGLES,self.indexLength,GL.GL_UNSIGNED_SHORT,ctypes.c_void_p(0))

class QuadradoBranco(App):

    def setup(self):
        self.projection = glm.perspective(math.pi/4,800/600,0.1,100)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)
        self.shader = Shader(VERTEX_SHADER,FRAGMENT_SHADER)
        self.mesh = Quadrado()
        self.a =0

        GL.glActiveTexture(GL.GL_TEXTURE0)
        self.loadTexture("dado.png")

    def onResize(self, width, height):
        self.projection = glm.perspective(math.pi/4,width/height,0.1,100)

    def draw(self):
        GL.glClearColor(0.5, 0.5, 0.5, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        camera = glm.lookAt(glm.vec3(0,5,10),glm.vec3(0,0,0),glm.vec3(0,1,0))
        model = glm.rotate(self.a,glm.vec3(0,1,1))
        mvp = self.projection * camera * model
        self.shader.useProgram()
        self.shader.setMat4("mvp",mvp)
        self.mesh.draw()
        self.a += 0.005

if __name__ == "__main__":
    QuadradoBranco()
