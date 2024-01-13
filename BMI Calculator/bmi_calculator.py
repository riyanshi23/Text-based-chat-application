# Function to calculate BMI
def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m) * height (m))
    bmi = weight / (height ** 2)
    return bmi

# Function to classify BMI into categories
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Classify BMI into categories
    category = classify_bmi(bmi)

    # Display BMI result and category
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()