"""EThe objective of this exercise is to calculate someone's body mass index (BMI) (in this case I set an example by giving my name" hans "). The inputs are the person's height in centimeters and weight in kilograms The output is its weight divided by its height in square meters."""

print("hans BMI")

# Enter my current weight 98 Kg
weight = float(input("Enter hans weight:")) 

# Height of 1.80 cm is entered
height = float(input("Enter heigh:"))

BMI = weight/(height * height)

# Should result 30.24691358024691
print ("hans, your super BMI is", BMI)
#
