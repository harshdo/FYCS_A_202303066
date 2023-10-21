# A for loop is used for itreating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["harsh", "abhijit","roshan","bhavesh"]

# using for loop
'''
for person in people:
    print(f"Current person: {person}")
   ''' 
# Break

'''
for person in people:
    if person == "abhijit":
        break
    print(f"Current person: {person}") 
   ''' 
# Continue

'''
for person in people:
    if person == "abhijit":
        continue
    print(f"Current person: {person}") 
'''

# Range
'''
for i in range(1,11):
    print("no.",+i) # or print(f"no.{i}")
'''

# While

count = 0
while count < 15:
    print(f"Count no.{count}")   #count += 1
                                 #print(f"Count no.{count}")
    count += 1





















    
