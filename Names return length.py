# Program to take 10 names from user and then count the number of users who's name has greater than 5 letters

# manual input
# user_list = ["sunil", "johnny", "mike", "angelika", "todd"]
n = int(input("Enter the number of names to enter: "))

# Taking user input through list comprehension
user_list = list(j for j in input("Enter the list of names:").strip().split())[:n]

def user_count(user_list):
    count = 0
    for i in user_list:
        if len(i) > 5:
            count += 1
    return count


count_total = user_count(user_list)

print(count_total)
