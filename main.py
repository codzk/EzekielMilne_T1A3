from app_functions import create_profile, log_in

file_name = "user_data.csv"


# introduction/title (Calorie Calculator)
print("Welcome to our Calorie Calculator. Your guide for your daily calorie needs.")

# menu 1.create profile, 2. log in and 3.exit 
def generate_menu():
    print("1. Create Profile")
    print("2. Log In")
    print("3. Exit")
    option = input ("Please Select a Number from the Options Provided: ")
    return option


while True:
    option = generate_menu()

    if option == "1":
        create_profile(file_name)
    elif option == "2":
        log_in()
    elif option == "3":
        print("Thank you for using our Calorie Calculator!")
        break
    else:
        print("The option you have chosen is invalid. Please select a valid option.")





    





