# Program
height  = float(input("Enter your height in m: "))
weight  = float(input("Enter your weight in kg: "))

BMI = round(weight / height ** 2) 

if BMI < 18.5:
    print(f"Your Bmi is {BMI} and you are Underweight")
elif BMI > 18.5 and BMI < 25:
    print(f"Your Bmi is {BMI} and you are Normal weight")
elif BMI > 25 and BMI < 30:
    print(f"Your Bmi is {BMI} and you are Overweight")
elif BMI > 30 and BMI < 35:
    print(f"Your Bmi is {BMI} and you are Obese")
else:
    BMI > 35
    print(f"Your Bmi is {BMI} and you are clinically Obese")