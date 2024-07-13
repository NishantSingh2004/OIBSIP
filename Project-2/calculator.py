from bmi_lib import bmi_calc, bmi_catogorize, xyz_input

def nishant():
    print("Welcome to the  BMI Calculator!")

    weight, height = xyz_input()

    bmi = bmi_calc(weight, height)
    category = bmi_catogorize(bmi)

    print("\nBMI Result:")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    nishant()