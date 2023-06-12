
def check_sign_in_option():
    selected_option= input("For sign-in press 1, for sign up press 2 and press enter:")
    if selected_option in ["1","2"]:
        #check username
        return True, selected_option
    else:
        print("Wrong input. Try again")
        check_sign_in_option()

def check_username(option,user_name):
    # if selected option is sign-in and username exists
        #check password
    # if selected option is sign-up and username exists
        # user name already exists, select another username
    pass
    
def check_user_name_validity():
    pass

def check_pw_validity():
    pass

if check_sign_in_option(option):
    user_name=input("Enter username :")
    pwd=input("Password :")

    if option=="2":
        pwd_2=input("Re enter password :")
    
    is_valid_username= check_user_name_validity()
    is_valid_pwd = check_pw_validity()
    if is_valid_username and is_valid_pwd:
        #stat game
        pass


def get_user_info():
    """depending on the sign in option selected, get user information"""
    # check if valid option is selected
    is_valid_option, selected_option= check_sign_in_option()
    if is_valid_option==True:
        """Ask for username and pw if valid option is selected."""
        user_name=input("Enter username :")
        pwd=input("Password :")
        # if user has selected for sign up ask to re enter pw
        if selected_option=="2":
            pwd_2=input("Re enter password :")
