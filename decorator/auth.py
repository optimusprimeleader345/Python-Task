def login_required(func):
    def wrapper():
        password = input("Enter the password: ")
        if password == "secret":
            return func()
        else:
            print("Incorrect password. Access denied.")
    return wrapper
@login_required
def dashboard():
    print("Welcome to the dashboard!")
print(dashboard("admin"))
print(dashboard("guest"))