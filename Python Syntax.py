#print statements
#print raw strings, print whatever is entered to the output
print(r'C:\users\docs')

Message = "Welcome User"
a = 10
#Memory Address of variables "Message" and "a" can be referenced using the function id()
#Note: In Python, the value is stored in a memory address and any new variables referenced will have the same address if the value is not changed
#Returns the memory address where the variable "Message"  is stored
#Note: If a value is not referenced or stored in a variable, then the concept of "Garbage Collection" is used to store the unassigned value
id(Message)

#Returns the memory address where the variable "a"  is stored
id(a)

# id("Welcome User") will also return the same address as id(Message)



#list
list = ["a", "b", "c", 2, 3]
#indexing
#indexing elements in a list
#if list = ["a", "b", "c", 2, 3], then we can index elements of a list as below

# list[0] will index the zeroth element "a"
# list[-1] will index the zeroth element "a"
# list[1:4] will index the second element and exclude the fourth element here (means last element mentioned will be excluded)
# list[1:] will index from the first element till the last element in the list
# list[:4] will index from the zeroth element till the third element, which means it excludes the fourth element.

#adding elements to a list
#appends number 45 to the end of the list name list
list.append(45)

#clear method clears or deletes all the elements in a list
list.clear

#inserts the value "Sunny" at position 2 in the list
list.insert(2, "Sunny")

#removes the first occurence of value "a" from the list
list.remove("a")

#remove a value from a list based on index or position, will be used if we don't know the value of the elements in the list (most real life situations)
#remove an element from the list at index 4, if index not specified will remove the last element added to the stack LIFO
list.pop(4)

#remove an element that is last added without mentioning any index
list.pop()

#delete elements from a list
#delete elements from the list starting from index 2 to the last element in the list
del list[2:]

#delete elements from the list starting from index 0 to the 3rd index, excluding the 4th element in the list
del list[:4]

#If we want to add multiple elements to the end of the list, use the extend method, but we need to mention that in a list 
list.extend([3, 4, 9, "santa"])

#A dictionary is used to a store a group of objects as Key Value pairs (also called as map, HashMap, hash in other languages like Java)
# A dictionary is unordered and the values of items can be changed by referencing the 'keys' in the dictionary
#Personal details can be stored and can be easily referenced when stored in a dictionary
#example dictionary
#***Note: We can have a list in a dictionary and a dictionary within a dictionary
#Here City is a LIST and Phone is a DICTIONARY
dict = {"Key1":"Value1", "Key2":"Value2" }
dict1 = {"Name": "Sunil", "City": ["Chicago", "Boston","LA", "Seattle"], "Age": 25, "Zipcode": 75932, "Phone":{"Phone1": 123, "Phone2": 345, "Phone3": 456}}

#indexing values from a dictionary using the key
dict["Key1"]

# We can update the values of a dictionary using the key but the key has to exist
dict['Key1'] = 'New Value1'

#Index a list "City" from dict1, using the key value
dict1["City"]

#Index a specific item, say index1 from a list "City" from dict1 (first index the dictionary and then list index the specfic item in a list)
dict1["City"][1]

#Index a dictionary "Phone" within a dictionary dict1 (first index dict1 and then index dictionary Phone from dict1)
dict1["Phone"]

#Index a specfic item from dictionary "Phone" within a dictionary dict1 (first index dict1 and then index dictionary Phone from dict1)
dict1["Phone"]["Phone1"]

#Map KEYS from a list to VALUES from a list
#Use Zip method to map keys to values and finally use a dictionary to convert to a dictionary
list1 = ["Name", "City", "Age", "Zipcode"]
list2 = ["Sunil", "Chicago", 32, 53428]
 
#Using a zip function to map keys in list1 to values in list2 and store them in a dict
# Zip function can be used to create a dictionary using two lists with one list being the keys
# and the other list being the values of that keys
dict3 = {zip(list1, list2)}
print("Dict 3 is: ", dict3)
#Outputs dict3 = {["Name": "Sunil", "City": "Chicago" , "Age": 32, "Zipcode": 53428


#Update a value in a dictionary, updates the value of key "City" to value "Boston"
# dict3["City"] = "Boston"

#Insert a new key value in to an existing dictionary if it doesn't exist, other update existing value
dict3["Phone"] = 1234

#Delete an item from a dictionary (using a key)
#Deletes an item (key and value) whose key is "Phone"
del dict3["Phone"]

#GET a specific item from a dictionary using GET method
dict1.get("Name")
dict.get("Key1")

#Index all items i.e both key and value in a dictionary
dict1.items()

#Index all keys in a dictionary
dict1.keys()

#Index values from a dictionary
dict1.values()

#Returns TRUE if all the Keys in a dictionary are TRUE
all(dict1)

#Returns TRUE if ANY of the key in the dictionary is TRUE
any(dict1)

#Returns a sorted list of keys from a dictionary
sorted(dict1)



#list
list = ["a", "b", "c", 2, 3]

#array


#hash map


#hash table


#parse tree


#docstring

##Python inbuilt functions

#returns the maximum element from both list1 and list2
max(list1, list2)

#returns the minimum element from both list1 and list2
min(list1, list2)

#add all the numbers in a given list
#if list1 contains all integers, then we can use the sum(list1) to output a single value after adding all the elements from a list
sum(list1)


##Sort the values from a list in increasing order using the sort method
#sorts the elements in a list in increasing order
list.sort(list1)

#Tuples
#Tuples are immutable, i.e can't be changed but can be indexed using the index number
# There are only two methods that can performed on a tuple => count and index
#Tuple can be used of a list if we don't want the values to be changed but needed the results faster
#Tuple is unordered
tuple1 = (34, 5, 67, 89)

#Sets
#Set is a collection of unique elements and is unordered
#set is much faster since it uses a concept has hash
#Even though duplicate values are present in a set, will only output single elements if they are duplicate, here 96 will be listed only once when set1 is printed
set1 = {56, 96, 45, 34, 96}

# rstrip() method
# rstrip() method removes a whitespaces or the character to be removed from a sentence.


# split() method

#map  function is used to perform an operation on a list with the desired output function such as converting to an integer or calling some function to get the desired output operation
map(function, list or tuple or string)
