
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


# check sign in option
# is_valid_option, selected_option= check_sign_in_option()
# get user info
# validate user info
# start game


# main

# is_valid_option, selected_option= check_sign_in_option()
#    if is_valid_option==True:
#       user_name, pw , pw2 = get_user_info()
# is_user_info_ validated, messaage = validate_user_info(user_name, pw, pw2)
#   if is_user_info_validated = True:
#           start game
#   else: 

def main():
    """ Main executable logic """
    # welcome text

    # ask user to choose between sign-in and sign-up.
    # user can press 9 to navigate back to home menu

    # get user_name

    # validate user name

    # get password

    # validate password

    # write user name and password to google sheet

    # confirm user status as sign in
    # user can press 8 to sign out 

    # start game

    # end game

    # write high score if necessary

    # restart game for same user

    # ask user to sign 

    # if user name and password are validated, 
