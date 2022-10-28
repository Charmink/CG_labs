import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

fig = plt.figure('Лабораторная работа №1 - Муртазин Р.Ю.', figsize=(8., 6.))
ax = fig.add_subplot(111, projection='polar')
plt.subplots_adjust(bottom=0.2)
plt.title('ρ = a * cos(3 * phi)')

phi = np.arange(0, 2 * np.pi, 0.0001)
r = 5 * np.cos(3 * phi)
initial_text = "5"
l, = plt.plot(phi, r, lw=2)

l.set_ydata(r)
ax.set_ylim(np.min(r), np.max(r))
plt.draw()


def submit(text):
    r_new = float(text) * np.cos(3 * phi)
    l.set_ydata(r_new)
    ax.set_ylim(np.min(r_new), np.max(r_new))
    plt.draw()


ax_box = plt.axes([0.4, 0.05, 0.5, 0.075])
text_box = TextBox(ax_box, 'Введите значение параметра а:', initial=initial_text)
text_box.on_submit(submit)

plt.show()
