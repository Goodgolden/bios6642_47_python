################################################################################
## the main functions                                                         ##
################################################################################
### Login function for maximum 3 times of failures on user name and password
def Login():
    """
    the default username is: Admin,
    the default password is: python.
    """
    login = True # initiation for login
    times = 0 # initation for times
    while login and times < 3: #
        user_name = input("User name: ")
        password = input("Password: " )
        if user_name == "Admin" and password == "python":
            login = False # success and end the while loop
            print("You've successfully logged in.")
            Initialization(file)
            UserSelection()
        else:
            times = times + 1 # add one more time
            print("Please try again. You have tried", times, "times.")
    if times >= 3: # after 3 times of failures
        print("Please restart the system.") # automatically stops running
        return
################################################################################
### Initialization function is to read all the file data
def Initialization(file):
    with open(file, "r") as data: # read the file and name it as data
        information = data.readlines() # read data as a list
        header = information[0].strip().split(",")  # split and store the header as a list
        accounts = [] # another list for account
        for row in information[1:len(information)]: # each row is an individual
            values = row.strip().split(",") # split each row
            values = [i.strip() for i in values] # iteration
            accounts.append(values)  # add each attributes into the list
    return header, accounts
################################################################################
### the user can select a number responding to specific function
### must be in the list, otherwise there will be a warning
def UserSelection():
    menu = """
        MENU
        +—————————————————————————————————————————+
        | 1. Display                              |
        | 2. Statistics                           |
        | 3. Subset                               |
        | 4. Search                               |
        | 5. Singup                               |
        | 6. Cancellation                         |
        | 7. Operation                            |
        | 8. Record                               |
        | 99. Logout                              |
        +—————————————————————————————————————————+
        """
    print(menu)
    selection = int(input("Please select your function number in the menu: "))
    if selection == 1:
        Display() # see the later function code below line169
    elif selection == 2:
        Statistics() # see the later function code below line189
    elif selection == 3:
        Subset()  # see the later function code below line233
    elif selection == 4:
        Search() # see the later function code below line440
    elif selection == 5:
        Signup(file) # see the later function code below
    elif selection == 6:
        Cancellation(file) # see the later function code below
    elif selection == 7:
        Operation() # see the later function code below
    elif selection == 8:
        Record() # see the later function code below
    elif selection == int(99):
        print("Successfully logged out.")
        return
    else:
        print("Please select your function based on the menu number")
        UserSelection()

################################################################################
### after the performance of the function, return back to the Main Menu
def Back2Menu():
    menu = """
        +—————————————————————————————————————————+
        | 9. Menu                                 |
        | 99. Logout                              |
        +—————————————————————————————————————————+
        """
    print(menu)
    try:
        selection = int(input("Please select your function number in the menu: "))
        if selection == 9:
            UserSelection()
        elif selection == 99:
            print("Successfully logged out")
            return
        else:
            print("Please enter the function number in the menu")
            Back2Menu()
    except ValueError:
        print("Please enter the function number in the menu")
        Back2Menu()
    except UnboundLocalError:
        print("Please enter the function number in the menu")
        Back2Menu()
    except Exception:
        print("Please enter the function number in the menu")
        Back2Menu()
################################################################################
## functions in the menu                                                      ##
################################################################################
### to store and get the header into a list
def Header():
    init = Initialization(file) # use the Initialization function read as list
    header = init[0]  # the first element should be the header
    return header
################################################################################
### to store and get the account into a list
def Accounts():
    init = Initialization(file) # use the Initialization function read as list
    accounts = init[1]  # the second element should be the account
    return accounts
