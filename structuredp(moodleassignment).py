# NAME = KISAKYE MARIA SENGENDO
# REG. NO. = S24B38/033      ACCESS NO. = B30260
# BACHELOR OF SCIENCE IN DATA SCIENCE AND ANALYTICS



##Even Odd checker: 
num = int(input("enter a number: "))
if num % 2 == 0:
    print("It is even")
else:
    print("It is odd")


##Reverse string:
def reverse_string(word):
    return word[::-1]

word = "Boy"
reversed_string = reverse_string(word)
print(reversed_string)


##Multiplication table:
for a in range(1, 7):
    for b in range(1, 7):
        result = a*b
        print(f"{a} * {b} = {result}")


##Fizzbuzz:
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 ==0:
        print("Buzz")
    else:
        print(num)


##Maximum:
def find_maximum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

max_number=find_maximum(50, 90, 20)
print(f'{max_number}')


##Print numbers:
for number in range(11):
    if number == 4 or number == 8:
        continue
    print(number, end=" ")



