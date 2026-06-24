print('Enter your total marks :')

marks1 = int(input())
marks2 = int(input())
marks3 = int(input())
marks4 = int(input())
marks5 = int(input())

avg = int(marks1 + marks2 + marks3 + marks4 + marks5 / 5)
print(avg)
Validrange = range(0, 101)

if avg not in Validrange:
    print('Invalid avg score/grade')
elif avg in range(100,101):
    print('S+')
elif avg in range(95,101):
    print('S')
elif avg in range(91,101):
    print('A+')
elif avg in range(85,101):
    print('A')
elif avg in range(80,101):
    print('A-')
elif avg in range(77,101):
    print('B+')
elif avg in range(75,101):
    print('B')
elif avg in range(70,101):
    print('B-')
elif avg in range(65,101):
    print('C+')
elif avg in range(60,101):
    print('C')
elif avg in range(50,101):
    print('C-')
elif avg in range(40,101):
    print('D+')

