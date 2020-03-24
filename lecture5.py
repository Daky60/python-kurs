
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

## filter edition

## Find oldest person
oldest_person = max(map(lambda x: x['Age'], searchbase))
oldest_person_data = next(filter(lambda x: oldest_person == x['Age'], searchbase))
print(f"The oldest person is {oldest_person_data['Name']} who has shoe size {oldest_person_data['Size']}")


## Find median shoesized person
median_sized_person = sorted(map(lambda x: x['Size'], searchbase))[len(searchbase)//2]
median_sized_person_data = next(filter(lambda x: median_sized_person == x['Size'], searchbase))    ## filter edition
print(f"The person with median shoe size is {median_sized_person_data['Name']} who is {median_sized_person_data['Age']} years old")


## Find any person
print("Please enter search value, name, age or size followed by value: ")
pull_info = input().title().split()
find_requested_person = next(filter(lambda x: pull_info[1] in x[pull_info[0]], searchbase))
print(f"Name: {find_requested_person['Name']}\nAge: {find_requested_person['Age']}\nSize: {find_requested_person['Size']}")






## map edition

## Find oldest person
#find_old_person = map(lambda x: oldest_person in x['Age'], searchbase)
#find_old_person_index = list(find_old_person).index(True)
#print(f"The oldest person is {searchbase[find_old_person_index]['Name']} who has shoe size {searchbase[find_old_person_index]['Size']}")

## Find median shoesized person
#median_sized_person = sorted(map(lambda x: x['Size'], searchbase))[len(searchbase)//2]
#find_median_sized_person = map(lambda x: median_sized_person in x['Size'], searchbase)
#ind_median_sized_person_index = list(find_median_sized_person).index(True)
#print(f"The person with median shoe size is {searchbase[find_median_sized_person_index]['Name']} who is {searchbase[find_median_sized_person_index]['Age']} years old")

## Find any person
#find_requested_person = map(lambda x: pull_info[1] in x[pull_info[0]], searchbase)
#find_requested_index = list(find_requested_person).index(True)
#print(f"Name: {searchbase[find_requested_index]['Name']}\nAge: {searchbase[find_requested_index]['Age']}\nSize: {searchbase[find_requested_index]['Size']}")

## Easy version
#print("Please enter search value, name, age or size followed by value: ")
#pull_info = input()
#pull_info = pull_info.split()
#for i in searchbase:
#    if (pull_info[1].title()) in i[pull_info[0].title()]:
#        print(f"Name: {i['Name']}\nAge: {i['Age']}\nSize: {i['Size']}")
