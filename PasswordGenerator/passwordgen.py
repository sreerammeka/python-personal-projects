#8 character Password Generator
#Need to fix some characters not appearing from the 4 lists, when generating random passwords.

#library for generating random numbers
import random

lc_list = ['a', 'b', 'c']
uc_list = ['A', 'B', 'C']
# num_list = ['1', '2', '3', '4']
#convert an integer to a string after every iteration
num_list = [str(i) for i in range(10)]
sc_list = ['!', '@']

print("num_list is", num_list)

#Select a random value from the list
#Choice takes O(1) time to retrieve random data from a sequence.
#Choice is faster than Shuffle
# lc= random.choice(lc_list)
# uc= random.choice(uc_list)
# num= random.choice(num_list)
# sc = random.choice(sc_list)

before_list = [lc_list, uc_list, num_list, sc_list]
# combined_list = [lc, uc, str(num), sc]

# shuffle_pass = random.shuffle(combined_list)
# shuffle_list = random.sample(combined_list, len(combined_list))
unmerged_shuffle_list = random.sample(before_list, len(before_list))
# shuffle_pass = random.choice(combined_list)

print("The unmerged shuffle list is", unmerged_shuffle_list)
#Shuffle takes O(N) time to index a full list or sequence, and O(1) time to retrieve value
# lc= random.shuffle(lc_list)
# uc= random.shuffle(uc_list)
# num= random.shuffle(num_list)
# sc = random.shuffle(sc_list)

def pswdgen():

#Converting a number to string and adding all lists to generate a random password
    # final_pass = lc + uc + str(num) + sc
    #Change length from 8 to 12 to convert to a 12 character password generator
    final_shuffle_pass = random.sample(unmerged_shuffle_list[0] + unmerged_shuffle_list[1] + unmerged_shuffle_list[2] + unmerged_shuffle_list[3], 8)
    
    return final_shuffle_pass
    # return final_pass, final_shuffle_pass, final_umerged_shuffle_pass


#Testing by assigning a function to a variable.
a = pswdgen()

print("The value of a is", a)

# finalpass = ''.join(a)
#The '' is used as a seperator to join between the characters, here everything will be concatenated to each other
# finalpass = ''.join(pswdgen())
finalpass = ''.join(a)

print("The final 8 character random password is", finalpass)



