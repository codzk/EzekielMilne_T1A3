from app_functions import create_profile, log_in, calculate_calories, calculate_bmi

file_name = "user_data.csv"
logged_in_user = None
logged_in = False

# introduction/title (Calorie and BMI Calculator)
print("\nWelcome to our Calorie and BMI Calculator. Your guide for your daily calorie needs.")

# menu 1. create profile, 2. log in, and 3. exit
while True:
    print("\n1. Create Profile")
    print("2. Log In")
    print("3. Exit")
    option = input("\nPlease enter the number corresponding to your choice: ")

    if option == "1":
        create_profile(file_name)
    elif option == "2":
        logged_in_user = log_in(file_name)
        if logged_in_user:
            logged_in = True
            # options after successful login
            while logged_in:  # Use the logged_in flag to control the flow
                print("\nWelcome! How can I help?")
                print("1. Calculate Calories")
                print("2. Calculate BMI")
                print("3. Log")
                print("4. Exit")
                sub_option = input("\nEnter your choice: ")
                if sub_option == "1":
                    if not calculate_calories():
                        logged_in = False  # Set the flag to False to exit the inner loop
                elif sub_option == "2":
                    if not calculate_bmi():
                        logged_in = False
                elif sub_option == "3":
                    print("For log/history")
                elif sub_option == "4":
                    print("Exiting the Calorie Calculator.")
                    logged_in = False  # Set the flag to False to exit both loops
                else:
                    print("Invalid option. Please choose a valid option.")
    elif option == "3":
        print("\nThank you for using our Calorie and BMI Calculator!")
        break  # Exit the main loop
    else:
        print("Invalid option. Please choose a valid option.")
