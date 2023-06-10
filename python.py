W = float(input("Enter the weight in kg:"))
H = float(input("Enter the height in m:"))
BMI = W/(H*H)
print("Your BMI is:",BMI)
if BMI <=18.5:
  print("Healthy habits calling!You are underweight")
elif BMI <=24.9:
  print("Well done, keep it up!You are healthy")
elif BMI <=29.9:
  print("Healthy habits calling!!You are overweight")
else:
  print("Extra healthy habits on the call!!You are obese")
