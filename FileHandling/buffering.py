f = open('data.txt', mode='r', buffering=10, encoding='utf-8')
if f: 
    print('opened')
print(f.name)
print(f.encoding)
print(f.mode)
print(f.closed)

f.close()

print(f.closed)