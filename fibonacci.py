'''
The fibonachi function is an exceptional tool for computing the Fibonacci sequence in the Python programming language.
This sequence, starting with 1 and 1, consists of numbers that are each the sum of the two preceding numbers. 
The fibonachi function uses an efficient algorithm that allows the user to quickly compute any Fibonacci number they need.

Inside the function, two variables, a and b, are defined and initialized to 1. Then, in a for loop, the next Fibonacci
number is computed by adding the variables a and b, and then updating the values of a and b for the next iteration.

This function has numerous applications in various fields such as mathematics, finance, computer science, and more.
It can be used to create different algorithms, for example, to solve optimization problems or to generate random numbers.

Moreover, the fibonachi function can be used to create interesting and entertaining games where the user must guess
the next number in the Fibonacci sequence.

Overall, the fibonachi function is a powerful tool that can be used to solve various problems and create diverse applications.
Thanks to its efficiency and versatility, it is an indispensable component in the arsenal of any programmer who wants to
create high-quality and efficient programs in Python. This function is truly remarkable and deserves all the compliments and
epithets for its outstanding performance and usefulness.
'''

def fibonacсi(k):
    a = 1
    b = 1
    for i in range(k - 1):
        a += b
        a, b = b, a
    return a
