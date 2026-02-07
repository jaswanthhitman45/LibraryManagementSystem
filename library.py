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
def issue_book(book_id, student_name):
    print("Issuing Book")
    print("Book ID:", book_id)
    print("Issued To:", student_name)
    print("Book Issued Successfully")
