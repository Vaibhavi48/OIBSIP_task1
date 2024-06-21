def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def check_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be greater than 0")
            return value
        except ValueError as e:
            print("Invalid input. Please enter a positive number.")

height = get_user_input("Enter your height in meters: ")
weight = get_user_input("Enter your weight in kilograms: ")

bmi = calculate_bmi(weight, height)
status = check_bmi_status(bmi)

print("Your bmi:",bmi,"kg/m^2","\n",'Your status:',status)
