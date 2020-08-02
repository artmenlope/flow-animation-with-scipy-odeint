# flow-animation-with-scipy-odeint

This script has been created just for fun. It creates an animation of a flow of particles (or points) whose trajectory has been calculated using the odeint function from the scipy.integrate sub-package.

The following animation can be obtained using the default acceleration field definition from the [script](https://github.com/artmenlope/flow-animation-with-scipy-odeint/blob/master/odeint-2d-flow.py).

<p align="center">
<img src="https://github.com/artmenlope/flow-animation-with-scipy-odeint/blob/master/odeint-flow-animation-compressed.gif" width="40%">
</p>

The acceleration field that acts on each particle and generates the animation above is given by
<!-- Note: For Latex formulas in Github's Markdown see https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b and the script at https://jsfiddle.net/8ndx694g/ -->
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=%5Cvec%7Ba%7D%3D(a_x%2Ca_y)%20%5C%3B%2C%20%5C%3B%5C%3B%0A%5Cbegin%7Bcases%7D%0A%0Aa_x%20%20%26%20%5C!%5C!%5C!%5C!%20%3D%20-%20%5Ccos(y)%20%5C%3B%20%5Csin(x)%20%5C%5C%5B1.8ex%5D%0Aa_y%20%20%26%20%5C!%5C!%5C!%5C!%20%3D%20-%20%5Csin(y)%20%5C%3B%20%5Ccos(x)%0A%5Cend%7Bcases%7D">
</p>

For the making of the [script](https://github.com/artmenlope/flow-animation-with-scipy-odeint/blob/master/odeint-2d-flow.py) the following references have been consulted:
1. [Docs.scipy.org. 2020. _Scipy.Integrate.Odeint — Scipy V1.5.2 Reference Guide_. [online]](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html)

2. [Correoso, K., 2014. _Microentrada: Rendimiento De Scatterplots En Matplotlib – Pybonacci_. [online] Pybonacci.org.](https://pybonacci.org/2014/09/09/microentrada-rendimiento-de-scatterplots-en-matplotlib/)
