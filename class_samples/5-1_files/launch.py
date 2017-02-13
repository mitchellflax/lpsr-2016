my_list = ['Jenny', 'Oscar', 'Alonzo', 'Angela']

f = open("coolpeople.txt", "w")

for item in my_list:
    f.write(item + "\n")

f.close()
