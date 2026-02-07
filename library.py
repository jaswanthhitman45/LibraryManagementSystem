print("Library Management System Initialized")

def register_student(name, roll):
    print("Registering Student")
    print("Name:", name)
    print("Roll No:", roll)
    print("Registration Successful")

def login(username, password):
    print("Checking credentials")
    if username == "admin" and password == "admin123":
        print("Login Successful")
    else:
        print("Invalid Login")
