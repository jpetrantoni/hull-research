# main.py

import create_window
import simulation

import PyQt6
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QOpenGLContext
from PyQt6.QtGui import QPaintEngine

from create_model import Model
import create_window

# use a Widget that is opened on the screen


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("Black Hull")

        # set window size
        self.setGeometry(100, 100, 800, 600)

        # show all the widgets
        self.show()


# create pyqt5 app
App = PyQt6.QtWidgets.QApplication([])
# create the instance of our Window
window = Window()

# Create a QWidget
widget = QWidget()

# Set the widget's paint engine
# widget.setPaintEngine(QPaintEngine())

# Create a QPainter
painter = QPainter()

# Begin painting on the widget
painter.begin(widget)

# # Create a QPainter for drawing on the window
# painter = QPainter(window)

# start the app
App.exec()


# # Make the context current
# context.makeCurrent(window)

# Load the 3D boat model data
model = Model("model.stl")


# draw the fiberglass laying device


# Set the initial position of the boat
initial_position = model.center_mass

# Set the initial direction of the boat
initial_direction = model.face_normals[0]

# Define the initial path as a line segment from the initial position in the initial direction
initial_path = [initial_position, initial_position + initial_direction]

# Set the initial path and relevant parameters
path = initial_path
learning_rate = 0.1
temperature = 100.0
cooling_rate = 0.995


def calculate_num_rotations(path):
    # Calculate the number of rotations in the path
    num_rotations = 0
    for i in range(len(path) - 1):
        # Calculate the angle between the two vectors
        angle = simulation.angle_between_vectors(path[i], path[i + 1])

        # If the angle is greater than 90 degrees, then the boat has rotated
        if angle > 90:
            num_rotations += 1

    return num_rotations


# Use gradient descent to find the optimal path
path = simulation.gradient_descent(
    path, learning_rate, temperature, cooling_rate)


# Use simulated annealing to further improve the path
path = simulation.simulated_annealing(
    path, learning_rate, temperature, cooling_rate)

# draw the boat hull

# Draw the final path
painter.setPen(PyQt6.QtGui.QColor(255, 0, 0))
painter.drawLine(100, 100, 200, 200)

# Draw the fiberglass laying device
painter.setPen(PyQt6.QtGui.QColor(0, 255, 0))
painter.drawLine(200, 200, 300, 300)

# End painting
painter.end()


# # Print the final cost
print("Final cost:", simulation.cost(path))
