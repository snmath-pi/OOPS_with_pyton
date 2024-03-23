import os
while True:
    print('\n 1. Add Record... ')
    print('\n 2. Display Records... ')
    print('\n 3. Search Student Record By Name... ')
    print('\n 4. Search Student Record Roll No... ')
    print('\n 5. Delete Student Record By Name... ')
    print('\n 6. Update Student Record')
    print('\n 7. Exit')
    
    n = int(input('Enter your choice...'))
    if n == 7: break
    elif n == 1: 
        print('***Enter Student Details 🚀***\n')
        name = input('Enter Name... ')
        roll = input('Enter Roll No... ')
        c1 = input('Enter class... ')
        fees = input('Enter fees... ')
        per = input('Enter percentage... ')
        f = open('student.txt', 'a')
        f.write(name + '-' + roll + '-' + c1 + 
                '-' + fees + '-' + per + 
                '\n')
        print('Record Added Successfully ✅')
        f.close()
    elif n == 2:
        print('\n\n List of present Records... ')
        print('NAME-ROLLNO-CLASS-FEES-PER')
        f = open('student.txt', 'r')
        while True:
            d = f.readline()
            if len(d) == 0:break
            print(d.strip())
        f.close()
    
        
        
