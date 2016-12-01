# this assigns the variable friends to the people and then prints it out based on which oes spend the most time with 
friends = ["Sam" , "David" , "Erick" , "Daniela" , "Robel"]
print("These are the five friends that I spend the most time with:")
number = 1

# this is going to put them in order lie, 1,2,3,4,5. 
for members in friends:
    print(str(number) + ". " + members)
    number = number + 1 

# this assaigns my other friends to friends2
friends2 = ["Raul", "Wendy" , "Michelle" , "Aly" , "Mayra"]

# this is going to sort and thenput my friends in reverse and then print the list of all my friends together
friends3 = friends + friends2
friends3.sort()
friends3.reverse()
print("These are my other friends:")
number = 1 
for members in friends3:
    print(str(number) + ". " + members)
    number = number + 1
