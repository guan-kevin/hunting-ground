import random
print('fixed')
with open('texts/hello.txt', 'r') as f:
    for line in f:
        print(line.rstrip())
if random.randint(0, 1) == 0:
    # runtime error
    print(x)
else:
    print('No Error')
