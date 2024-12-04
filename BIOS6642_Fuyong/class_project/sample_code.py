# Please modify the user_login function such that the system
# (i.e., your program) automatically stops running if the user
# provides 3 successive incorrect inputs for user name and password.
def user_login():
    login = True
    while login:
        user_name = input('User name: ')
        password = input('Password: ')
        if user_name == 'Admin' and password == 'python':
            login = False
        else:
            print('The user name and password are not matched. Please try again.')


# Please delete the pass statement and implement the database_initialization function.
# Add proper formal parameters for the function, if necessary.
def database_initialization():
    pass


# Please delete the pass statement and implement the user_selection function.
# Add proper formal parameters for the function, if necessary.
def user_selection():
    pass


# main function
def main(database_name):
    # Bank account management system database initialization
    # Please implement the database_initialization function
    user_login()

    # Initialization of the bank account management system database
    # Please implement the database_initialization function (and add proper formal parameters if necessary)
    database_initialization()

    # Bank account management via user selection
    # Please implement the user_selection function (and add proper formal parameters if necessary)
    user_selection()


# Run the main function
database_filename = 'account_data.csv'
main(database_filename)
