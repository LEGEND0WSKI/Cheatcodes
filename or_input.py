# Longer way of doing this
# name = input("Username: ")
# if name :
#     username =  name
# else:  
#     username = "Guest"

# Short way of doing this
# name = input("Username: ")
# username = name or "Guest"

# Shorter way of doing this
username = input("Username: ") or "Guest"

print(f"Hello, {username}!")