#This code identifies brazillian phonenumbers and email addresses in any text copied to the clipboard
import re, pyperclip

text = pyperclip.paste()
phonereg = re.compile(r'''(
    (\(?0?\d{2}\)?)     #Area Code
    (\s|-|\.)?          #Separation (optional)
    (9?\d{4})           #First five/four digits
    (\s|-|\.)?          #Separation (optional)
    (\d{4})             #Last Four Digits
)''', re.VERBOSE)
emailreg = re.compile(r'''(
    [a-zA-Z0-9._%+-]+    #Username
    @                    #Separation
    [a-zA-Z0-9.-]+       #Email Domain
    (\.[a-zA-Z]{2,4})    #Suffix
)''', re.VERBOSE)
phMatches = phonereg.findall(text)
emailMatches = emailreg.findall(text)
emails = []
for group in range(len(emailMatches)):
    emails.append(emailMatches[group][0])
phones = []
for group in range(len(phMatches)):
    a_code = phMatches[group][1]
    if '(' in a_code: #removing parethesis from area code
        a_code = a_code[1:-1]
    if '0' in a_code: #removing 0 from area code
        a_code = a_code[1:]
    phones.append('(' + a_code + ')' + phMatches[group][3] + '-' + phMatches[group][5])
if emails == []:
    print('No emails found')
else:
    print(f'Emails found:\n{", ".join(emails)}')
if phones == []:
    print('No phones found')
else:
    print(f'Phones found:\n{", ".join(phones)}')
