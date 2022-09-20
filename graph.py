from numpy import linspace, meshgrid
from main import *
import matplotlib.pyplot as plt



x1 = linspace(-6,6,2000)
x2 = linspace(-6,6,2000)

x1_,x2_ = meshgrid(x1,x2)

u,v = phase_plane(x1_,x2_)
vel = sqrt(u**2+v**2)

# fig = plt.figure()
# ax = plt.axes()
plt.figure()
# plt.axis("equal")
plt.streamplot(x1_,x2_,u,v, color='k', linewidth=0.8,density=2, minlength=0.01, arrowsize=0.5,arrowstyle="->")
# plt.quiver(x1_,x2_,u,v)
plt.show()

# matplotlib.pyplot.streamplot(x, y, u, v, density=1, linewidth=None, color=None, cmap=None, norm=None, arrowsize=1, arrowstyle='-|>', minlength=0.1, transform=None, zorder=None, start_points=None, maxlength=4.0, integration_direction='both', broken_streamlines=True, *, data=None)



# plt.rcParams['text.usetex'] = True

# w0 = zeros([1000])
# w = zeros([1000])
# theta = linspace(-pi,pi,1000)

# for i in range(1000):
#     w[i] = w_nonliner(theta[i])
#     w0[i] = sqrt(g/l)

# fig = plt.figure()
# ax = plt.axes()
# ax.grid()

# ax.plot(theta, w0, label = "frequency of approximate function")
# ax.plot(theta, w, label = "frequency of exact equation")
# ax.set(xlabel = "$\theta_{0}$")
# plt.show()



# fig, ax = plt.subplots()
# interface tracking profiles
# N = 500
# delta = 0.6
# X = np.linspace(-1, 1, N)
# ax.plot(X, (1 - np.tanh(4 * X / delta)) / 2,    # phase field tanh profiles
        # X, (1.4 + np.tanh(4 * X / delta)) / 4, "C2",  # composition profile
        # X, X < 0, "k--")                        # sharp interface

# legend
# ax.legend(("phase field", "level set", "sharp interface"),
          # shadow=True, loc=(0.01, 0.48), handlelength=1.5, fontsize=16)

# the arrow
# ax.annotate("", xy=(-delta / 2., 0.1), xytext=(delta / 2., 0.1),
            # arrowprops=dict(arrowstyle="<->", connectionstyle="arc3"))
# ax.text(0, 0.1, r"$\delta$",
        # color="black", fontsize=24,
        # horizontalalignment="center", verticalalignment="center",
        # bbox=dict(boxstyle="round", fc="white", ec="black", pad=0.2))

# Use tex in labels
# ax.set_xticks([-1, 0, 1])
# ax.set_xticklabels(["$-1$", r"$\pm 0$", "$+1$"], color="k", size=20)

# Left Y-axis labels, combine math mode and text mode
# ax.set_ylabel(r"\bf{phase field} $\phi$", color="C0", fontsize=20)
# ax.set_yticks([0, 0.5, 1])
# ax.set_yticklabels([r"\bf{0}", r"\bf{.5}", r"\bf{1}"], color="k", size=20)

# Right Y-axis labels
# ax.text(1.02, 0.5, r"\bf{level set} $\phi$",
        # color="C2", fontsize=20, rotation=90,
        # horizontalalignment="left", verticalalignment="center",
        # clip_on=False, transform=ax.transAxes)

# Use multiline environment inside a `text`.
# level set equations
# eq1 = (r"\begin{eqnarray*}"
       # r"|\nabla\phi| &=& 1,\\"
       # r"\frac{\partial \phi}{\partial t} + U|\nabla \phi| &=& 0 "
       # r"\end{eqnarray*}")
# ax.text(1, 0.9, eq1, color="C2", fontsize=18,
        # horizontalalignment="right", verticalalignment="top")

# phase field equations
# eq2 = (r"\begin{eqnarray*}"
       # r"\mathcal{F} &=& \int f\left( \phi, c \right) dV, \\ "
       # r"\frac{ \partial \phi } { \partial t } &=& -M_{ \phi } "
       # r"\frac{ \delta \mathcal{F} } { \delta \phi }"
       # r"\end{eqnarray*}")
# ax.text(0.18, 0.18, eq2, color="C0", fontsize=16)

# ax.text(-1, .30, r"gamma: $\gamma$", color="r", fontsize=20)
# ax.text(-1, .18, r"Omega: $\Omega$", color="b", fontsize=20)

# plt.show()



