#Adventure game


def play_game():
    print("Welcome to Let's Play a Game adventure!")
    print("You have just arrived in Nairobi, you're in Machakos country bus!")
    print("1. Extremly tired, locate the nearest Restaurant and have a lunch? ")
    print("2. Proceed directly to Bus station and take your Mathree to Embakasi? ")

    options = input("Pick one option?\n" )

    if options == '1':
        find_restaurant()
    elif options == '2':
        proceed_to_Bus_station()
    else:
        print("Invalid option")
      
        
def find_restaurant():
    print("You find the restaurant, and since you have not eaten since morning, what do you choose?")
    print("1. Buy some yummy chicken drum sticks? ")
    print("2. Buy ugali nyama? ")

    find_options = input("Pick one option?\n")

    if find_options == '1':
        print("That was quite delicious!, time to go home!!")
    elif find_options == '2':
        print("I'm quite full, home here I come!!")
    else:
        print("Invalid option")

def proceed_to_Bus_station():
    print("You arrive at the Bus station, which Bus do you board?")
    print("1. Green bus? ")
    print("2. White Mathree? ")

    proceed_options = input("Pick one options?\n")
    if proceed_options == '1':
        print("Quite a spacious bus, I like it!")
    elif proceed_options == '2':
        print("I like the music, Its a trend!")
    else:
        print("Invalid option")
        
play_game()
