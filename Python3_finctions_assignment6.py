#TASK 1
'''
Write a function, sublist, that takes in a list of numbers as the parameter. 
In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
'''

def sublist(nums_list):
    without_five = []
    x = 0
    if 5 not in nums_list:
        return nums_list
    
    while nums_list[x] != 5:
        without_five.append(nums_list[x])
        x += 1
    return without_five


nums_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(sublist(nums_list))
nums1_list = [5]
print(sublist(nums1_list))
nums2_list = [8, 6, 5]
print(sublist(nums2_list))



#TASK2
'''
Write a function called check_nums that takes a list as its parameter, 
and contains a while loop that only stops once the element of the list is the number 7. 
What is returned is a list of all of the numbers up until it reaches 7.
'''

def check_nums(nums_list):
    stop_at_seven = []
    x = 0
    if 7 not in nums_list:
        return nums_list
    
    while nums_list[x] != 7:
        stop_at_seven.append(nums_list[x])
        x += 1
    return stop_at_seven


nums_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(check_nums(nums_list))
nums1_list = [7]
print(check_nums(nums1_list))
nums2_list = [8, 6, 7, 5]
print(check_nums(nums2_list))


#TASK 3
'''
Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
'''

def sublist(str_list):
    without_stop = []
    x = 0
    if 'STOP' not in str_list:
        return str_list
    
    while str_list[x] != 'STOP':
        without_stop.append(str_list[x])
        x += 1
    return without_stop

words_list = ['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']
print(sublist(words_list))


#TASK 4
'''
Write a function called stop_at_z that iterates through a list of strings. 
Using a while loop, append each string to a new list until the string that appears is “z”. 
The function should return the new list.
'''

def stop_at_z(str_list):
    no_z = []
    x = 0
    if 'z' not in str_list:
        return str_list
    
    while str_list[x] != 'z':
        no_z.append(str_list[x])
        x += 1
    return no_z

words_list = ['bob', 'joe', 'lucy', 'z', 'zz', 'carol', 'james']
print(stop_at_z(words_list))



#TASK 5
'''
Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, 
but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. 
Once complete, sum2 should equal sum1.
'''

sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

print(sum1)

sum2 = 0
y = 0
while y < len(lst):
    sum2 += lst[y]
    y += 1
    
print(sum2)
print(sum2 == sum1)



#CHALLENGE
'''
Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. 
What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. 
(i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) 
If you want to make this even more of a challenge, do this without slicing
'''

def beginning(str_list):
    no_bye = []
    x = 0
    if 'bye' not in str_list:
        return str_list
    
    while str_list[x] != 'bye':
        no_bye.append(str_list[x])
        x += 1
        if len(no_bye) == 10:
            break
    return no_bye

words_list = ['bob', 'joe', 'lucy', 'bye', 'zz', 'carol', 'james']
words2_list = ['hello', 'hi', 'hiyah', 'howdy', 'what up','whats good', 
               'holla', 'good afternoon', 'good morning', 'sup', 
               'see yah', 'toodel loo', 'night', 'until later', 
               'peace', 'bye', 'good-bye', 'g night']
print(beginning(words_list))
print(beginning(words2_list))