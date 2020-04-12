#Collecting varyables g = number to guess at x = first guess y= number of itterations
#Recolectando variables g = número para adivinar x = primera aproximación y = número de iteraciones
g = float(input("pick a number, any number. Big as you like:"))
x = float(input("now guess the root:"))
y = float(input("how many guesses do I get?:"))
#Function for root
def sqrt(g , x , y):
    ans = x
    y = y - 1
    while y > 0:
        ans = 0.5*(ans+(g/ans))
        y = y - 1
    return ans
print (sqrt(g, x, y))
