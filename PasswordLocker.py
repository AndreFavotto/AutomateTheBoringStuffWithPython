#! python3
# PasswordLocker.py - An insecure password locker program. This code saves accounts passwords. 
'''In order to run this code from terminal, you need to download the file 'PasswordLocker.bat' and 
add it's path to your environment variables (PATH). As it's done, open your command prompt ant type 
PasswordLocker.'''
import sys, pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
 'luggage': '12345',
 'facebook': '154789'}

def main(op):
    if op == 'add':
        account = input("Type the new account's name: ")
        password = input("Type the new account's password: ")
        if account not in PASSWORDS:
            PASSWORDS.setdefault(account, password)
            pyperclip.copy(PASSWORDS[account])
            print(f'{account} succesfully added and copied to the clipboard.')
            '''note that this file won't actually be saved, we'd need to open a separated
            file and open it in the program to do so''' 
            sys.exit()
        else:
            print('You already have this account registered! Try editing it.')
        sys.exit()
    elif op == 'edit':
        account = input("Type the account's name: ")
        if account not in PASSWORDS:
            print('This account is not registered yet')
            sys.exit()
        password = input("Type the new account's password: ")
        PASSWORDS[account] = password
        pyperclip.copy(PASSWORDS[account])
        print(f'New password succesfully edited and copied to the clipboard.')
      
    elif op == 'delete':
        account = input("Type the account's name you want to delete: ")
        try:
            del PASSWORDS[account]
            print(f'{account} succesfully deleted.')
        except:
            print("You don't have this account registered yet!")
    else:
        if op in PASSWORDS:
            pyperclip.copy(PASSWORDS[op])
            print('Password for ' + op + ' copied to clipboard.')
        else:
            print('There is no account named ' + op)

if len(sys.argv) <2:
    print('''Usage: type: "PasswordLocker [account] " to copy account password;
"PasswordLocker add" to add a new account and password;
"PasswordLocker edit" to edit an account's password;
"PasswordLocker delete" to delete an account.''')
    sys.exit()
op = sys.argv[1]
main(op)
