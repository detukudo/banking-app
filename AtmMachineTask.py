import datetime

now = datetime.datetime.now()
name = input('What is your name \n')
allowedUsers = ['David','John','James']
allowedPasswords = ['passwordDavid','passwordJohn','passwordJames']

if (name in allowedUsers):
    password = input('Type your password \n')
    userId = allowedUsers.index(name)

    if (password == allowedPasswords[userId]):
        print ("Current date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        print ('Welcome {}\n'.format(name))
        print('Here are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Account Balance')
        print('4. Complaint')

        selectedOption = int(input('Please select an option \n'))

        if(selectedOption == 1):
            amount = input('Please enter amount to withdraw \n')
            print('counting....... \n')
            print('Please take your {} cash, thank you'.format(amount))

        elif(selectedOption == 2):
            amount = input('Please enter amount to deposit \n')
            print('counting....... \n')
            print('Your balance has been credited with {}, thank you'.format(amount))

        elif(selectedOption == 3):
            print('1. Savings')
            print('2. Current')
            accountType = int(input('Select your account type \n'))
            if(accountType == 1):
                print('Your Savings account balance is .....')

            elif(accountType == 2):
                print('Your Current account balance is ......')

            else:
                print('Invalid account type, please try again')
            
        elif(selectedOption == 4):
            complaint = input('Please enter your complaint \n')
            print('Your complaint: \n\n {} \n\nhas been noted, and will be addressed shortly \nThank you'.format(complaint))

        else:
            print('Invalid option, please try again')

    else:
        print('Password incorrect, pls try again')

else:
    print('Name not found, please try again')