import random
print('fixed')
with open('texts/hello.txt', 'r') as f:
    for line in f:
        print(line.rstrip())
if random.randint(0, 10000) == 0:
    # runtime error
    x = 0
    x = x + 'string'
    print(x)
else:
    print('No Error')
