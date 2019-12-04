import numpy as np  
import matplotlib.pyplot as plt  
import math




def riemann_sum(function, a, b, num_div, right=False):
    funcobj = compile(function, "Riemann input formula", "eval")
    rsum = 0
    div_size = (b - a) / num_div
    for i in range(0 + right, num_div + right):
        x = a + (i * div_size)
        func_val = eval(funcobj)
        rsum += func_val * div_size
    return rsum

def main():
    print("Riemann Sum calculator") 
    print("Enter a valid Python expression to be evaluated")
    print("Use x for the independent variable")
    function = input("Type in any eqatuion: ")
    a = float(input("a: "))
    b = float(input("b: "))
    num_div = int(input("n: "))
    right = input("Right or left? (L/R): ").upper() == "R"
    rsum = riemann_sum(function, a, b, num_div, right)
    print(rsum)


if __name__ == "__main__":

    main()
   



main()
