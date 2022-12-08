# Import the OpenGL.GL and OpenGL.GLU modules
import OpenGL.GL as GL
import OpenGL.GLU as GLU

from PyQt6 import QtWidgets, QtGui, QtCore

import trimesh


class Model:
    def __init__(self, path):
        self.model = trimesh.load(path)
        self.vertices = self.model.vertices
        self.faces = self.model.faces

        self.vertex_buffer = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vertex_buffer)
        GL.glBufferData(
            GL.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL.GL_STATIC_DRAW)

        self.center_mass = self.model.center_mass
        self.face_normals = self.model.face_normals

    def draw(self):
        # Bind the vertex buffer object and enable vertex attributes
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vertex_buffer)
        GL.glEnableVertexAttribArray(0)
        GL.glVertexAttribPointer(
            0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, None)

        # Bind the index buffer object and draw the model using the indices
        GL.glBindBuffer(
            GL.GL_ELEMENT_ARRAY_BUFFER, self.index_buffer)
        GL.glDrawElements(GL.GL_TRIANGLES, len(
            self.faces) * 3, GL.GL_UNSIGNED_INT, None)

        # Unbind the vertex and index buffer objects
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, 0)

        # Disable vertex attributes
        GL.glDisableVertexAttribArray(0)
