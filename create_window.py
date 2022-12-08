from PyQt6 import QtGui


class Window(QtGui.QWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setTitle("Black Hull")
        self.resize(800, 600)

    def create_context(self):
        context = QtGui.QOpenGLContext(self)
        context.setFormat(self.requestedFormat())
        context.create()

        return context

    def render(self, painter):

        # Clear the window with the current background color
        painter.beginNativePainting()
        context = painter.paintEngine().openglContext()
        context.functions().glClear(context.functions().GL_COLOR_BUFFER_BIT)
        painter.endNativePainting()

        # Draw the 3D model of the boat hull
        painter.setPen(QtGui.QColor(255, 255, 255))
        painter.drawLine(0, 0, 100, 100)

        # Draw the linear path on the surface of the hull
        painter.setPen(QtGui.QColor(255, 0, 0))
        painter.drawLine(100, 100, 200, 200)

        # Draw the fiberglass laying device
        painter.setPen(QtGui.QColor(0, 255, 0))
        painter.drawLine(200, 200, 300, 300)

    def render_now(self):
        if not self.isExposed():
            return

        self
