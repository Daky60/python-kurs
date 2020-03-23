
X = 1   ## int
Y = 4   ## int
addresses = {"Adam": "Ormvägen 5", ## dict
"Bella": "Klockgatan 1",
"Cornelia": "Vikingagatan 3"}  
cars = ["Volvo", "Opel", "BMW"] ## list
numbers1 = {1, 2, 3, X, 6}  ## set
numbers2 = {Y, 2, 3, 4, 7}  ## set


for i in (X, Y, addresses, cars, numbers1, numbers2):
    print(type(i))                              ## returns all types

addresses["Daniel"] = "Prinsgränd 2"            ## Adds item to dict
print(len(addresses))                           ## Returns length of dict
print(sorted(addresses.items())[-1][1])         ## Last person's address
addresses = {v:k for k, v in addresses.items()} ## 
print(sorted(addresses.items())[0][1])          ## First address' associated name

print(cars[X])                                  ## returns item with index #1 in cars list
#print(cars[Y])                                 ## out of range
cars.sort()                                     ## sorts list alphabetically
print(cars[0])                                  ## returns item with index #0 in cars list
cars_2 = cars                                   ## one and the same
cars.append("Saab")                             ## updates cars_2 too
print(cars, cars_2)                             ## returns both lists
cars_3 = cars.copy()                            ## copies cars list
cars.append("Mercedes")                         ## doesn't update cars_3
print(cars, cars_2, cars_3)                     ## returns all 3 lists
cars += cars                                    ## duplicates all items in list
print(sorted(set(cars), reverse=True))          ## Sorted in reverse alphabetical order and removes all duplicates

searchbase = []
for i in range(3):
    print("Enter name: ")
    name = input().title()
    print("Enter age: ")
    age = input()
    print("Enter size: ")
    size = input()
    person = dict({'Name': name, 'Age': age, 'Size': size})
    searchbase.append(person)


print(searchbase)
print("Please enter search value, name, age or size followed by value: ")
pull_info = input()
pull_info = pull_info.split()
for i in searchbase:
    if (pull_info[1].title()) in i[pull_info[0].title()]:
        print(f"Name: {i['Name']}\nAge: {i['Age']}\nSize: {i['Size']}")
