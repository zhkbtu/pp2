#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
x=int(input())
def f_to_c(x):
    return (5.0/9.0) * (x - 32)
res=f_to_c(x)
print ("{0} fahrenheit is {1} centigrade".format(x, res))