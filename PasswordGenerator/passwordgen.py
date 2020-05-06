#Password Generator

#library for generating random numbers
import random

lc_list = ['a', 'b', 'c']
uc_list = ['A', 'B', 'C']
num_list = [1, 2, 3, 4]
sc_list = ['!', '@']


#Select a random value from the list
#Choice takes O(1) time to retrieve random data from a sequence.
#Choice is faster than Shuffle
lc= random.choice(lc_list)
uc= random.choice(uc_list)
num= random.choice(num_list)
sc = random.choice(sc_list)

combined_list = [lc, uc, str(num), sc]

shuffle_pass = random.shuffle(combined_list)
# shuffle_pass = random.sample(combined_list, len(combined_list))
# shuffle_pass = random.choice(combined_list)


#Shuffle takes O(N) time to index a full list or sequence, and O(1) time to retrieve value
# lc= random.shuffle(lc_list)
# uc= random.shuffle(uc_list)
# num= random.shuffle(num_list)
# sc = random.shuffle(sc_list)

def pswdgen():


#Converting a number to string and adding all lists to generate a random password
    final_pass = lc + uc + str(num) + sc
    final_shuffle_pass = shuffle_pass
    

    return final_pass, final_shuffle_pass

print("The random password is", pswdgen())
# print("The shuffled password is",
# print(final_pass)

#Testing by assigning a function to a variable.
a = pswdgen()

print("The value of a is", a)



