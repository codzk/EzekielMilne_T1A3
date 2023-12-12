from app_functions import create_profile, log_in

file_name = "user_data.csv"
logged_in = False


# introduction/title (Calorie Calculator)
print("Welcome to our Calorie Calculator. Your guide for your daily calorie needs.")

# menu 1.create profile, 2. log in and 3.exit 
def generate_menu():
    print("1. Create Profile")
    print("2. Log In")
    print("3. Exit")
    option = input ("Please Select a Number from the Options Provided: ")
    return option


while not logged_in: # loop until logged_in is True
    option = generate_menu()

    if option == "1":
        create_profile(file_name)
    elif option == "2":
        logged_in_user = log_in(file_name)
        if logged_in_user:
            logged_in = True # set to True if login is successful 
            # options after successful login
            print("Welcome!How can I help?")
            print("1. Calculate Calories")
            print("2. Log")
            print("3. Exit")
    elif option == "3":
        print("Thank you for using our Calorie Calculator!")
        break
    elif logged_in:
        if option == "1":
            calculate_calories()
        elif option == "2":
            print("for log/history")
        elif option == "3":
            print("Exiting the Calorie Calculator.")
            break
    else:
        print("The option you have chosen is invalid. Please select a valid option.")





    





