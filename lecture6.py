print("hi\n" * 10)


cnt = 1
for i in range(9):
    print(str(cnt) * cnt)
    cnt+=1

## guess number
"""
import random
answer = int(random.randrange(1, 100))
print("Guess number between 1 and 100:", end=" ")
while True:
    guessed_answer = int(input())
    if type(guessed_answer) == int and int(guessed_answer) >= 1 and int(guessed_answer) <= 100:
        if guessed_answer == answer:
            print('Congratulations, you’re correct!')
            break
        elif guessed_answer > answer:
            print('Guess lower:', end=" ")
        elif guessed_answer < answer:
            print('Guess higher:', end=" ")
"""

## break if uneven num
first_list = [3, 7, 9, 2, 6]
for i in first_list:
    if not (i % 2) == 0:
        print("uneven not allowed")
        break
    else:
        print(i)

second_list = [2, 3, 6, 7, 9]
third_list = []

## combine lists into list of tuples
for second_list in first_list:
    add_to_tuple = second_list, first_list.index(second_list)
    third_list.append(add_to_tuple)
print(third_list)

## List comprehension ver.
fourth_list = [(second_list, first_list.index(second_list)) for second_list in first_list]
print(fourth_list)


## Fill basket
fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
print("How many fruits does your basket fit?",end=" ")
requested_fruits = int(input())
my_basket = []
for i in range(requested_fruits):
    for i in fruits:
        if len(my_basket) < requested_fruits:
            my_basket.append(i)
print(my_basket)

#t = [fruits[i] for i in range(requested_fruits)]
 

#find prime numbers
start = 2
finish = 100
while start < finish:
    i = 2
    while i < start//2:
        if start % i == 0:
            break
        i += 1
    else:
        print(start, end=" ")
    start += 1