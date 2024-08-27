weight = float(input("enter your weight in kg"))
height = float(input("enter your height in cm"))
BMI = weight / (height/100)**2
print("your bmi is", BMI)
if BMI <= 18.4:
    print("you are underweight")
elif BMI <= 24.9:
 print("you are healthy")
elif BMI <= 29.9:
 print("you are overweight")
elif BMI <= 39.9:
 print("you are severly overweight")
elif BMI <= 49.9:
 print("you are obese")
