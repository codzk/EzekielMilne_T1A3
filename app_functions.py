import csv

# user create profile
def create_profile(file_name):
    print("Create Profile")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([username, password])

    print(f"Profile for {username} created successfully")
    
def load_user_data(file_name):
    user_data = []
    with open(file_name, "r") as r:
        reader = csv.reader(r)
        for row in reader:
            user_data.append({"username": row[0], "password": row[1]})
    return user_data

def login_valid(username, password, user_data):
    for user in user_data:
        if user["username"] == username and user["password"] == password:
            return True
    return False


# user log in details
def log_in(file_name):
    print("Log In")

    user_data = load_user_data(file_name)

    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if login_valid(username, password, user_data):
        print("Login Successful.")
        return{"username": username, "password": password}
    else:
        print("\nInvalid Username or Password. Please try again.")
        return None
    
def calculate_calories():
    print("Calculate Calories")

    # user input for age, height, weight and activity level
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))

    # choose an activity level
    print("Select your activity level: ")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly active (light exercise/sports 1-3 days/week)")
    print("3. Moderately active (moderate exercise/sports 3-5 days/week)")
    print("4. Very active (hard exercise/sports 6-7 days a week)")
    activity_level = int(input("Enter the number corresponding to your activity level: "))

    # Harris-Benedict equation for estimating Basal Metabolic Rate (BMR)
    # BMR calculation depends on gender (1.2 for females, 1.55 for males)

    gender = input("Enter your gender (M/F) in upper case: ").upper()

    if gender == "M":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "F":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        print("Invalid gender. Please enter 'M' or 'F'.")
        return
    
    # Adjust BMR based on activity level
    activity_factors = [1.2, 1.375, 1.55, 1.725]
    activity_multiplier = activity_factors[activity_level - 1]
    total_calories = round(bmr * activity_multiplier)

    print(f"\nYour estimated daily calorie needs: {total_calories} calories.")
    return input("\nDo you want to go back to the sub menu? (yes/no): ").lower() == 'yes'
    # goes back to sub_option

def calculate_bmi():
    print("Calculate BMI")

    # user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height_cm = float(input("Enter your height in centimeters: "))

    #convert height to metres
    height_m = height_cm / 100

    # BMI calculation
    bmi = weight / (height_m ** 2)

    print (f"\nYour BMI is: {bmi:.2f}")

    # BMI categories
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    print(f"Your BMI category is: {category}")
    return input("\nDo you want to go back to the sub menu? (yes/no): ").lower() == 'yes'
    #goes back to sub_option