################################################################################
### to show all the accounts in the file:
def Display():
    header = Header()
    accounts = Accounts()
    output = """
        +—————————————————————————————————————————+
        | 1. Display                              |
        +—————————————————————————————————————————+
        """
    print(output)
    print("Account number, Name, Age, Residency, Balance, Date")
    for row in accounts:
        print("{0}, {1}, {2}, {3}, {4}, {5}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    choice = input("Do you want to back to the main menu Y/N: ")
    if choice == "Y":
        UserSelection()
    else:
        Back2Menu()
################################################################################
def Statistics():
    import statistics  # statistics package provides the mean, median functions
    accounts = Accounts() # call Accounts function to read the list
    agelist = []  # age is a new list
    balancelist = [] # balance is a new list
    for row in accounts: # initiation for the new file
        age = int(row[2])
        balance = int(row[4])
        agelist.append(age) # add the new infomation into the list
        balancelist.append(balance) # add the new infomation into the list
    age34 = []  # Lists to store balances with corresponding ages in sub-age groups.
    age35to44 = []
    age45to54 = []
    age55to64 = []
    age65to74 = []
    age75 = []
    for time in zip(agelist, balancelist): # convert the age and balance into a dictionary
        if time[0] < 35: # for the dictionary time[0] will be the age
            age34.append(time[1])
        elif  time[0] >= 35 and time[0] < 45:
            age35to44.append(time[1])
        elif  time[0] >= 45 and time[0] < 55:
            age45to54.append(time[1])
        elif  time[0] >= 55 and time[0] < 65:
            age55to64.append(time[1])
        elif  time[0] >= 65 and time[0] < 75:
            age65to74.append(time[1])
        elif  time[0] >= 75:
            age75.append(time[1])
    output= """
    +—————————————————————————————————————————+
    | 2. Statistics                           |
    +—————————————————————————————————————————+
    """
    print(output)
    ## just subset the entire dataset
    print("Overall: \n", "{0}, {1}, {2}".format("Total", "Average", "Median"), "\n", "{0}, {1}, {2}".format(sum(balancelist), round(statistics.mean(balancelist), 2), statistics.median(balancelist)))
    print("Under 35: \n", "{0}, {1}, {2}".format("Total", "Average", "Median"), "\n","{0}, {1}, {2}".format(sum(age34), round(statistics.mean(age34), 2), statistics.median(age34)))
    print("Age 35-44: \n" , "{0}, {1}, {2}".format("Total", "Average", "Median"), "\n", "{0}, {1}, {2}".format(sum(age35to44), round(statistics.mean(age35to44), 2), statistics.median(age35to44)))
    print("Age 45-54: \n" , "{0}, {1}, {2}".format("Total", "Average", "Median"), "\n", "{0}, {1}, {2}".format(sum(age45to54), round(statistics.mean(age45to54), 2), statistics.median(age45to54)))
    print("Age 55-64: \n" , "{0}, {1}, {2}".format("Total", "Average", "Median"), "\n", "{0}, {1}, {2}".format(sum(age55to64), round(statistics.mean(age55to64), 2), statistics.median(age55to64)))
    print("Age 65-74: \n" , "{0}, {1}, {2}".format("Total", "Average", "Median"), "\n", "{0}, {1}, {2}".format(sum(age65to74), round(statistics.mean(age65to74), 2), statistics.median(age65to74)))
    print("Above 75: \n" , "{0}, {1}, {2}".format("Total", "Average", "Median"), "\n", "{0}, {1}, {2}".format(sum(age75), round(statistics.mean(age75), 2), statistics.median(age75)))
    ## user's choice for next step
    choice = input("Do you want to back to the main menu Y/N: ")
    if choice == "Y":
        UserSelection()
    else:
        Back2Menu()
################################################################################
def Subset():
    menu =  """
        +—————————————————————————————————————————+
        | 3. Subset                               |
        |     31. By Age                          |
        |     32. By Residency                    |
        |     33. By Balance                      |
        |     34. By Date                         |
        | 9. Menu                                 |
        +—————————————————————————————————————————+
        """
    print(menu)
    try:
        selection = int(input("Please enter the function number: "))
        if selection== 31:
            ByAge()
        elif selection== 32:
            ByResidency()
        elif selection == 33:
            ByBalance()
        elif selection== 34:
            ByDate()
        elif selection == 9:
            Back2Menu()
        else:
            print("Please enter the function number in the menu")
            Subset()
    except ValueError:
        print("Please enter the function number in the menu")
        Subset()
    except Exception:
        print("Please enter the function number in the menu")
        Subset()
################################################################################
def  Back2Subset():
    menu = """
        +—————————————————————————————————————————+
        | 9. Menu                                 |
        | 99. Logout                              |
        +—————————————————————————————————————————+
        """
    print(menu)
    try:
        selection = int(input("Please select your function number: "))
        if selection == 9:
            UserSelection()
        elif selection == 99:
            print("Successfully logged out")
            return
        else:
            print("Please enter the function number in the menu")
            Back2Subset()
    except ValueError:
        print("Please enter the function number in the menu")
        Back2Subset()
    except UnboundLocalError:
        print("Please enter the function number in the menu")
        Back2Subset()
    except Exception:
        print("Please enter the function number in the menu")
        Back2Subset()
################################################################################
def ByAge():
    accounts = Accounts()
    output =  """
        +—————————————————————————————————————————+
        | 3. Subset                               |
        |     31. By Age                          |
        +—————————————————————————————————————————+
        """
    print(output)

    try:
        min = int(input("Please enter the minimum age: "))
        max = int(input("Please enter the maximum age: "))
        print("Account number, Name, Age, Residency, Balance, Date")
        if min> max:
            raise TypeError
        if min < 0 or max < 0:
            raise Exception
        else:
            for row in accounts:
                age = int(row[2])
                if age >= min and age <= max:
                    print("{0}, {1}, {2}, {3}, {4}, {5}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    except ValueError:
        print("Please enter a valid age range")
        ByAge()
    except TypeError:
        print("Please enter a valid age range")
        ByAge()
    except Exception:
        print("Please enter a valid age range")
        ByAge()
    choice = input("Do you want to check another subset Y/N: ")
    if choice == "Y":
        Subset()
    elif choice == "N":
        UserSelection()
    else:
        Back2Menu()
################################################################################
def ByResidency():
    accounts = Accounts()
    output = """
        +—————————————————————————————————————————+
        | 3. Subset                               |
        |     32. By Residency                    |
        +—————————————————————————————————————————+
        """
    print(output)
    resident = str(input("Please enter a state residency: "))
    print("Account number, Name, Age, Residency, Balance, Date")
    for row in accounts:
        residency = str(row[3])
        if resident == residency:
            print("{0}, {1}, {2}, {3}, {4}, {5}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    choice = input("Do you want to check another subset Y/N: ")
    if choice == "Y":
        Subset()
    elif choice == "N":
        UserSelection()
    else:
        Back2Subset()
################################################################################
def ByBalance():
    accounts = Accounts()
    output =  """
        +—————————————————————————————————————————+
        | 3. Subset                               |
        |     33. By Balance                      |
        +—————————————————————————————————————————+
        """
    print(output)
    try:
        min = int(input("Please enter the minimum balance: "))
        max = int(input("Please enter the maximum balance: "))
        if min > max:
            raise TypeError
        if min < 0 or max< 0:
            raise Exception
        print("Account number, Name, Age, Residency, Balance, Date")
        subbalance_result = False  # Check if the corresponding records are found or not.
        for row in accounts:
            balance = int(row[4])
            if balance >= min and balance <= max:
                print("{0}, {1}, {2}, {3}, {4}, {5}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    except TypeError:
        print("Please enter a valid balance range")
        ByBalance()
    except Exception:
        print("Please enter a valid balance range")
        ByBalance()
    choice = input("Do you want to check another subset Y/N: ")
    if choice == "Y":
        Subset()
    elif choice == "N":
        UserSelection()
    else:
        Back2Subset()
################################################################################
def ByDate():
    import datetime
    header = Header()
    accounts = Accounts()
    output =  """
        +—————————————————————————————————————————+
        | 3. Subset                               |
        |     34. By Date                         |
        +—————————————————————————————————————————+
        """
    print(output)
    min_str = str(input("Please enter the starting mm/dd/yyyy: "))
    max_str = str(input("Please enter the ending mm/dd/yyyy: "))
    min_date = datetime.datetime.strptime(min_str, '%m/%d/%Y').date()
    max_date = datetime.datetime.strptime(max_str, '%m/%d/%Y').date()
    print("{0}, {1}, {2}, {3}, {4}, {5}".format(header[0], header[1], header[2], header[3], header[4], header[5]))
    for row in accounts:
        date = str(row[5])
        date1 = datetime.datetime.strptime(date, '%m/%d/%Y').date()
        if date1 >= min_date and date1 <= max_date:
            print("{0}, {1}, {2}, {3}, {4}, {5}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    choice = input("Do you want to check another subset Y/N: ")
    if choice == "Y":
        Subset()
    elif choice == "N":
        UserSelection()
    else:
        Back2Subset()
################################################################################
def Search():
    header = Header()
    accounts = Accounts()
    menu =  """
        +—————————————————————————————————————————+
        | 4. Search                               |
        |     41. By AccNum                       |
        |     42. By Name                         |
        | 9. Menu                                 |
        +—————————————————————————————————————————+
        """
    print(menu)
    try:
        selection = int(input("Please enter function number: "))
        if selection== 41:
            ByAccNum()
        elif selection== 42:
            ByName()
        elif selection == 9:
            Back2Menu()
        else:
            print("Please enter the function number in the menu")
            Search()
    except ValueError:
        print("Please enter the function number in the menu")
        Search()
    except Exception:
        print("Please enter the function number in the menu")
        Search()
################################################################################
def  Back2Search():
    menu = """
        +—————————————————————————————————————————+
        | 9. Menu                                 |
        | 99. Logout                              |
        +—————————————————————————————————————————+
        """
    print(menu)
    try:
        selection = int(input("Please select your function number in the menu: "))
        if selection == 9:
            UserSelection()
        elif selection == 99:
            print("Successfully logged out")
            return
        else:
            print("Successfully logged out")
            return
    except ValueError:
        print("Please enter the function number in the menu")
        Back2Search()
    except UnboundLocalError:
        print("Please enter the function number in the menu")
        Back2Search()
    except Exception:
        print("Please enter the function number in the menu")
        Back2Search()
################################################################################
def ByAccNum():
    accounts = Accounts()
    output = """
        +—————————————————————————————————————————+
        | 4. Search                               |
        |     41. By AccNum                       |
        +—————————————————————————————————————————+
        """
    print(output)
    accnum = int(input("Please enter your AccuNum: "))
    print("Account number, Name, Age, Residency, Balance, Date")
    exist = False
    for row in accounts:
        AccNum = int(row[0])
        if accnum == AccNum:
            exist = True
            print("{0}, {1}, {2}, {3}, {4}, {5}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        else:
            continue
    if not exist:
        print("AccNum does not exist")
        Search()

    choice = input("Do you want to search another account Y/N: ")
    if choice == "Y":
        Search()
    elif choice == "N":
        UserSelection()
    else:
        Back2Search()
################################################################################
def ByName():
    accounts = Accounts()
    output = """
        +—————————————————————————————————————————+
        | 4. Search                               |
        |     42. By Name                         |
        +—————————————————————————————————————————+
        """
    print(output)
    exist = False
    name = str(input("Please enter the UserName: "))
    print("Account number, Name, Age, Residency, Balance, Date")
    for row in accounts:
        Name = str(row[1])
        if name == Name:
            exist = True
            print("{0}, {1}, {2}, {3}, {4}, {5}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    if not exist:
        print("UserName does not exist")
        Search()
    choice = input("Do you want to search another account Y/N: ")
    if choice == "Y":
        Search()
    elif choice == "N":
        Back2Search()
    else:
        Back2Menu()
################################################################################
def Signup(file):
    import random
    import datetime
    header = Header()
    accounts = Accounts()
    menu =  """
        +—————————————————————————————————————————+
        | 5. Singup                               |
        +—————————————————————————————————————————+
        """
    print(menu)
    new = random.randint(100, 9999)
    for row in accounts:
        if new == int(row[0]):
            print(new)
            Signup(file)
    new_num = str(new)
    new_name = str(input("Please enter the new UserName: "))
    new_age = str(input("Please enter the new Age: "))
    new_res = str(input("Please enter the new Residency: "))
    new_bal = str(input("Please enter the new Balance: "))
    new_date =  str(datetime.date.today().strftime("%m/%d/%y"))
    print(new_num, new_name, new_age, new_res, new_bal, new_date)
    with open(file, "a") as data:
        new_list = [new_num, new_name, new_age, new_res, new_bal, new_date]
        new_account = ','.join(new_list)
        data.write(new_account + "\n")
        data.close()
    print("Here is your new account information:")
    print("AccNum:", new_num, "\nUserName:", new_name, "\nAge:", new_age, "\nResidency:", new_res, "\nBalance:", new_bal, "\nDate:", new_date)
    choice = input("Do you want to check with Display Y/N: ")
    if choice == "Y":
        Display()
    elif choice == "N":
        UserSelection()
    else:
        Back2Menu()
################################################################################
def Cancellation(file):
    menu =  """
        +—————————————————————————————————————————+
        | 6. Cancellation                         |
        +—————————————————————————————————————————+
        """
    print(menu)
    accounts = Accounts()
    result = False
    del1 = input('Please enter the AccNum to delete: ')
    data = open(file, "r")
    info = data.readlines()
    for n in range(1, len(info)):
        accnum = (info[n]).split(",")[0]
        if accnum == del1:
            result = True
            del info[n]
            print("Successfully deleted: ", accnum, result)
            break
    data = open(file, "w")
    for list in info:
        data.write('%s' % list)
    data.close()
    if result == False:
        print("The account does not exist")
    choice = input("Do you want to check with Display: Y/N ")
    if choice == "Y":
        Display()
    elif choice == "N":
        UserSelection()
    else:
        Back2Menu()
################################################################################
def Operation():
    result = False
    menu = """
        +—————————————————————————————————————————+
        | 7. Operation                            |
        +—————————————————————————————————————————+
        """
    print(menu)
    AccNum = int(input('Please enter the AccNum: '))
    if GetAccount(AccNum) == None:
        selection = 9
        print("AccNum does not exist")
        choice = input("Do you want find Another AccNum Y/N: ")
        if choice == "Y":
            Operation()
        elif choice == "N":
            UserSelection()
        else:
            Back2Menu()
    else:
        result = True
        menu = """
        +—————————————————————————————————————————+
        | 7. Operation                            |
        |     71. Deposit                         |
        |     72. Withdraw                        |
        |     73. Transfer                        |
        |     74. Show                            |
        |     75. Change                          |
        |     76, History                         |
        | 9. Menu                                 |
        +—————————————————————————————————————————+
        """
        print(menu)
        try:
            selection = int(input('Please enter the function number: '))
            if selection == 71:
                BankAccount(AccNum).Deposit()
            elif selection== 72:
                BankAccount(AccNum).Withdraw()
            elif selection == 73:
                BankAccount(AccNum).Transfer()
            elif selection == 74:
                BankAccount(AccNum).Show()
            elif selection == 75:
                BankAccount(AccNum).Change()
            elif selection == 76:
                BankAccount(AccNum).History()
            elif selection == 9:
                UserSelection()
            else:
                choice = input("Do you want find Another AccNum Y/N: ")
                if choice == "Y":
                    Operation()
                elif choice == "N":
                    UserSelection()
                else:
                    Back2Menu()
        except ValueError:
            print('Input is invalid. Please enter an integer number in the list.')
################################################################################
def Record():
    menu = """
        +—————————————————————————————————————————+
        | 8.Record                                |
        +—————————————————————————————————————————+
        """
    print(menu)
    history = open("history.txt", "r")
    for event in history:
        print(event)
    choice = input("Do you want to get back to menu Y/N: ")
    if choice == "Y":
        UserSelection()
    else:
        Back2Menu()
################################################################################
## User function                                                              ##
################################################################################
### to get hte account with a specific AccNum
def GetAccount(AccNum):
    accounts = Accounts() # use the Accounts function to get the list
    for row in accounts: # iteration for all the individual row store into the
        if int(row[0]) == AccNum:  # AccNum is in 0 index.
            return row
################################################################################
### Update the file after information changes
def Update(accounts):
    header = Header()
    with open(file, "w+") as data: # open the file to write new information
        data.write(",".join(header) + "\n")
        for row in accounts: # iteration for each individual row
            row1 = ",".join(row)  # change the list into a string
            data.write(row1 + "\n")
        data.close()
###############################################################################
class BankAccount:
    import datetime
    def __init__ (self, AccNum):
        self.__AccNum = int(GetAccount(AccNum)[0])
        self.__AccName = GetAccount(AccNum)[1]
        self.__AccAge = int(GetAccount(AccNum)[2])
        self.__AccResidency = str(GetAccount(AccNum)[3])
        self.__AccBalance = int(GetAccount(AccNum)[4])
        self.__AccDate = GetAccount(AccNum)[5]
#-----------------------------------------------------------------------------#
    def Deposit(self):
        import datetime
        now=datetime.datetime.now().date()
        try:
            DepMoney = int(input('I want to deposit: $'))
            if DepMoney < 0:
                print("Please enter a valid deposite amount")
                DepMoney = 0
                BankAccount(self.__AccNum).Deposit()
            else:
                self.__AccBalance += DepMoney
                accounts = Accounts()
            for n in range(0, len(accounts)):
                if int(accounts[n][0]) == int(self.__AccNum):
                    accounts[n][4] = str(self.__AccBalance)
                    break
            Update(accounts)
            print("you just deposit $", DepMoney, "into", self.__AccNum )
            history = open("history.txt", "a")
            history.write("AccNum: " + str(self.__AccNum) + ", Name: "
                          + str(self.__AccName) + ", Time: " + now.strftime("%m/%d/%Y"))
            history.write(", Action: Deposit" + ", Amount: "
                          + str(DepMoney) + ', Balance: '+ str(self.__AccBalance) +"\n")
            history.close()
            with open("AccNum"+ str(self.__AccNum) + " personal file.txt", "a") as person:
                person.write("AccNum: " + str(self.__AccNum) + ", Name: "
                             + str(self.__AccName) + " Time: " + now.strftime("%m/%d/%Y"))
                person.write(", Action: Deposit" + ", Amount: " + str(DepMoney)
                             + ', Balance: '+ str(self.__AccBalance) +"\n")
                person.close()
        except Exception:
            print("Please enter a valid deposite amount")
            BankAccount(self.__AccNum).Deposit()
        Operation()
#-----------------------------------------------------------------------------#
    def Withdraw(self):
        import datetime
        now=datetime.datetime.now().date()
        WitMoney = input("I want to withdraw: $")
        WitMoney = int(WitMoney)
        if WitMoney < 0:
            print("Please enter a valid withdraw amount")
            WitMoney =0
            BankAccount(self.__AccNum).Withdraw()
        elif WitMoney > self.__AccBalance:
            choice = input("Do you want to Deposit more and Withdraw Y/N: ")
            WitMoney = 0
            if choice == "Y":
                BankAccount(self.__AccNum).Deposit()
            elif choice == "N":
                print("Low interest Usury! Please Contact 314-285-6207")
                BankAccount(self.__AccNum).Withdraw()
            else:
                print("Someone does not know how number works")
                BankAccount(self.__AccNum).Withdraw()
        else:
            self.__AccBalance -= WitMoney
            accounts = Accounts()
            for n in range(0, len(accounts)):
                if int(accounts[n][0]) == int(self.__AccNum):
                    accounts[n][4] = str(self.__AccBalance)
                    break
            Update(accounts)
            print("you just withdraw $", WitMoney, "from", self.__AccNum )
            history = open("history.txt", "a")
            history.write("AccNum: " + str(self.__AccNum) + ", Name: "
                              + str(self.__AccName) + ", Time: " + now.strftime("%m/%d/%Y"))
            history.write(", Action: Withdraw" + ", Amount: " + str(WitMoney)
                          + ', Balance: '+ str(self.__AccBalance) +"\n")
            history.close()
            with open("AccNum"+ str(self.__AccNum) + " personal file.txt", "a") as person:
                person.write("AccNum: " + str(self.__AccNum) + ", Name: "
                             + str(self.__AccName) + ", Time: " + now.strftime("%m/%d/%Y"))
                person.write(", Action: Withdraw" + ", Amount: " + str(WitMoney)
                             + ', Balance: '+ str(self.__AccBalance) +"\n")
                person.close()
        Operation()
#-----------------------------------------------------------------------------#
    def Transfer(self):
        import datetime
        now=datetime.datetime.now().date()
        Receiver = int(input("I want to send to AccNum: "))
        if GetAccount(Receiver) == None:
            print("AccNum does not exist")
            BankAccount(self.__AccNum).Transfer()
        else:
            RecNum = Receiver
            RecName = GetAccount(Receiver)[1]
            RecBalance = int(GetAccount(Receiver)[4])
            SendMoney = int(input("I want to send: $"))
            if SendMoney >= self.__AccBalance:
                print("We buy kidneys. Please contact 269-267-7489")
                BankAccount(self.__AccNum).Show()
            elif SendMoney < 0:
                print("Hey, Stop robbing people")
                BankAccount(self.__AccNum).Show()
            else:
                self.__AccBalance -= SendMoney
                RecBalance += SendMoney
                print("you just transfer $", SendMoney, " from ", self.__AccNum, " to ", Receiver)
                accounts = Accounts()
                for n in range(0, len(accounts)):
                    if int(accounts[n][0]) == int(self.__AccNum):
                        accounts[n][4] = str(self.__AccBalance)
                    if int(accounts[n][0]) == int(Receiver):
                        accounts[n][4] = str(RecBalance)
                Update(accounts)
                history = open("history.txt", "a")
                history.write("AccNum: " + str(self.__AccNum) + ", Name: " + str(self.__AccName)
                              + ", Time: " + now.strftime("%m/%d/%Y") )
                history.write(", Action: Sending" + ", Amount: " + str(SendMoney)
                              + ", Balance: " + str(self.__AccBalance) +"\n")
                history.write("AccNum: " + str(RecNum) + ", Name: "
                              + str(RecName) + ", Time: " + now.strftime("%m/%d/%Y"))
                history.write(", Action: Receive" + ", Amount: "
                              + str(SendMoney) + ", Balance: " + str(RecBalance) +"\n")
                history.close()
                with open("AccNum"+ str(self.__AccNum) + " personal file.txt", "a+") as person:
                    person.write("AccNum: " + str(self.__AccNum) + ", Name: " + str(self.__AccName)
                                 + ", Time: " + now.strftime("%m/%d/%Y"))
                    person.write(", Action: Sending" + ", Amount: " + str(SendMoney)
                                 + ", Balance: " + str(self.__AccBalance) +"\n")
                    person.close()
                with open("AccNum"+ str(RecNum) + " personal file.txt", "a+") as person:
                    person.write("AccNum: " + str(RecNum) + ", Name: " + str(RecName)
                                 + ", Time: " + now.strftime("%m/%d/%Y"))
                    person.write(", Action: Receive" + ", Amount: " + str(SendMoney)
                                 + ", Balance: " + str(RecBalance) +"\n")
                    person.close()
        Operation()
#-----------------------------------------------------------------------------#
    def Show(self):
        import datetime
        now=datetime.datetime.now().date()
        print("Account number, Name, Age, Residency, Balance, Date")
        print(GetAccount(self.__AccNum))
        history = open("history.txt", "a")
        history.write("AccNum: " + str(self.__AccNum) + ", Name: "
                      + str(self.__AccName) + ", Time: " + now.strftime("%m/%d/%Y"))
        history.write(", Action: Showing" + ", Balance: "+ str(self.__AccBalance) +"\n")
        history.close()
        with open("AccNum"+ str(self.__AccNum) + " personal file.txt", "a") as person:
            person.write("AccNum: " + str(self.__AccNum) + " Name: "
                         + str(self.__AccName) + " Time: " + now.strftime("%m/%d/%Y"))
            person.write(", Action: Showing" + ", Balance: "+ str(self.__AccBalance) +"\n")
            person.close()
        Operation()
#-----------------------------------------------------------------------------#
    def Change(self):
        import datetime
        accounts = Accounts()
        now = datetime.datetime.now().date()
        print("Account number, Name, Age, Residency, Balance, Date")
        print(GetAccount(self.__AccNum))
        NewName = input("Please enter a new name: ")
        if NewName == "":
            NewName = str(self.__AccName)
        NewAge = int(input("Please enter a new age: "))
        if NewAge < 0:
            print("Wait until you get borned")
            BankAccount(self.__AccNum).Change()
        elif NewAge < 18:
            print("I need to see your parents")
            BankAccount(self.__AccNum).Change()
        elif NewAge >= 100:
            print("What do you eat daily")
            BankAccount(self.__AccNum).Change()
        else:
            NewResidency = input("Please enter a new residency: ")
            if NewResidency == "":
                NewResidency = self.__AccResidency
            for n in range(0, len(accounts)):
                if int(accounts[n][0]) == int(self.__AccNum):
                    accounts[n][1] = NewName
                    accounts[n][2] = str(NewAge)
                    accounts[n][3] = NewResidency
                    print("Successfully Change you indentity")
                    print("Account number, Name, Age, Residency, Balance, Date")
                    print("{0}, {1}, {2}, {3}, {4}, {5}".format(self.__AccNum, NewName,
                                                                NewAge, NewResidency,
                                                                self.__AccBalance, now.strftime("%m/%d/%Y")))
                    break
            Update(accounts)
            history = open("history.txt", "a")
            history.write("AccNum: " + str(self.__AccNum) + ", Name: "
                          + str(self.__AccName) + ", Time: " + now.strftime("%m/%d/%Y")
                          + ", Action: ChangeName, Name: " + str(self.__AccName) + ', into: '
                          + str(NewName) + ", Action: ChangeAge" + ", Age: " + str(self.__AccAge)
                          + ', into: '+ str(NewAge) + ", Action: ChangeRes"
                          + ", Residency: " + str(self.__AccResidency)
                          + ', into: '+ str(NewResidency) +"\n")
            history.close()
            with open("AccNum"+ str(self.__AccNum) + " personal file.txt", "a") as person:
                person.write("AccNum: " + str(self.__AccNum) + ", Name: "
                          + str(self.__AccName) + ", Time: " + now.strftime("%m/%d/%Y")
                          + ", Action: ChangeName, Name: " + str(self.__AccName) + ', into: '
                          + str(NewName) + ", Action: ChangeAge" + ", Age: " + str(self.__AccAge)
                          + ', into: '+ str(NewAge) + ", Action: ChangeRes"
                          + ", Residency: " + str(self.__AccResidency)
                          + ', into: '+ str(NewResidency) +"\n")
                person.close()
        Operation()
#-----------------------------------------------------------------------------#
    def History(self):
        with open('AccNum'+ str(self.__AccNum) + ' personal file.txt', 'r+') as person:
            for event in list(person):
                print(event)
        Operation()
################################################################################
################################################################################
file = #"put your file dierctory here"
Login()
