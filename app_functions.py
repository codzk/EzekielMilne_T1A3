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
        print("Invalid Username or Password. Please try again.")
        return None