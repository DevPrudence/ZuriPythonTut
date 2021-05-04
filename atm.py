import datetime
now = datetime.datetime.now()
name = input ("What is your name? \n")
AllowedUsers = ['Bisi', 'Tola', 'Fade', 'John']
AllowedPassword = ['PasswordBisi', 'PasswordTola', 'PasswordFade', 'PasswordJohn']
if (name in AllowedUsers):
    password = input ("What is your password? \n")
    userid = AllowedUsers.index(name)
    if (password == AllowedPassword[userid]):
        print ('Welcome %s' % name)
        print('Current date and time')
        print (now.strftime ("%d/%m/%Y %H:%M:%S"))
        print ('These are the available options')
        print ('1. Withdraw')
        print ('2. Cash Deposit')
        print ('3. Complaints')
        selectedOption = int(input('Please select an option \n'))
        if (selectedOption == 1):
            deposit = input('How much would you like to withdraw? \n')
            print ('Current balance')
        elif (selectedOption == 2):
            deposit = input('How much would you like to deposit? \n')
            print ('Current balance')
        elif (selectedOption == 3):
            complaint = input('What issue will you like to report? \n')
            print ('Thank you for contacting us')
    else:
        print ('Password incorrect, please try again')
else:
    print ('Username not found, please try again')
