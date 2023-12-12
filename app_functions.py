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
    


# user log in details
def log_in():
    print("Log In")
    username = input("Enter your username: ")
    password = input("Enter your password: ")