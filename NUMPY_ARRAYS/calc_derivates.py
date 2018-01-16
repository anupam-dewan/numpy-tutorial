"""
Calculate Derivative
--------------------
Topics: NumPy array indexing and array math.
Use array slicing and math operations to calculate the
numerical derivative of ``sin`` from 0 to ``2*pi``.  There is no
need to use a 'for' loop for this.
Plot the resulting values and compare to ``cos``.
Bonus
~~~~~
Implement integration of the same function using Riemann sums or the
trapezoidal rule.
See :ref:`calc-derivative-solution`.
"""
from numpy import linspace, pi, sin, cos, cumsum
from matplotlib.pyplot import plot, show, subplot, legend, title

# calculate the sin() function on evenly spaced data.
def derivative():
    x = linspace(0,2*pi,101)
    y = sin(x)
    dx=x[1:]-x[:-1]
    dy=y[1:]-y[:-1]
    slope=dy/dx
    subplot(1,2,1)
    plot(x,y)
    title('sin')
    subplot(2,2,1)
    plot(slope)
    title('slope of sin')
    subplot(2,2,2)
    plot(x,cos(x))
    title('cos')
    show()