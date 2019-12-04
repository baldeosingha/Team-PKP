import numpy as np  
import matplotlib.pyplot as plt  
# This program calculate the Riemann sum which is the area under a curve
#
# The function being used in this case is y = x^2
#
# This program integrates the function from x1 to x2
# x2 must be greater than x1, otherwise the program will print an error message.
#
equation = input("Type in any equation: ")

def Riemann(): 
    x1 = float(input("x_1="))
    x2 = float (input("x_2="))
    if x1 > x2:
        print("The calculated area will be negative")
    # Compute delta_x for the integration interval
    #
    delta_x = ((x2-x1)/1000)
    j = abs ((x2-x1)/delta_x)
    i = int (j)
    print("i =", i)
    # initialize
    n=0
    A= 0.0
    x = x1
    # Begin Numerical Integration
    while n < i:
        delta_A = x * delta_x
        x = x + delta_x
        A = A + delta_A
        n = n+1

    print("Area Under the Curve =", A)


def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()


Riemann()
graph(equation, range(-100, 100))