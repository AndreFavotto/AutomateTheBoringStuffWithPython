#This code converts a list into a string

words = ['apples', 'bananas', 'grapes', 'watermelons']
i = 0
string = ''
while i <= len(words) - 2:
    string = string + words[i] + ', '
    i+=1
print(string + 'and ' + words[len(words)-1] + '.')