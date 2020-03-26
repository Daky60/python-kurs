


start = 2
finish = 15
while start < finish:
    control = False
    i = 2
    while i < start//2:
        if start % i == 0:
            control = True
            break
        i += 1
    if not control:
        print(start)    
    start += 1








"""
second_number = 2
my_number = 5


while second_number in range(2, my_number):
    second_number +=1
    if (my_number % second_number) == 0:
        print(second_number,"is not prime")
    else:
        print(my_number, second_number,"is prime")
"""



"""
control = 2
start = 2
finish = 100
prime_numbers = []


while control in range(start,finish):
    control+=1
    while start in range(2, control):
        start+=1
        if (control % start) != 0:
            print(start)        

"""

"""
while ( start > 1 and start < finish ):
    while control in range(start, finish):
        control+=1
        if ( start % control ) == 0:
            prime_numbers.append(start)
        else:
            print(start)
    start+=1
print(prime_numbers)
"""



"""
while start > 1 and start < finish:
    while start % 2 != 0:
        print(start, "is a prime number")
        prime_list.append(start)
        break
    start+=1
print(prime_list) 

"""


# Python program to display all the prime numbers within an interval
