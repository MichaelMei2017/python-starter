print('''

##### #####  ######   ##    ####  #    # #####  ######    #  ####  #        ##   #    # #####  
  #   #    # #       #  #  #      #    # #    # #         # #      #       #  #  ##   # #    # 
  #   #    # #####  #    #  ####  #    # #    # #####     #  ####  #      #    # # #  # #    # 
  #   #####  #      ######      # #    # #####  #         #      # #      ###### #  # # #    # 
  #   #   #  #      #    # #    # #    # #   #  #         # #    # #      #    # #   ## #    # 
  #   #    # ###### #    #  ####   ####  #    # ######    #  ####  ###### #    # #    # #####  

''')

print("Welcome to the treasure island game")
print('You\'re on the mission to find the treasure')

print( "You are at a cross road do you to go 'left or right'")
# _____________________________________________________
#right--> you fell into a hole. Game over
direction=input(" ")
if direction == "left":
    print("You come to a lake. There is an island in the middle of the lake. "
          "Type 'wait'  to 'wait' for a boat. Type 'swim' to swim across")
    action=input("You choose to:")
    if action == "wait":
        print("you arrived at the island unharmed."
              "there is a house with 3 doors, one yellow and one blue.")
        color=input("What color do you choose?")
        if color == "red":
            print("A room full of fire. Game over!")
        elif color == "blue":
            print("you entered a room of beast. Game over!")
        else:
            print("you found the treasure. you win!")

    else:
        print("you got attacked by an angry trout. Game over!")
else:
    print("you fell into a hole. Game over!")
# left-> You come to a lake . there is an island in the middle of the lake type 'wait'  to 'wait' to wait for a boat. type 'swim ' to swim across;;;
# swim you got attacked by an angry trout. Game over

# _______________________________________________________

# wait->you arrived at the island unharmed.there is a house with 3 doors , one yellow and one blue , which color you choose?
# _______________________________________________________

# blue-> you entered a room of beast game over
# red--> A room full of fire. Game over
# yellow-> you found the treasure you win
