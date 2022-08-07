# flow-animation-with-scipy-odeint

This script has been created just for fun. It creates an animation of a flow of particles (or points) whose trajectory has been calculated using the odeint function from the scipy.integrate sub-package.

The following animation can be obtained using the default acceleration field definition from the [script](https://github.com/artmenlope/flow-animation-with-scipy-odeint/blob/master/odeint-2d-flow.py).

<p align="center">
<img src="https://github.com/artmenlope/flow-animation-with-scipy-odeint/blob/master/odeint-flow-animation-compressed.gif" width="40%">
</p>

The acceleration field that acts on each particle and generates the animation above is given by

$$
\vec{a} = (a_x, a_y)  \quad \longrightarrow \quad \begin{array}{c} a_x = -\cos(y)\sin(x)\\
a_y=-\sin(y)\cos(x) \end{array}
$$

For the making of the [script](https://github.com/artmenlope/flow-animation-with-scipy-odeint/blob/master/odeint-2d-flow.py) the following references have been consulted:
1. [Docs.scipy.org. 2020. _Scipy.Integrate.Odeint — Scipy V1.5.2 Reference Guide_. [online]](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html)

2. [Correoso, K., 2014. _Microentrada: Rendimiento De Scatterplots En Matplotlib – Pybonacci_. [online] Pybonacci.org.](https://pybonacci.org/2014/09/09/microentrada-rendimiento-de-scatterplots-en-matplotlib/)
