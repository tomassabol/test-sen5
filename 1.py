import random
list1 = "02468"
list2 = "13579"
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



with open("hesla.txt", 'w') as file:
    for i in range(20):
        password = ""
        for j in range(5):
            password += random.choice(list1)
            password += random.choice(list2)
            password += random.choice(a)
        file.write(password+"\n")
