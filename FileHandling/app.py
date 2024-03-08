# age = input('Enter you age:')
# f = open('data.txt', 'w')
# f.write(age)

# f.close()

f = open('data.txt', 'r')
if f:
    print('successfully opened')
print(type(f))
