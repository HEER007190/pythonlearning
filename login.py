data=[]
def sign_up(email,password):
    login_data={'email':email,'password':password}
    if email.endswith('@gmail.com') and len(password)<=8:
     data.append(login_data)
     print(f"sign up email {email} with password {password} successfully")
    else:
       print("Invalid email or password")
def login(login_email,login_password):
    for login_data in data:
        if login_data['email'] == login_email and login_data['password'] == login_password:
            print("Login successfully")
        else:
            print("Login failed")
user_choice = input("Enter your choice to sign up or login: ").title().strip()
if user_choice == "Sign Up":
    sign_up(input("Enter your email: "), input("Enter your password: "))
elif user_choice == "Login":
    login(input("Enter your email: "), input("Enter your password: "))
else:
    print("Invalid choice")