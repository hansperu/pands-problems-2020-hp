"""Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared."""

print("hans BMI")

weight = float(input("Enter hans weight:"))
height = float(input("Enter heigh:"))

BMI = weight/(height * height)

print ("hans, your super BMI is", BMI)

