from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons

apr = int(input("Введите точность аппроксимации: ")) + 4

fig = plt.figure('Лабораторная работа №3 - Муртазин Р.Ю.', figsize=(8., 6.))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.2)
plt.title('Пятигранная прямая правильная пирамида аппроксимированная цилиндром', y=0.95)
v = np.array([[0, 0, 1], [0, 0, 0]])

for i in range(1, apr + 1):
    x = np.cos(2 * np.pi * i / apr)
    y = np.sin(2 * np.pi * i / apr)
    z = sum([0.5 ** i for i in range(1, apr - 4)])
    v = np.vstack([v, [x, y, 0], [x, y, z]])

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
verts = [[v[0], v[3], v[2 * apr + 1]], [v[1], v[2], v[2 * apr]], [v[3], v[2 * apr], v[2 * apr + 1]],
         [v[2], v[3], v[2 * apr]]]
for i in range(2, 2 * apr - 1, 2):
    verts = verts + [[v[0], v[i + 1], v[i + 3]], [v[1], v[i], v[i + 2]], [v[i], v[i + 1], v[i + 3]],
                     [v[i], v[i + 2], v[i + 3]]]
ax.add_collection3d(Poly3DCollection(verts, facecolor='green', linewidths=1, edgecolors='seagreen', alpha=0.25))


def iButton(event):
    ax.view_init(28, -136)
    plt.draw()


axes_ibutton_add = plt.axes([0.55, 0.05, 0.4, 0.075])
ibutton_add = Button(axes_ibutton_add, 'Изометрическая')
ibutton_add.on_clicked(iButton)


def oButton(event):
    ax.view_init(-2, 0)
    plt.draw()


axes_obutton_add = plt.axes([0.06, 0.05, 0.4, 0.075])
obutton_add = Button(axes_obutton_add, 'Ортографическая')
obutton_add.on_clicked(oButton)
lines_visibility = plt.axes([0.02, 0.85, 0.37, 0.11], facecolor='lightcyan')
radio = RadioButtons(lines_visibility, ('Каркасная отрисовка', 'Убрать видимые линии'))


def lines(a):
    condition = {'Каркасная отрисовка': 0.20, 'Убрать видимые линии': 1}
    alpha = condition[a]
    ax.add_collection3d(Poly3DCollection(verts, facecolors='lightgreen', linewidths=1, edgecolors='seagreen',
                                         alpha=alpha))
    plt.draw()


radio.on_clicked(lines)
plt.show()
