


full_sentence = first_string, second_string, third_string = "Jag tYcker om äGg", "inte", "SPAM"

### V1
split_first_string = first_string.title().swapcase().rsplit(" ", 2)
compiled_string = (f"{split_first_string[0]} {second_string.title().swapcase()} {split_first_string[1]} {third_string}")
print(compiled_string)

### V2
list_index = [0, 1, 4 , 2, 5]

convert_to_list = (
    f"""
    {first_string}
    {second_string}
    """.title().swapcase() 
    + third_string
).split()

list_wanted_items = [convert_to_list[i] for i in list_index]
convert_to_string = (' '.join(list_wanted_items))
print(convert_to_string)

### V3
initial_list = ((f"{first_string} {second_string} ").title().swapcase() + third_string).split()
print(' '.join([initial_list[i] for i in [0,1,4,2,5]]))


### V4

