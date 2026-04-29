art = '''                888                     
                888                     
                888                     
 .d8888b .d88b. 88888b. 888d888 8888b.  
d88P/   d88\/88b888 \88b888P/     \88b 
888     888  888888  888888    .d888888 
Y88b.   Y88..88P888 d88P888    888  888 
 \Y8888P \Y88P/ 88888P/ 888    \Y888888 '''
print(art)
print('\n')
print("---------------------")
print('Welcome to COBRA.')
print('Your mission is to KILL the COBRA.')
print('\n')

choice1 = input(
    'You awaken at a crossroad, where do you want to go?\nType "left" or "right".\n>  ').lower()


if choice1 == "left":

    choice2 = input(
        'As you walk you see in the distance a... table? Looking around, you sense no other prescence. ' \
        'On the table lies a single wodden club.\nType "acquire" to take it for yourself or "leave" to continue fowards.\n>  ').lower()
    
    choice3 = input(
        'You\'ve arrived at a lake, there is an island in the center of the lake.\nType "wait" to wave a passing boat or "swim" to simply swim across.\n>  ').lower()

    if choice3 == "wait":

        choice4 = input(
            'You reach a house with three doors: yellow, green, blue.\n>  '
        ).lower()

        if choice4 == "green":
            print("COBRA... GAME OVER.")

        elif choice4 == "yellow":
            print("You face the cobra...")

        elif choice4 == "blue":
            print("Water... GAME OVER.")

        else:
            print("Invalid door choice.")

    elif choice3 == "swim":
        print("Catfish eats you... GAME OVER.")

    else:
        print("Invalid lake choice.")


else:
    print("You fall into a hole... GAME OVER.")