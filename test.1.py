print('תנאים:')
print('1:')
num1: float = float(input('enter a number:'))
num2: float = float(input('enter a number:'))
if num1 < num2:
    for i in range(3):
        print(num1)
else:
    for i in range(3):
        print(num2)

print('2:')
x: int = int(input('enter a number:'))
y: int = int(input('enter a number:'))
list_2: list[int] = [x, y]
average = sum(list_2) / len(list_2)
print(average)

print('3:')
number1: int = int(input('enter a number:'))
number2: int = int(input('enter a number:'))
number3: int = int(input('enter a number:'))
if number3 < number1 > number2:
    print(number1)
elif number3 < number2 > number1:
    print(number2)
else:
    print(number3)

print('4:')

movie: int = int(input('Movie time in minutes:'))
hours: int = movie // 60
minute: int = movie % 60

print(f"The film is {hours} hour and {minute} minutes long")

print('לולאות:')

print('1:')
top: int = int(input('enter a number:'))
for i in range(1, top + 1):
    print(i, end=' ')
print()

print('2:')
num1: int = int(input('enter a number:'))
num2: int = int(input('enter a number:'))
if num1 >= num2:
    for i in range(num2, num1 + 1):
        print(i, end=' ')
else:
    for j in range(num1, num2 + 1):
        print(j, end=' ')
print()

print('עיבוד נתונים:')
print('1:')
count1: int = 0
x: int = 0
while True:
    x: int = int(input('enter a number:'))
    if count1 == 0 and x == -99:
        print('None')
    if x == -99:
        break
    else:
        count1 += x

print(count1)

print('2:')
max_number: int = None
min_number: int = None
count2: int = 0
while True:
    y: int = int(input('enter a number:'))
    if count2 == 0 and y == -99:
        print('None')
    if y <= 0:
        break
    if max_number == None or y > max_number:
        max_number = y
    if min_number == None or y < min_number:
        min_number = y
    else:
        count2 += 1
print(f'the largest number is {max_number}')
print(f'the smallest number {min_number}')

print('3:')
list3: list[int] = []
for i in range(5):
    num: int = int(input('enter a number:'))
    list3.append(num)
max3: int = max(list3)
index = list3.index(max3)
answer = index + 1
print(answer)

print('לולאות מורכבות')
print('1:')
list_tem: list[int] = []
tem: int = 0
tickets: int = 0
while not tickets == 12:
    try:
        tem: int = int(input('Enter the temperature:'))
        if tem == 0 and list_tem[-1] == 0:
            continue
        if -5 <= tem <= 40:
            print('correct data')
            list_tem.append(tem)
            tickets += 1
        else:
            print('wrong data')
            break

    except ValueError as str:
        print(' ValueError')
print(list_tem)
average1 = sum(list_tem) / len(list_tem)
print(f'the average is:{average1}')
print('the highest temperature:', max(list_tem))
print('the lowest temperature:', min(list_tem))
