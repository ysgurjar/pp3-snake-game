"""
Provides authentication and connection to user data stored in google sheet.
Provides read and write capabilities to user data database.
Provides prompts for user input to terminal and validation of those inputs.
"""
# =====================================
# IMPORTS
# =====================================
import gspread
from google.oauth2.service_account import Credentials

# =====================================
# DATABASE CONNECTIONS
# =====================================
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Constants
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("pp3_user_data")
USER_DATA_SPREADSHEET = SHEET.worksheet("user_data")
# Global vars
data = USER_DATA_SPREADSHEET.get_all_values()
usernames_db = USER_DATA_SPREADSHEET.col_values(1)[1:]
pwds_db = USER_DATA_SPREADSHEET.col_values(2)[1:]
high_scores_db = USER_DATA_SPREADSHEET.col_values(3)[1:]

# =====================================
# FUNCTION DEFINITIONS
# =====================================


def append_gsheet_db(*args):
    """
    Appends userdata at the end of database
    """
    print("Adding user data to database..")
    USER_DATA_SPREADSHEET.append_row(args)
    print("data updated successfully")


def update_gsheet_high_score(u_name, score):
    """Updates user high score

    Args:
        u_name (str): user name
        score (int): score from the last game played
    """
    usernames_db = USER_DATA_SPREADSHEET.col_values(1)[1:]
    high_scores_db = USER_DATA_SPREADSHEET.col_values(3)[1:]
    row_number = usernames_db.index(u_name) + 2
    high_score = max(
        int(high_scores_db[usernames_db.index(u_name)]), int(score)
    )
    USER_DATA_SPREADSHEET.update_cell(row_number, 3, high_score)


def get_high_score(u_name):
    """Returns high score for given user name from database

    Args:
        u_name (str): user name

    Returns:
        int: high score for given user
    """
    high_scores_db = USER_DATA_SPREADSHEET.col_values(3)[1:]
    usernames_db = USER_DATA_SPREADSHEET.col_values(1)[1:]
    return int(high_scores_db[usernames_db.index(u_name)])


def choose_signing_option():
    """Prompts user to sign in or sign up

    Returns:
        bool, str: True , selected option - if inputs is validated
        func : recurring call to function itself - if inputs is not validated
    """
    print("\n")
    selected_option = input(
        "For sign-in press 1, for sign up press 2 and press enter:"
    )
    if selected_option in ["1", "2"]:
        return True, selected_option
    else:
        print("\nWrong input. Try again.\n")
        return choose_signing_option()


def get_user_name():
    """Prompt user to enter user name

    Returns:
        int: username
    """
    print("\n")
    user_name = input(
        "Enter username (alpha numeric, without space, minimum 4 char):"
    )
    return user_name


def validate_user_name(u_name):
    """Validate user name

    Args:
        u_name (int): user name

    Returns:
        bool, int: True, user name - if input is validated
        func: recurring call to itself - if input is not validated
    """
    # check if username is alphanumeric
    if u_name.isalnum() is True and len(u_name) > 3:
        return True, u_name
    else:
        print("\nInvalid input\n")
        return validate_user_name(get_user_name())


def get_pwd():
    """Pompts user to enter password

    Returns:
        str: password
    """
    print("\n")
    pwd = input(
        "Enter password (alpha numeric, without space, minimum 8 char):"
    )
    return pwd


def validate_pwd(pwd):
    """Validate password

    Args:
        pwd (str): password

    Returns:
        bool, str: True, password - if validated
        func: recurring call to itself - if input is not validated
    """
    # Check if it is alphanumeric
    if pwd.isalnum() is True and len(pwd) >= 8:
        return True, pwd
    else:
        print("\nInvalid input\n")
        return validate_pwd(get_pwd())


def additional_validation(u_name, pwd, selected_option):
    """Checks for all the possible combinations of \
        user name, password and selected sign in or \
        sing up option and provide relevent info \
        to user

    Args:
        u_name (str): user name
        pwd (str): password
        selected_option (str): selected sign in or sign up option

    Returns:
        _type_: _description_
    """
    # Check if  user name already exists db
    usernames_db = USER_DATA_SPREADSHEET.col_values(1)[1:]
    is_user_in_db = u_name in usernames_db

    # Get the pwd for that username from db and check if it matches
    try:
        pwds_db = USER_DATA_SPREADSHEET.col_values(2)[1:]
        pwd_from_db_for_given_user = pwds_db[usernames_db.index(u_name)]
    except ValueError:
        pwd_from_db_for_given_user = None
    is_pwd_match = pwd_from_db_for_given_user == pwd

    # Check for additional validation
    match (is_user_in_db, is_pwd_match, selected_option):
        # Allow - new user is signing up with unique user name
        case (False, False, "2"):
            print("\nSign up successful. \n")
            append_gsheet_db(u_name, pwd, 0)
            return True

        # Allow - existing user is singing in with matching pwd
        case (True, True, "1"):
            print("\nSing in successful. \n")
            return True

        # Prevent - new user singing up with
        # existing user name and existing pwd
        case (True, True, "2"):
            print(" \nUsername already exists. \n")
            print("Please select sign up if you are existing user. \n")
            print(
                "Please select a different user name if you are a new user. \n"
            )
            return False

        # Prevent - new user singing up with existing user name and new pwd
        case (True, False, "2"):
            print("\nUsername already exists. \n")
            print(
                "If you are a new user, retry by choosing another username. \n"
            )
            print(
                "If you are an existing user and forgot your pwd,"
                "please create a new login.\n"
            )
            return False

        # Prevent - sign in with wrong password
        case (True, False, "1"):
            print("\nUsername already exists. \n")
            print("Wrong password \n")
            print(
                "If you are an existing user and forgot your pwd"
                "please create a new login. \n"
            )
            return False

        # Prevent - sign in if username does not exist
        case _:
            print(
                "\nYou want to sign in but user name does not exist."
                "Please retry. \n"
            )
            print("If you are a new user, please select a sign up option. \n")
            return False
