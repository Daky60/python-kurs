import random

## 1 & 2
def print_numbers(num):
    return print("svar:", str(num) * int(num))


print("Enter number: ", end="")
one_input = int(input())
if one_input > 5:
    print_numbers(one_input)
else:
    for i in range(one_input):
        print_numbers(i+1)

## 3
def sort_list_one(flist):
    length = len(flist)
    for _ in range(length):
        for i in range(0, length-_-1):
            a, b = flist[i], flist[i+1]
            if a > b:
                flist[i], flist[i+1] = b, a
    return print(flist)

my_list = [1, 7, 4, 0, 15, 34, 66, 4]

sort_list_one(my_list)



def sort_biggest(a, b, indx):
    if a > b:
        a[indx], b[indx+1] = b, a

def sort_list_two(nlist):
    length = (len(nlist))
    for _ in range(length):
        for i in range(0, length-_-1):
            sort_biggest(nlist[i], nlist[i+1], i)
    return print(nlist)

sort_list_two(my_list)


## 4
def sort_list(unsorted_list):
    p = unsorted_list[(random.randrange(0, len(unsorted_list)))]
    p = unsorted_list.pop(unsorted_list.index(p))
    smaller = []
    larger = []
    sorted_list = []
    for element in unsorted_list:
        if element <= p:
            smaller.append(element)
        else:
            larger.append(element)
    if len(smaller) > 0:
        sorted(smaller)
    if len(larger) > 0:
        sorted(larger)
    sorted_list = smaller
    sorted_list.append(p)
    sorted_list += larger
    return sorted_list


my_list = [1, 5, 7, 9, 15]
print(sort_list(my_list))



"""
our_list = []
for _ in range(20): 
    our_list.append(random.randrange(100))



print("Input: ", end="")
new_list = []
while True:
    nmr = input()
    if nmr.isdecimal():
        for i in our_list:
            if i < int(nmr) and i//2 % 2 != 0:
                new_list.append(i)
        break
    else:
        print("Try again: ",end="")
print(new_list)
"""




def generate_list(l_amount, l_range):
    f_list = []
    for _ in range(l_amount):
        f_list.append(random.randrange(l_range))
    return f_list

def return_number():
    print("Enter a number: ", end="")
    while True:
        num = input()
        if num.isdecimal():
            return int(num)
        else:
            print("Try again: ", end="")

def remove_lows(f_list, num):
    new_list = []
    for i in f_list:
        if i > num:
            new_list.append(i)
    return new_list

def sort_odds(f_list):
    new_list = []
    for i in f_list:
        if i % 2 != 0:
            new_list.append(i)
    return new_list

#given_list = generate_list(20, 100)
#given_number = return_number()
#given_list = remove_lows(given_list, given_number)
#given_list = sort_odds(given_list)
#print(given_list)

### TBC