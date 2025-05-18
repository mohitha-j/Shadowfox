from math import pow
Height=float(input("Enter height in meters"))
Weight=float(input("Enter weight in kilograms"))
BMI=Weight/pow(Height,2)
if BMI==30 or BMI>30:
    print("Obesity")
if BMI>25 and BMI<29:
    print("Overweight")
if BMI>18.5 and BMI<25:
    print("Normal")
if BMI<18.5:
    print("Underweight")
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
city=input("enter the city in name")   
if city in Australia:
    print(f"{city} is in Australia")
if city in UAE:
    print(f"{city} is in UAE")
if city in India:
    print(f"{city} is in India")
city1=input("enter city1")
city2=input("Enter city2")
if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
if city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")
if city1 in India and city2 in India:
    print("Both cities are in India")
else:
    print("They dont belong to same country")
