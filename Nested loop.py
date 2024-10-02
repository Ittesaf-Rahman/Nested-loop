i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(j,end=", ")
        j = j + 1
    i = i + 1
    print("")

for k in range(1, 6):
    for l in range(1, 11):
        print(l, end=(', '))
    print("")

My_string = input("Enter a string = ")
My_char = input("Enter a Char = ")
find = 0
count = 0
while find < len(My_string):
    if My_string[find] == My_char:
        count = count + 1
    find = find + 1
print(count)

upper = int(input("Enter upper number = "))
lower = int(input("Enter lower number = "))
for num in range(lower, upper + 1):
    if num > 2:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

number = 12345678
number_str = str(abs(number))
number_len = len(number_str)
if (number_len % 2) == 1:
    mid_number = number_str[number_len // 2]
else:
    mid_left = number_len // 2 - 1
    mid_right = number_len // 2
    mid_number = mid_left * mid_right
print(mid_number)

