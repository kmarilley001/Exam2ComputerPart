# ask for type of destination
#   prints out a packing list for that vacation type

###############################################################################
# DONE: 1. (5 pts)
#
#   For this module, we are going to create a vacation planner that will help
#   the user plan what they need to bring on vacation.
#
#   For this _TODO_, write a function called starter_list() that takes 1
#   parameter:
#       - type      <-- str
#
#   This function should use a match case statement that checks for a matching
#   vacation type and returns a list of items that the user should probably
#   bring on that type of vacation.
#
#   So, for example, if the function is given the type "beach", the function
#   would return a list like this:
#
#      ["swimsuit", "towel", "sunscreen"]
#
#   For your function, make sure you have at least 3 vacation types and each
#   type should return a list of at least 3 items.
#
#   If the user types in an invalid vacation type, the function should return
#   an empty list.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
# Defined a function starter_list with a parameter vacation_type. Create a match  case function that returns the list. 

def starter_list(vacation_type): 
    match vacation_type: 
        case "Beach": 
            return ["swimsuit", "towel", "sunscreen"]
        case "Mountains": 
            return ["ski jacket", "gloves", "hat"]
        case "City": 
            return ["glasses", "metro card", "map"]
        case _: 
            return []

###############################################################################
# DONE: 2. (4 pts)
#
#   Now, perhaps the user would like to bring some of their own stuff that they
#   specify.
#
#   For this _TODO_, write a function called gather_items() that will
#   continually ask the user for an item to add to their list.
#
#   The function should meet these criteria:
#
#       1. Prompt the user like so:
#               "Please enter an item: "
#       2. It should keep track of all of the items in a list as it goes.
#       3. If the user types "end", it should stop asking for more items
#       4. Once it is done, it should return the list of items.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
# Defined a function that creates a list and utilizing a while loop user is able to iput their own items onto a list. 

def gather_items(): 
    items = []
    while True: 
        user_input = input("Please enter an item: ")
        if user_input.lower() == 'end': 
            break 
        items.append(user_input)
    return items
###############################################################################
# DONE: 3. (6 pts)
#
#   For this _TODO_, write a function called main() that will start things off.
#
#   Your function should meet these criteria:
#
#       1. It should first greet the user in a friendly way.
#       2. It should then prompt the user for a vacation type and allow them to
#          enter a vacation type.
#       3. It should then show them what item are already in their list based
#          on the type entered. There should be one item per line.
#       3. Next, it should start asking them for particular items and keep track
#          of them as the user enters more.
#       4. Once the user is done entering items, instead of printing the list of
#          items that they entered, it should print their entire list that
#          includes the starter list from the beginning and all the items that
#          they entered. You should do this by combining the lists and looping
#          through it printing each item. Do NOT just loop through the two lists
#          separately.
#       5. At the very end, it should say goodbye to the user in some friendly
#          way.
#
#   Make sure you call the function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
#Creating a main function that incorporates the two functions listed aboved. Which then ca combine the starter list and the user created list by using a for loop its able to print. 

def main(): 
    print("Welcome to the Vacation Planner!")
    vacation_type = input("Pleaser enter your vacation type: ")
    starter_items = starter_list(vacation_type)
    for item in starter_items: 
        print(f"{starter_items}")
    
    
    user_items = gather_items()

    combined_list = starter_items + user_items

    print("Your complete packing list: ")
    for item in combined_list: 
        print(item)

    print("Goodbye! Have a wonderful vacay!")

main()

