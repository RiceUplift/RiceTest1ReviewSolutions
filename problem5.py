a = float(input("Enter the value of a: ")) #We want all 3 user values to be floats so that we can deal with decimals.
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

x_1 = (-b + pow(b**2 - 4*a*c, .5))/(2*a) #+ solution to the quadratic formula.
x_2 = (-b - pow(b**2 - 4*a*c, .5))/(2*a) #- solution to the quadratic formula.

print("The solutions are: " + str(x_1) + " and " + str(x_2)) #Outputs both solutions


'''
If you put in values a=1, b=0, c=4, one of the solutions you get is (1.2246467991473532e-16+2j). This is how Python
writes a complex number. Recal that a complex number can be written in the form z = x + iy, where x = Re(z) and 
y = Im(z). In this case, Python uses j as the complex number instead of i. This is reasonably common among engineers.
The e-16 part means the same thing it does on graphing and scientific calculators, x10^(-16). So the first number is 
really 1.2246467991473532e-16 = 1.2246467991473532x10^-16 = .00000000000000012246467991473532. This is a tiny number.
As we know from algebra, the solution should be 2i and -2i (or 2j and -2j as the engineers would say). Python, and 
other languages, aren't always the best at rounding. This small number is the result of not being infinitely accurate.
When you get a number this small in Python, it likely means the value is 0. (Unless of course you are working with 
numbers that small.)
'''