import random
def check(ans, count):
    while not (isinstance(ans, int) and ans > 0 and ans < 21):
        print('Number must be an integer between 1 and 20!')
        ans = eval(input('Take a guess: '))
    if count > 1:
         ans = eval(input('Wrong answer! Try again: '))
    count += 1
    return ans, count

num = random.randint(1,20)
print("I'm thinking of an integer number between 1 and 20.")
ans = eval(input('Take a guess: '))
count = 1
ans, count = check(ans,count)
if ans == num:
    print('Right answer, you got it at first try!')
while (ans != num):
    ans, count = check(ans,count)
if(ans == num):
    print(f'Right answer, it took you {count} tries to get it!')
