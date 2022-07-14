#TASK 1
# Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.

letters = "alwnfiwaksuezlaeiajsdl"
l_list = [i for i in letters]
sorted_letters = sorted(l_list, reverse = True)
print(sorted_letters)
print(set(sorted_letters))


#TASK 2
#Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)
print(animals_sorted)


#TASK 3
'''
The dictionary, medals, shows the medal count for six countries during the Rio Olympics. 
Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.
'''

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
names = []
for key in medals.keys():
    names.append(key)

alphabetical = sorted(names)
    
print(names)
print(alphabetical)


#TASK 4
#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three=list(sorted(medals,key=lambda m:medals[m],reverse=True))[:3]
print(top_three)



#TASK 5
'''
We have provided the dictionary groceries. 
You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.
'''

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 
             'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = list(sorted(groceries, key = lambda a : groceries[a], reverse = True))
print(most_needed)


#TASK 6
'''
Create a function called last_four that takes in a single ID number and returns the last four digits. 
For example, the number 17573005 should return 3005. Then, use the resulting function to sort the list of ids stored in the variable, ids, from lowest to highest. 
Save this sorted list in the variable, sorted_ids. 
Hint: Remember that only strings can be indexed, so conversions may be needed.
'''

def last_four(x):
    x = sorted(x)
    four_ids = [id for id in x]
    return four_ids

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
ids_func = last_four(ids)
print(ids_func)

sorted_ids = []
for i in ids_func:
    sorted_ids.append(str(i)[-4:])
print(sorted_ids)


#TASK 7
'''
Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. 
Save this sorted list in the variable sorted_id.
'''

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = list(sorted(ids, key = lambda id: id%10000))
print(sorted_id)


#TASK 8
#Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = list(sorted(ex_lst, key = lambda a : a[1]))
print(lambda_sort)


