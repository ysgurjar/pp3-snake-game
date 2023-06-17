import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS=Credentials.from_service_account_file('creds.json')
SCOPED_CREDS=CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT=gspread.authorize(SCOPED_CREDS)
SHEET=GSPREAD_CLIENT.open('pp3_user_data')
user_data_spreadsheet=SHEET.worksheet('user_data')
data=user_data_spreadsheet.get_all_values()
usernames_db=user_data_spreadsheet.col_values(1)[1:]
pwds_db=user_data_spreadsheet.col_values(2)[1:]
high_scores_db=user_data_spreadsheet.col_values(3)[1:]

print(data)
print(usernames_db)
prompt=input("enter username:")


def choose_signing_option():
    selected_option = input(
        "For sign-in press 1, for sign up press 2 and press enter:")
    if selected_option in ["1", "2"]:
        # check username
        return True, selected_option
    else:
        print("Wrong input. Try again.")
        return choose_signing_option()


def get_user_name():
    user_name = input(
        "Enter username (alpha numeric, without space, minimum 4 char):")
    return user_name


def validate_user_name(u_name):
    # check if username is alphanumeric
    if u_name.isalnum() == True and len(u_name)>3:
        return True, u_name
    else:
        print("Invalid input")
        return validate_user_name(get_user_name())


def get_pwd():
    pwd = input("Enter password (alpha numeric, without space, minimum 8 char):")
    return pwd


def validate_pwd(pwd):
    # check if it is alphanumeric
    if pwd.isalnum() == True and len(pwd)>=8:
        return True, pwd
    else:
        print("Invalid input")
        return validate_pwd(get_pwd())


def additional_validation(u_name, pwd, selected_option):

    # check if  user name already exists db
    
    is_user_in_db = u_name in usernames_db

    # get the pwd for that username from db and check if it matches
    pwd_from_db_for_given_user = pwds_db[usernames_db.index(u_name)]
    is_pwd_match = pwd_from_db_for_given_user == pwd

    # check for additional validation
    match (is_user_in_db, is_pwd_match, selected_option):

        # allow - new user is signing up with unique user name
        case (False, None, "2"):
            print("Sign up successful. \n")
            return True

        # allow - existing user is singing in with matching pwd
        case (True, True, "1"):
            print("Sing in successful. \n")
            return True

        # prevent - new user singing up with existing user name and existing pwd
        case (True, True, "2"):
            print("Username already exist.")
            print("Please select sign up if you are existing user.")
            return False

        # prevent - new user singing up with existing user name and new pwd
        case (True, False, "2"):
            print("Username already exists.")
            print("If you are a new user, retry by choosing another username")
            print(
                "If you are an existing user and forgot your pwd, please create a new login")
            return False
        
        # prevent sign in with wrong password
        case (True, False, "1"):
            print("Username already exists.")
            print("Wrong password")
            print(
                "If you are an existing user and forgot your pwd, please create a new login")
            return False

        # prevent - sign in if username does not exist
        case _:
            print("You want to sign in but user name does not exist. Please retry.")
            print(
                "If you are an existing user and forgot your pwd, please create a new login")
            return False